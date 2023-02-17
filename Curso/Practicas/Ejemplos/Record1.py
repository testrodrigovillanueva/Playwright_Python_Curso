from playwright.sync_api import Playwright, sync_playwright, expect

#playwright codegen  https://demoqa.com/

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://demoqa.com/
    page.goto("https://demoqa.com/")

    # Click svg >> nth=0
    page.locator("svg").first.click() 
    page.wait_for_url("https://demoqa.com/elements")

    # Click text=Text Box
    page.locator("text=Text Box").click()
    page.wait_for_url("https://demoqa.com/text-box")

    # Click [placeholder="Full Name"]
    page.locator("[placeholder=\"Full Name\"]").click()

    # Fill [placeholder="Full Name"]
    page.locator("[placeholder=\"Full Name\"]").fill("Rodrigo")

    # Press Tab
    page.locator("[placeholder=\"Full Name\"]").press("Tab")

    # Click [placeholder="name\@example\.com"]
    page.locator("[placeholder=\"name\\@example\\.com\"]").click()

    # Fill [placeholder="name\@example\.com"]
    page.locator("[placeholder=\"name\\@example\\.com\"]").fill("rodrigo@gmail.com")

    # Click #currentAddress
    page.locator("#currentAddress").click()

    # Fill #currentAddress
    page.locator("#currentAddress").fill("Demo uno")

    # Press Tab
    page.locator("#currentAddress").press("Tab")

    # Click #permanentAddress
    page.locator("#permanentAddress").click()

    # Fill #permanentAddress
    page.locator("#permanentAddress").fill("Demo dos")

    # Click text=Submit
    page.locator("text=Submit").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
