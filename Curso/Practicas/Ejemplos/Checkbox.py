import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright
 
#pytest --slowmo 1000  --headed Input2.py

# def test_input2(page: Page):    
#     page.goto("https://testingqarvn.com.es/datos-personales/")
#     expect(page).to_have_title("Datos Personales | TestingQaRvn")


def test_input2(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=3000)
    #context=browser.new_context()    
    context=browser.new_context(record_video_dir="Videos/Checkbox/")
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 800 }
    )
    page=context.new_page()
    #page.set_viewport_size({"width": 1500, "height": 700})
    page.goto("https://demoqa.com/checkbox")
    expect(page).to_have_title("ToolsQA")
    page.set_default_timeout(5000)
    
    
    # check1=page.locator("//button[contains(@aria-label,'Toggle')]")
    # expect(check1).to_be_visible()
    # # expect(nombre).to_be_enabled()
    # # expect(nombre).to_be_empty()
    # # expect(nombre).to_have_id("wsf-1-field-21")
    # page.locator("//button[contains(@aria-label,'Toggle')]").click()
    # page.screenshot(path="Imagenes/Checkbox/chek1.png")  
    # expect(page).to_have_url(re.compile(".*checkbox")) 
    
    #Click en Desktop
    # Click [aria-label="Toggle"]
    page.locator("[aria-label=\"Toggle\"]").click()
    # Click [aria-label="Toggle"] >> nth=1
    page.locator("[aria-label=\"Toggle\"]").nth(1).click()
    # Click text=NotesCommands >> svg >> nth=0
    page.locator("text=NotesCommands >> svg").nth(2).click()
    

       
    
   
    
    
    
    
    ##Cerrar Context y Navegador     
    context.close()
    browser.close()
    
    
    
    
    
    
    
    
    
   