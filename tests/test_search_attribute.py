import pytest
from playwright.sync_api import expect
from pages.single_run import Attributes


SEARCH_QUERY = "layer"


@pytest.mark.attributes_search
@pytest.mark.flaky(retries=3, delay=5)
def test_search_attribute(page):
    attr_selectors=Attributes(page)

    # Assert that the 'Attributes' tab is visible within 10 seconds
    expect(attr_selectors.attributes_tab).to_be_visible(timeout=10_000)

    # Input the search query, simulating key presses.
    attr_selectors.search_bar.type(SEARCH_QUERY, delay=80)

    # Assert that the search query returns matching results
    expect(attr_selectors.matching_results_list).not_to_be_empty()

    # Assert that every matching result contains the searched query
    for i in range(attr_selectors.matching_items.count()):
        assert SEARCH_QUERY in attr_selectors.matching_items.nth(i).inner_text().lower()

    # Get results count
    result_count_from_text, result_count_from_list = attr_selectors.get_result_count()

    # Assert that the results count from text matches the count from returned list
    assert result_count_from_text == result_count_from_list