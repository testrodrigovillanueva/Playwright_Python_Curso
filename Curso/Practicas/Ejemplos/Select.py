import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

tiempo=1
ruta="Imagenes/Select/"


def test_select1(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)
    #context=browser.new_context()    
    #context=browser.new_context(record_video_dir="Videos/Checkbox/")
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 800 }
      #record_video_dir="Videos/Checkbox/"
    )
    page=context.new_page()    
    page.goto("https://testingqarvn.com.es/combobox/")
   
    
    page.set_default_timeout(5000)
    page.mouse.wheel(0, 400)
    time.sleep(1)
    F=Funciones_Globales(page)
    #expect(page).to_have_title("ComboBox | TestingQaRvn")
    F.Validar_titulo_pagina("ComboBox | TestingQaRvn")
    
    
    F.Texto_Img("//input[@id='wsf-1-field-45']","Rodrigo",ruta+"nombre.png",tiempo)
    F.Texto_Img("//input[@id='wsf-1-field-46']","Villanueva",ruta+"apellido.png",tiempo)
    F.Texto("//input[@id='wsf-1-field-47']","rodrigo@gmail.com",tiempo)
    F.Texto("//input[@id='wsf-1-field-48']","667567",tiempo)
    F.Texto("//textarea[contains(@id,'wsf-1-field-49')]","Demo de la Dirección",tiempo)
    page.mouse.wheel(0, 700)
    time.sleep(1)
    F.Click("//label[contains(@id,'wsf-1-label-50-row-1')]",tiempo)
    F.Click_Img("//label[contains(@id,'wsf-1-label-51-row-2')]",ruta+"combo2.png",tiempo)
    
    #combo por valor 
    #F.Combo_value("//select[contains(@id,'wsf-1-field-53')]","Linux",tiempo)
    F.Combo_label("//select[contains(@id,'wsf-1-field-53')]","Mac",tiempo)
    
    F.Click("//button[contains(@id,'wsf-1-field-52')]",tiempo)
    F.Esperar(3)
    
    #Validar la url
    #expect(page).to_have_url(re.compile(".*datos-personales/"))   
    F.Validar_url(".*combobox/")
    
    #Validar Texto 
    F.Validar_contiene_texto("//p[contains(.,'Gracias por tu encuesta.')]","Gracias")
    
    
    
    
    
    
    #expect(page).to_have_url(re.compile(".*docs/intro"))
    
    
    context.close()
    browser.close()
    
    
    