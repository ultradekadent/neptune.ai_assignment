import pytest
from playwright.sync_api import expect
from pages.single_run import Attributes


ATTRIBUTE_PATH = "sys/diagnostics/attributes/bool_count"


@pytest.mark.attributes_navigate_tree
@pytest.mark.flaky(retries=3, delay=5)
def test_navigate_tree(page):
    attr_selectors=Attributes(page)

    # Assert that the 'Attributes' tab is visible within 10 seconds.
    expect(attr_selectors.attributes_tab).to_be_visible(timeout=10_000)

    # Navigate to known namespace & attribute
    attr_selectors.sys_namespace.click()
    attr_selectors.diagnostics_namespace.click()
    attr_selectors.attributes_namespace.click()
    attr_selectors.bool_count_attr.click()

    # Check if the preview header displays the correct path
    expect(attr_selectors.preview_header).to_contain_text(ATTRIBUTE_PATH, timeout=1000)