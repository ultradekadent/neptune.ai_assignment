import pytest, json
from playwright.sync_api import expect
from pages.single_run import Attributes, Common


with open("test_files\\attributes.json") as f:
    attribute_data = json.load(f)


@pytest.mark.attributes_match_data
@pytest.mark.flaky(retries=3, delay=5)
@pytest.mark.parametrize("attr", attribute_data)
def test_attr_values_match_expected_data(page, attr):
    attr_selectors=Attributes(page)
    common_selectors=Common(page)

    # Assert that the 'Attributes' tab is visible within 10 seconds
    expect(attr_selectors.attributes_tab).to_be_visible(timeout=10_000)

    # Input the attribute path and name in the search bar
    attr_selectors.search_bar.fill(attr["path"]+("/")+attr["name"])

    # Click on the first matching item.
    attr_selectors.matching_items.first.click()

    # Assert that the attribute value matches expected data.
    expect(attr_selectors.preview_content).to_have_text(attr["value"], timeout=10_000)