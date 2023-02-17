import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright
 
#pytest --slowmo 1000  --headed Input2.py

# def test_input2(page: Page):    
#     page.goto("https://testingqarvn.com.es/datos-personales/")
#     expect(page).to_have_title("Datos Personales | TestingQaRvn")


def test_input2(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=500)
    #context=browser.new_context()    
    context=browser.new_context(record_video_dir="Videos/Input2/")
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 800 }
    )
    page=context.new_page()
    #page.set_viewport_size({"width": 1500, "height": 700})
    page.goto("https://testingqarvn.com.es/datos-personales/")
    expect(page).to_have_title("Datos Personales | TestingQaRvn")
    page.set_default_timeout(5000)
    
    
    nombre=page.locator("#wsf-1-field-21")
    expect(nombre).to_be_visible()
    expect(nombre).to_be_enabled()
    expect(nombre).to_be_empty()
    expect(nombre).to_have_id("wsf-1-field-21")
    page.locator("#wsf-1-field-21").fill("Rodrigo")
    page.screenshot(path="Imagenes/input2/nombre.png")  
    expect(page).to_have_url(re.compile(".*datos-personales/"))    
    
    page.locator("//input[contains(@id,'wsf-1-field-22')]").fill("Villanueva Nieto")    
    page.screenshot(path="Imagenes/input2/apellidos.png")
    time.sleep(2)
    
    page.locator("//input[contains(@id,'wsf-1-field-23')]").fill("rodrigo@gmail.com")    
    page.screenshot(path="Imagenes/input2/email.png")
    
    page.locator("#wsf-1-field-24").fill("5547898578")    
    page.screenshot(path="Imagenes/input2/telefono.png")
    
    page.locator("//textarea[contains(@id,'wsf-1-field-28')]").fill("Dirección demo 2")    
    page.screenshot(path="Imagenes/input2/Dirección.png")
    
    boton=page.is_visible("#wsf-1-field-27")
    if boton:
        print(boton) 
        page.locator("#wsf-1-field-27").click()  
    else:
        print("No se Encuentar el Boton")
        print(boton)
    page.screenshot(path="Imagenes/input2/submit.png")
    
    expect(page).to_have_url(re.compile(".*datos-personales/"))
    
    gracias=page.locator("//p[contains(.,'Gracias por tu encuesta.')]")
    expect(gracias).to_contain_text("Gracias")
    
    print("Termina la prueba")
    
    
    #Cerrar Context y Navegador     
    context.close()
    browser.close()
    
    
with sync_playwright() as playwright:
    test_input2(playwright)
    
    
    
    
    
    
   