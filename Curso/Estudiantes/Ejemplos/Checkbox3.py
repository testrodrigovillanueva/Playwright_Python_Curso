#playwright codegen  https://demoqa.com/checkbox

import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright


def test_checkbox3(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    #context=browser.new_context(record_video_dir="Videos/Input")
    context=browser.new_context(
        viewport={'width':1500, 'height':800}
        #record_video_dir="Videos/Checkbox"        
    )
    # Open new page
    page = context.new_page()

    page.goto("https://testingqarvn.com.es/prueba-de-campos-checkbox/")
    expect(page).to_have_title("Prueba de campos Checkbox | TestingQaRvn")    
    #Tiempo de Espera
    page.set_default_timeout(5000)
    
    #Scrholl de la página
    page.mouse.wheel(0,400)    #Coordenas en x, y   x=0, y=400
    time.sleep(2)
    
    #nombre
    page.locator("//input[contains(@id,'wsf-1-field-29')]").fill("Rodrigo")
    page.locator("//input[contains(@id,'wsf-1-field-30')]").fill("Villanueva")
    page.locator("//input[contains(@id,'wsf-1-field-31')]").fill("rodrigo@gmail.com")
    page.locator("//input[contains(@id,'wsf-1-field-32')]").fill("54654654")
    page.locator("//textarea[contains(@id,'wsf-1-field-33')]").fill("Demo de la dirección")
    
    
    #CheckBox
    page.mouse.wheel(0,700)    
    time.sleep(2)
    # page.locator("//label[contains(.,'PHP')]").click()
    # page.locator("//label[contains(.,'PHP')]").click()
    # time.sleep(1)
    # page.locator("//label[contains(.,'JS')]").click()
    
    # page.locator("//label[contains(.,'PHP')]").check()
    # page.locator("//label[contains(.,'PHP')]").uncheck()
    # time.sleep(2)
    # page.locator("//label[contains(.,'JS')]").check()
    # page.locator("//label[contains(.,'JS')]").uncheck()
    # assert page.locator("//label[contains(.,'JS')]").is_checked() is False
    
    #(//label[contains(@class,'wsf-label')])[7]
    
    
    for i in range(7,10):   #7,8,9
        #print(i)
        # salida=f"(//label[contains(@class,'wsf-label')])[{i}]"
        # print(salida)
        # page.locator(salida).click()
        
        page.locator(f"(//label[contains(@class,'wsf-label')])[{i}]").click()
        time.sleep(1)
        
    
    
    # expect(page).to_have_url(re.compile(".*datos-personales/"))
    
    
    
    
    

   
 
    context.close()
    browser.close()


