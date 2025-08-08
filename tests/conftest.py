import pytest, json, os
from playwright.sync_api import sync_playwright
from pathlib import Path
from pages.single_run import Common, Attributes

BASE_URL = "https://scale.neptune.ai/o/examples/org/LLM-Pretraining/runs/details?viewId=standard-view&detailsTab=attributes&runIdentificationKey=llm_train-v945&type=experiment&compare=uMlyIDUTmecveIHVma0eEB95Ei5xu8F_9qHOh0nynbtM"


# Create and launch browser. This fixture supports cross-browser testing.
@pytest.fixture(params=["chromium"], scope="function")
def browser(request):
    browser_type = request.param

    with sync_playwright() as playwright:
        launch_args = {
            "headless": False,
            "slow_mo": 1200
            }

        launchers = {
            "chromium": lambda: playwright.chromium.launch(**launch_args),
            "firefox": lambda: playwright.firefox.launch(**launch_args),
            "chrome": lambda: playwright.chromium.launch(channel="chrome", **launch_args),
            "msedge": lambda: playwright.chromium.launch(channel="msedge", **launch_args),
            "webkit": lambda: playwright.webkit.launch(**launch_args),
        }

        if browser_type not in launchers:
            raise ValueError(f"Unsupported browser: {browser_type}")

        browser = launchers[browser_type]()
        
        yield browser

        browser.close()

# Create a browser context, open a new page
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(
        # permissions=["notifications"],
        # viewport={"width": 1024, "height": 768},
        # java_script_enabled=False
        )
    
    # context.tracing.start(screenshots=True, snapshots=True)

    page = context.new_page()

    common_selectors = Common(page)

    # Handle the cookies and guide popups
    def guide_handler(page):
        common_selectors.close_guide_popup_btn.click()
    
    page.add_locator_handler(common_selectors.guide_popup_title, guide_handler)

    def cookies_handler(page):
        common_selectors.accept_cookies_btn.click()
    page.add_locator_handler(common_selectors.cookies_popup_title, cookies_handler)

    def cookies_handler_2(page):
        common_selectors.accept_cookies_btn_2.click()
    page.add_locator_handler(common_selectors.cookies_popup_title_2, cookies_handler_2)

    # Navigate to the base URL
    page.goto(BASE_URL)

    # Wait for the tests to run
    yield page

    # context.tracing.stop(path = "trace.zip")
    
    # Close the browser context
    context.close()
   