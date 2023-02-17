import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright
 
#pytest --slowmo 1000  --headed Input2.py
#locator.nth(index)

def test_checkbox3(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=100)
    #context=browser.new_context()    
    #context=browser.new_context(record_video_dir="Videos/Checkbox/")
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 800 }
      #record_video_dir="Videos/Checkbox/"
    )
    page=context.new_page()
    #page.set_viewport_size({"width": 1500, "height": 700})
    page.goto("https://testingqarvn.com.es/prueba-de-campos-checkbox/")
    expect(page).to_have_title("Prueba de campos Checkbox | TestingQaRvn")
    page.set_default_timeout(4000)
    
    elemento=page.locator("//input[contains(@id,'wsf-1-field-')]").nth(1)
    elemento.highlight()
    time.sleep(2)
    
    nombre=page.locator("//input[contains(@id,'wsf-1-field-29')]") 
    nombre.hover()
    apellido=page.locator("//input[contains(@id,'wsf-1-field-30')]")
    apellido.hover
    time.sleep(2)   
    nombre.highlight()
    nombre.hover()
    time.sleep(2)   
    nombre.fill("rodrigo")
    page.mouse.wheel(0, 400)
    time.sleep(1)
  
    page.locator("//input[contains(@id,'wsf-1-field-30')]").fill("Villanueva")
    page.locator("//input[contains(@id,'wsf-1-field-31')]").fill("rodrigo@gmail.com")
    page.screenshot(path="Imagenes/Checkbox/Apellidos.png")  
    expect(page).to_have_url(re.compile(".*prueba-de-campos-checkbox/")) 
    page.locator("//input[contains(@id,'wsf-1-field-32')]").fill("765675")
    page.locator("//textarea[contains(@id,'wsf-1-field-33')]").fill("Dirección uno")
    
    page.mouse.wheel(0, 700)
    #time.sleep(1)
    
    #php
    # page.locator("(//label[contains(@class,'wsf-label')])[7]").click()
    # page.locator("(//label[contains(@class,'wsf-label')])[7]").click()
    
    page.locator("(//label[contains(@class,'wsf-label')])[7]").check()
    assert page.locator("(//label[contains(@class,'wsf-label')])[7]").is_checked() is True
    #time.sleep(1)
    page.locator("(//label[contains(@class,'wsf-label')])[7]").uncheck()
    assert page.locator("(//label[contains(@class,'wsf-label')])[7]").is_checked() is False
    
  
    for i in range (7,10):    
          # a=f"(//label[contains(@class,'wsf-label')])[{i}]"
          # print(a)    
          # page.locator(a).click()
          page.locator(f"(//label[contains(@class,'wsf-label')])[{i}]").check()
          time.sleep(0.5)
    
    
    #expect(page).to_have_url(re.compile(".*datos-personales/"))
    
    

    time.sleep(3)
    ##Cerrar Context y Navegador     
    context.close()
    browser.close()
    
    
    
    
    
    
    
    
    
   