import asyncio
from logging import handlers
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        #browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        await page.screenshot(path="Imagenes/async.png")
        print(await page.title())        
        await browser.close()

asyncio.run(main())