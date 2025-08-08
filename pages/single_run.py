import re
from playwright.sync_api import Page


class Common:
    def __init__(self, page: Page):
        self.page = page

        # Selectors pertaining to cookies-related popups:
        self.cookies_popup_title = page.get_by_text("Manage your cookies")

        self.accept_cookies_btn = page.get_by_role("button", name="Accept all")

        self.decline_cookies_btn = page.get_by_role("button", name="Decline all")

        self.accept_cookies_btn2 = page.get_by_role("button", name="OK, I get it")

        self.cookies_popup_title_2 = page.get_by_text("This website uses cookies")

        self.accept_cookies_btn_2 = page.get_by_role("button", name="OK, I get it")
        

        # Selectors pertaining to guide-related popups:
        self.guide_popup_title = page.locator("iframe[title=\"modal\"]").first.content_frame.get_by_role("heading", name="Play with the example Neptune")

        self.close_guide_popup_btn = page.locator("iframe[title=\"modal\"]").first.content_frame.get_by_test_id("close-button")
        



class Attributes:
    def __init__(self, page: Page):
        self.page = page

        self.attributes_tab = page.get_by_role("button", name="Attributes")

        self.attr_value_cell = page.locator("[aria-rowindex='1'] > .sv-file-list__column-preview")

        self.preview_header = page.locator("//span[@class='middle-ellipsis n--lineHeight-xxl n--fontSize-sm']/span[@class='middle-ellipsis__truncated-start']")

        self.download_btn = page.locator(".av-preview-header > .n--flex-span-auto > .n-Button")

        self.download_as_img_btn = page.get_by_text("Download as image (PNG 1920px)")

        self.download_as_csv_btn = page.get_by_text("Download data (CSV)")

        self.search_bar = page.get_by_role("textbox", name="Search attributes...")

        self.matching_results_list = page.locator(".filter-search-results") # This represents the list of matching items as a whole.

        self.matching_results_text = page.locator(".filter-search-with-dropdown__menu-title") # This represents the "Showing first n matching search results:" text.

        self.matching_items = page.locator(".n-DropdownItem") # This represents every individual matching item

        # self.preview_body = page.locator(".preview-body") 
        self.preview_content = page.locator(".text-preview-content")

        # These selectors pertain to namespaces
        self.eval_namespace = page.get_by_role("link", name="eval")

        self.metrics_namespace = page.get_by_role("link", name="metrics")

        self.sys_namespace = page.get_by_role("link", name="sys", exact=True)

        self.diagnostics_namespace = page.get_by_role("link", name="diagnostics")

        self.attributes_namespace = page.get_by_role("link", name="attributes")


        # These selectors pertain to attributes
        self.loss_attr = page.get_by_role("link", name="loss")

        self.bool_count_attr = page.get_by_role("link", name="bool_count")


    # Get results count
    def get_result_count(self):
        # Read the "Showing first n matching search results:" string.
        matching_items_text = (self.matching_results_text.inner_text()) 
        # Extract the number from the string using regex.
        match = re.search(r'\d+', matching_items_text) 

        # If the string has a number, put it in the variable
        if match:
            result_count_from_text = int(match.group())

        # Count actual returned items 
        result_count_from_list = (self.matching_items.count())
        return result_count_from_text, result_count_from_list
    

'''class Charts:
    def __init__(self, page: Page):
        self.page = page


class Dashboards:
    def __init__(self, page: Page):
        self.page = page'''
