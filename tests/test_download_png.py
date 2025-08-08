import pytest, re, os
from playwright.sync_api import expect
from pages.single_run import Attributes


@pytest.mark.attributes_download_png
@pytest.mark.flaky(retries=3, delay=5)
def test_download_png(page):
    attr_selectors=Attributes(page)

    # Assert that the 'Attributes' tab is visible within 10 seconds.
    expect(attr_selectors.attributes_tab).to_be_visible(timeout=10_000)

    # Navigate to known namespace & attribute
    attr_selectors.eval_namespace.click()

    attr_selectors.metrics_namespace.click()

    attr_selectors.loss_attr.click()

    # Assert that the 'Download' button is visible within 5 seconds.
    expect(attr_selectors.download_btn).to_be_visible()

    # Start waiting for the download
    with page.expect_download() as download_info:
        # Perform the action that initiates download.
        attr_selectors.download_btn.click()

        attr_selectors.download_as_img_btn.click()


        download = download_info.value

        # Verify file name and extension
        assert re.match("eval_metrics_loss.png", download.suggested_filename)

        file_name = download.suggested_filename #<-- maintaining original file name for verification
        destination_folder_path = "downloads"
        file = (os.path.join(destination_folder_path, file_name))
        download.save_as(file)    
    