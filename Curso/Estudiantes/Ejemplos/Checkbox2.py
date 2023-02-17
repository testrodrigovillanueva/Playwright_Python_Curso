#playwright codegen  https://demoqa.com/checkbox

import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright


def test_checkbox2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context=browser.new_context(record_video_dir="Videos/Input")
    context=browser.new_context(
        viewport={'width':1500, 'height':800}
    )

    # Open new page
    page = context.new_page()

    # Go to https://demoqa.com/checkbox
    page.goto("https://demoqa.com/checkbox")

    # Click [aria-label="Toggle"]
    page.locator("[aria-label=\"Toggle\"]").click()

    # Click [aria-label="Toggle"] >> nth=1
    page.locator("[aria-label=\"Toggle\"]").nth(1).click()

    # Click text=NotesCommands >> svg >> nth=2
    page.locator("text=NotesCommands >> svg").nth(2).click()

    # Click [aria-label="Toggle"] >> nth=2
    page.locator("[aria-label=\"Toggle\"]").nth(2).click()

    # Click text=WorkSpaceOffice >> [aria-label="Toggle"] >> nth=0
    page.locator("text=WorkSpaceOffice >> [aria-label=\"Toggle\"]").first.click()

    # Click li:nth-child(2) > ol > li > ol > li:nth-child(2) > .rct-text > label > .rct-checkbox > .rct-icon
    page.locator("li:nth-child(2) > ol > li > ol > li:nth-child(2) > .rct-text > label > .rct-checkbox > .rct-icon").click()

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     test_checkbox2(playwright)
