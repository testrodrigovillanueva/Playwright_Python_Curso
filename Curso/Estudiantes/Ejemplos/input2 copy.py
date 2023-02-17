import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright

#pytest --slowmo 2000  --headed input2.py

def test_input2(page: Page):    
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
    
    boton=page.is_visible("#wsf-1-field-27887")
    print(boton)
    if boton:
        page.locator("#wsf-1-field-27").click()  
    else:
        print("No se Encuentar el Boton")
        print(boton)
    #page.screenshot(path="Imagenes/input2/submit2.png")
    
    
    #expect(page).to_have_url(re.compile(".*datos-personalesss/"))
    
    
    
    

    