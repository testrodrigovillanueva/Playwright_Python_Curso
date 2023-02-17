import re
import time
import random
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#Variables globales
tiempo=1.5
ruta="Imagenes/Select/"

def test_select2(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)  
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 800 }
      #record_video_dir="Videos/Checkbox/"
    )
    page=context.new_page()    
    page.goto("https://testingqarvn.com.es/combobox-dependiente/")   
    
    page.set_default_timeout(5000)
    #expect(page).to_have_title("ComboBox Dependiente | TestingQaRvn")
    
   
    numA2=random.sample(range(1,100000),6)
    numA3=random.sample(range(1,100000),6)
    
    #Creando nuestro Objeto de tipo Funciones Globales
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("ComboBox Dependiente | TestingQaRvn")
    #time.sleep(1)
    #page.mouse.wheel(0, 400)
    F.Scroll_xy(0,400)
    F.Esperar(tiempo)
    
    #nombre
    F.Texto_img("//input[contains(@id,'wsf-1-field-54')]","Rodrigo"+str(numA2[0]),ruta+"Nombre"+str(numA2[0])+".png",tiempo)
    F.Texto("//input[contains(@id,'wsf-1-field-55')]","Villanueva",tiempo)
    F.Texto("//input[contains(@id,'wsf-1-field-56')]","rodrigo@gmail.com",tiempo)
    F.Texto_img("//input[contains(@id,'wsf-1-field-57')]","5544"+str(numA3[0]),ruta+"Tel.png",tiempo)
    F.Texto("//textarea[contains(@id,'wsf-1-field-58')]","Demo de la Dirección",tiempo)
    
    
    #checkbox
    F.Scroll_xy(0,700)
    F.Click("//label[contains(@id,'wsf-1-label-59-row-1')]",tiempo)
    F.Click_img("//label[contains(@id,'wsf-1-label-60-row-3')]",ruta+"Radio.png",tiempo)
    
    #ComboBox
    F.Combo_value_img("//select[contains(@id,'wsf-1-field-61')]","Linux",ruta+"Combo.png",tiempo)
    
    #Metodo Random
    numA=random.sample(range(1,4),1)
    print(numA[0])
    #F.Combo_label_img("//select[contains(@id,'wsf-1-field-64')]","Mac",ruta+"Combo2.png",tiempo)
    
    if numA[0]==1:
      print("Es el uno")
      F.Combo_label_img("//select[contains(@id,'wsf-1-field-64')]","Ubuntu",ruta+"Combo2.png",tiempo)
    elif numA[0]==2:
      print("es el dos")
      F.Combo_label_img("//select[contains(@id,'wsf-1-field-64')]","Debian",ruta+"Combo2.png",tiempo)
    elif numA[0]==3:
      print("es el tres")
      F.Combo_label_img("//select[contains(@id,'wsf-1-field-64')]","Read Hat",ruta+"Combo2.png",tiempo)
    
    
    
    #Submit
    F.Click("//button[contains(@id,'wsf-1-field-62')]",tiempo)
    
    #Validar Confirmación
    F.Validar_texto_img("//p[contains(.,'Gracias por tu encuesta.')]","Gracias",ruta+"Respuesta.png",tiempo)    
    
    #validar url
    F.Validar_url("https://testingqarvn.com.es/combobox-dependiente/",tiempo)
    
    
    F.Esperar(2)
    context.close()
    browser.close()