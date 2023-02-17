import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright

#pytest --slowmo 2000  --headed input2.py

#def test_input2(page: Page):    
def test_input2(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=1000)
    #context=browser.new_context()
    context=browser.new_context(record_video_dir="Videos/Input")
    context=browser.new_context(
        viewport={'width':1500, 'height':800}
    )
    
    page=context.new_page()
    #page.set_viewport_size({"width": 600, "height": 700})    
    page.goto("https://testingqarvn.com.es/datos-personales/")
    expect(page).to_have_title("Datos Personales | TestingQaRvn")
    
    #Tiempo de Espera
    page.set_default_timeout(5000)
    
    page.locator("#wsf-1-field-21").fill("Rodrigo")
    page.screenshot(path="Imagenes/input2/nombre.png")
    
    
    #Aserts o Validadores
    apellidos=page.locator("#wsf-1-field-22")
    #Visible
    expect(apellidos).to_be_visible()    
    page.locator("#wsf-1-field-22").fill("Villanueva Nieto")
    
    
    
    #Enabled
    email=page.locator("#wsf-1-field-23")
    expect(email).to_be_enabled()
    #Empty tiene que estar Vacio
    expect(email).to_be_empty()    
    #Contiene el ID
    expect(email).to_have_id("wsf-1-field-23")    
    page.locator("//input[@id='wsf-1-field-23']").fill("rodrigo@gmail.com")
    page.screenshot(path="Imagenes/input2/email.png")
    #tiempo forzado
    time.sleep(0.5)
    
    
    page.locator("#wsf-1-field-24").fill("5578478578")
    page.locator("#wsf-1-field-28").fill("Dirección demo uno")
    
    #Validar si esta Visible
    # boton=page.locator("//button[@id='wsf-1-field-27']")
    # expect(boton).to_be_visible()
    
    boton=page.is_visible("#wsf-1-field-2723")  #True o False
    print(boton)
    if boton:
        print("Entro al True, es decir si lo encontro")
        page.locator("#wsf-1-field-27").click()  
    else:
        print("No se Encuentar el Boton")
        print(boton)        
    page.screenshot(path="Imagenes/input2/submit3.png")
    
    
    expect(page).to_have_url(re.compile(".*datos-personales/"))
    
    gracias=page.locator("//p[contains(.,'Gracias por tu encuesta.')]")
    expect(gracias).to_contain_text("Gracias")
    
    #Cerrar Context y Navegador     
    context.close()
    browser.close()
    

    
    

    