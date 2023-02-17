import re
from playwright.sync_api import Page, expect

#https://demoqa.com/


def test_uno(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page.locator("text=Get Started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()
    
    #Pantalla
    page.screenshot(path="Imagenes/ejemplo3.png")

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*docs/intro"))