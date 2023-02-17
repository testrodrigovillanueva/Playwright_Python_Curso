import re
import time
import random
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

tiempo=0.7
ruta="Imagenes/Calendarios/"


def test_select1(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)
    #context=browser.new_context()    
    #context=browser.new_context(record_video_dir="Videos/Checkbox/")
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 800 }
      #record_video_dir="Videos/Checkbox/"
    )
    page=context.new_page()    
    page.goto("https://testingqarvn.com.es/calendarios/")
    
    
    
    page.set_default_timeout(5000)
    page.mouse.wheel(0, 400)
    time.sleep(1)
    F=Funciones_Globales(page)
    #expect(page).to_have_title("ComboBox | TestingQaRvn")
    F.Validar_titulo_pagina("Calendarios | TestingQaRvn")
    
    
    
    
    F.Texto_Img("//input[contains(@id,'wsf-1-field-66')]","Rodrigo",ruta+"nombre.png",tiempo)
    F.Texto_Img("//input[contains(@id,'wsf-1-field-67')]","Villanueva",ruta+"apellido.png",tiempo)
    F.Texto("//input[contains(@id,'wsf-1-field-68')]","rodrigo@gmail.com",tiempo)
    F.Texto("//input[contains(@id,'wsf-1-field-69')]","667567",tiempo)
    F.Texto("//textarea[contains(@id,'wsf-1-field-70')]","Demo de la Dirección",tiempo)
    page.mouse.wheel(0, 700)
    time.sleep(1)
    
    #Random
    numAleatorio=random.sample(range(1, 3),1)  
    print(numAleatorio[0])   
    #Checkbox
    #F.Click("//label[contains(@id,'wsf-1-label-71-row-3')]",tiempo)
    #F.Click_Img("//label[contains(@id,'wsf-1-label-72-row-1')]",ruta+"combo2.png",tiempo)
    
    if numAleatorio[0]==1:          
          F.Click("//label[contains(@id,'wsf-1-label-71-row-1')]",tiempo)
    elif numAleatorio[0]==2:
          F.Click("//label[contains(@id,'wsf-1-label-71-row-2')]",tiempo)          
    elif numAleatorio[0]==3:
          F.Click("//label[contains(@id,'wsf-1-label-71-row-3')]",tiempo)
          
    F.Click("//label[contains(@id,'wsf-1-label-72-row-2')]",tiempo)
  
    
    
    
    #combo por valor 
    # F.Combo_value("//select[contains(@id,'wsf-1-field-61')]","Windows",tiempo)
    # F.Combo_label("//select[contains(@id,'wsf-1-field-63')]","Windows 10",tiempo)
    
    
    print(numAleatorio[0])  
    F.Combo_value("//select[contains(@id,'wsf-1-field-73')]","Windows",tiempo)
    if numAleatorio[0]==1:
          #print("es un uno")
          F.Combo_label("//select[contains(@id,'wsf-1-field-74')]","Windows 7",tiempo)
    elif numAleatorio[0]==2:
          #print("es un dos")
          F.Combo_label("//select[contains(@id,'wsf-1-field-74')]","Windows 10",tiempo)          
    elif numAleatorio[0]==3:
          #print("es un tres")
          F.Combo_label("//select[contains(@id,'wsf-1-field-74')]","Windows Server",tiempo)
          
    
    
    #Calendarios 
    #F.Texto("//input[contains(@id,'wsf-1-field-79')]","Septiembre 23, 2022",tiempo)
    F.Click("//input[contains(@id,'wsf-1-field-79')]")
    F.Click("(//div[contains(.,'28')])[9]")
    
    
    #Calendario2
    #F.Texto("//input[contains(@id,'wsf-1-field-78')]","Septiembre 24, 2022",tiempo)
    F.Click("//input[contains(@id,'wsf-1-field-78')]")
    F.Click("(//div[contains(.,'30')])[20]")
    #page.mouse.click(0,50)
    page.keyboard.press("Tab")
    F.Esperar(2)
    
    
    
    F.Click("//button[contains(@id,'wsf-1-field-77')]",tiempo)
    F.Esperar(2)
    
    #Validar la url
    #expect(page).to_have_url(re.compile(".*datos-personales/"))   
    F.Validar_url(".*calendarios/")
    
    #Validar Texto 
    F.Validar_contiene_texto("//p[contains(.,'Gracias por tu encuesta.')]","Gracias")
    
    #expect(page).to_have_url(re.compile(".*docs/intro"))
    
    
    context.close()
    browser.close()
    
    
    