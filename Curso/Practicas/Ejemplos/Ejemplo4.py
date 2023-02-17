import re
from playwright.sync_api import Page, expect

#https://demoqa.com/


def test_uno(page: Page):
    page.goto("https://demoqa.com/")
    expect(page).to_have_title(re.compile("ToolsQA"))
    

    # create a locator
    page.locator("text=Elements").click()
    page.locator("text=Text Box").click()
    page.locator('#userName').fill('Rodrigo')
    page.locator('#userEmail').fill('rodrigo@gmail.com')
    page.locator("//textarea[contains(@id,'currentAddress')]").fill('Demo uno dirección')
    page.locator("//textarea[contains(@id,'permanentAddress')]").fill("dirección Permanente")
    page.locator("//button[contains(@id,'submit')]").click()
    
    

   

    
    #Pantalla
    page.screenshot(path="Imagenes/ejemplo4.png")

    # Expects the URL to contain intro.
    #expect(page).to_have_url(re.compile(".*docs/intro"))