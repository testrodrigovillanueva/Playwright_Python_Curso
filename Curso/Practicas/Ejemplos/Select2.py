import re
import time
import random
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

tiempo=0.7
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
    page.goto("https://testingqarvn.com.es/combobox-dependiente/")
    
    
    
    page.set_default_timeout(5000)
    page.mouse.wheel(0, 400)
    time.sleep(1)
    F=Funciones_Globales(page)
    #expect(page).to_have_title("ComboBox | TestingQaRvn")
    F.Validar_titulo_pagina("ComboBox Dependiente | TestingQaRvn")
    
    
    
    
    F.Texto_Img("//input[contains(@id,'wsf-1-field-54')]","Rodrigo",ruta+"nombre.png",tiempo)
    F.Texto_Img("//input[contains(@id,'wsf-1-field-55')]","Villanueva",ruta+"apellido.png",tiempo)
    F.Texto("//input[contains(@id,'wsf-1-field-56')]","rodrigo@gmail.com",tiempo)
    F.Texto("//input[contains(@id,'wsf-1-field-57')]","667567",tiempo)
    F.Texto("//textarea[contains(@id,'wsf-1-field-58')]","Demo de la Dirección",tiempo)
    page.mouse.wheel(0, 700)
    time.sleep(1)
    F.Click("//label[contains(@id,'wsf-1-label-59-row-2')]",tiempo)
    F.Click_Img("//label[contains(@id,'wsf-1-label-60-row-2')]",ruta+"combo2.png",tiempo)
    
    
    
    #combo por valor 
    # F.Combo_value("//select[contains(@id,'wsf-1-field-61')]","Windows",tiempo)
    # F.Combo_label("//select[contains(@id,'wsf-1-field-63')]","Windows 10",tiempo)
    
    #Random
    numAleatorio=random.sample(range(1, 3),1)
    print(numAleatorio[0])  
    F.Combo_value("//select[contains(@id,'wsf-1-field-61')]","Windows",tiempo)
    if numAleatorio[0]==1:
          #print("es un uno")
          F.Combo_label("//select[contains(@id,'wsf-1-field-63')]","Windows 7",tiempo)
    elif numAleatorio[0]==2:
          #print("es un dos")
          F.Combo_label("//select[contains(@id,'wsf-1-field-63')]","Windows 10",tiempo)          
    elif numAleatorio[0]==3:
          #print("es un tres")
          F.Combo_label("//select[contains(@id,'wsf-1-field-63')]","Windows Server",tiempo)
    
    
    
    F.Click("//button[contains(@id,'wsf-1-field-62')]",tiempo)
    F.Esperar(2)
    
    #Validar la url
    #expect(page).to_have_url(re.compile(".*datos-personales/"))   
    F.Validar_url(".*combobox-dependiente/")
    
    #Validar Texto 
    F.Validar_contiene_texto("//p[contains(.,'Gracias por tu encuesta.')]","Gracias")
    
    #expect(page).to_have_url(re.compile(".*docs/intro"))
    
    
    context.close()
    browser.close()
    
    
    