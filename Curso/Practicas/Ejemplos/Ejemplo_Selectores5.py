import re
import time
from playwright.sync_api import Page, expect

#https://demoqa.com/


def test_uno(page: Page):
    page.goto("https://demoqa.com/text-box")
    expect(page).to_have_title(re.compile("ToolsQA"))  
    page.set_default_timeout(5000)  
    
    #Seleccionar por Text
    #page.locator("text=Log in").click()    
    
    page.locator("text=Check Box").click()
    
    page.locator("text=Text Box").click()
    
   
    
    #Id  Selector
    page.locator('#userName').fill('Rodrigo')
    page.locator('#userEmail').fill('rodrigo@gmail.com')
    time.sleep(10)
    
    #Xpath
 
    page.locator("//textarea[contains(@id,'currentAddress')]").fill('Demo uno dirección')
    page.locator("//textarea[contains(@id,'permanentAddress')]").fill("dirección Permanente")
    
    #Selecting elements that contain other elements
    #page.locator("button", has_text="Click me").click()
    page.locator("button", has_text="Submit").click()
    
    
    

  
    

   

    
    #Pantalla
    page.screenshot(path="Imagenes/ejemplo5.png")

  