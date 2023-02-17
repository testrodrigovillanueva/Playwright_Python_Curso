import re
import time
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#Variables globales
tiempo=0.3
ruta="Imagenes/Select/"

def test_select1(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)  
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 800 }
      #record_video_dir="Videos/Checkbox/"
    )
    page=context.new_page()    
    page.goto("https://testingqarvn.com.es/combobox/")   
    
    page.set_default_timeout(5000)
    #expect(page).to_have_title("ComboBox | TestingQaRvn")
    
   
    
    
    #Creando nuestro Objeto de tipo Funciones Globales
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("ComboBox | TestingQaRvn")
    #time.sleep(1)
    #page.mouse.wheel(0, 400)
    F.Scroll_xy(0,400)
    F.Esperar(tiempo)
    
    #nombre
    F.Texto_img("//input[contains(@id,'wsf-1-field-45')]","Rodrigo",ruta+"Nombre.png",tiempo)
    F.Texto("//input[contains(@id,'wsf-1-field-46')]","Villanueva",tiempo)
    F.Texto("//input[contains(@id,'wsf-1-field-47')]","rodrigo@gmail.com",tiempo)
    F.Texto_img("//input[contains(@id,'wsf-1-field-48')]","5547878748",ruta+"Tel.png",tiempo)
    F.Texto("//textarea[contains(@id,'wsf-1-field-49')]","Demo de la Dirección",tiempo)
    
    
    #checkbox
    F.Scroll_xy(0,700)
    F.Click("//label[contains(@id,'wsf-1-label-50-row-2')]",tiempo)
    F.Click_img("//label[contains(@id,'wsf-1-label-51-row-2')]",ruta+"Radio.png",tiempo)
    
    #ComboBox
    F.Combo_value_img("//select[contains(@id,'wsf-1-field-53')]","Linux",ruta+"Combo.png",tiempo)
    
    F.Combo_label_img("//select[contains(@id,'wsf-1-field-53')]","Mac",ruta+"Combo2.png",tiempo)
    
    
    #Submit
    F.Click("//button[contains(@id,'wsf-1-field-52')]",tiempo)
    
    #Validar Confirmación
    F.Validar_texto_img("//p[contains(.,'Gracias por tu encuesta.')]","Gracias",ruta+"Respuesta.png",tiempo)    
    
    #validar url
    F.Validar_url("https://testingqarvn.com.es/combobox/",tiempo)
    
    
    F.Esperar(2)
    context.close()
    browser.close()