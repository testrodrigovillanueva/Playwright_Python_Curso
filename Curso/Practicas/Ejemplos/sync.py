from playwright.sync_api import sync_playwright
#https://playwright.dev/python/docs/library#incompatible-with-selectoreventloop-of-asyncio-on-windows

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()
    page.goto("http://playwright.dev")
    page.screenshot(path="Imagenes/primer.png")
    print(page.title())
    browser.close()