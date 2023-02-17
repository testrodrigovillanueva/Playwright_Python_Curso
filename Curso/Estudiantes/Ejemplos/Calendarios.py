import re
import time
import random
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#Variables globales
tiempo=0.3
ruta="Imagenes/Calendarios/"

def test_Calendarios(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)  
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 800 }
      #record_video_dir="Videos/Checkbox/"
    )
    page=context.new_page()    
    page.goto("https://testingqarvn.com.es/calendarios/")   
    
    page.set_default_timeout(5000)    
    
   
    numA2=random.sample(range(1,100000),6)
    numA3=random.sample(range(1,100000),6)
    
    #Creando nuestro Objeto de tipo Funciones Globales
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Calendarios | TestingQaRvn")
    #time.sleep(1)
    #page.mouse.wheel(0, 400)
    F.Scroll_xy(0,400)
    F.Esperar(tiempo)
    
    #nombre
    F.Texto_img("//*[@id='wsf-1-field-66']","Rodrigo"+str(numA2[0]),ruta+"Nombre"+str(numA2[0])+".png",tiempo)
    F.Texto("//*[@id='wsf-1-field-67']","Villanueva",tiempo)
    F.Texto("//*[@id='wsf-1-field-68']","rodrigo@gmail.com",tiempo)
    F.Texto_img("//input[contains(@id,'wsf-1-field-69')]","5544"+str(numA3[0]),ruta+"Tel.png",tiempo)
    F.Texto("//textarea[contains(@id,'wsf-1-field-70')]","Demo de la Dirección",tiempo)
    
    
    #checkbox
    F.Scroll_xy(0,700)
    F.Click("//label[contains(@id,'wsf-1-label-71-row-3')]",tiempo)
    F.Click_img("//label[contains(@id,'wsf-1-label-72-row-1')]",ruta+"Radio.png",tiempo)
    
    #ComboBox
    F.Combo_value_img("//select[contains(@id,'wsf-1-field-73')]","Linux",ruta+"Combo.png",tiempo)
    
    #Metodo Random
    numA=random.sample(range(1,4),1)
    print(numA[0])    
    
    if numA[0]==1:
      print("Es el uno")
      F.Combo_label_img("//select[contains(@id,'wsf-1-field-75')]","Ubuntu",ruta+"Combo2.png",tiempo)
    elif numA[0]==2:
      print("es el dos")
      F.Combo_label_img("//select[contains(@id,'wsf-1-field-75')]","Debian",ruta+"Combo2.png",tiempo)
    elif numA[0]==3:
      print("es el tres")
      F.Combo_label_img("//select[contains(@id,'wsf-1-field-75')]","Read Hat",ruta+"Combo2.png",tiempo)
    
    
    #Calendarios
    #F.Texto("//input[contains(@id,'wsf-1-field-79')]","Septiembre 23, 2022",tiempo)
    # F.Click("//input[contains(@id,'wsf-1-field-79')]",tiempo)
    # F.Click("(//div[contains(.,'24')])[9]",tiempo)
    F.Click("//input[contains(@id,'wsf-1-field-79')]",tiempo)
    F.Click("(//div[contains(.,'24')])[9]")
    
    #Calendario2
    #F.Texto("//input[contains(@id,'wsf-1-field-78')]","Septiembre 24, 2022",tiempo)
    # F.Click("//input[contains(@id,'wsf-1-field-78')]",tiempo)
    # F.Click("(//div[contains(.,'29')])[20]",tiempo)
    F.Click("//input[contains(@id,'wsf-1-field-78')]",tiempo)
    F.Click("(//div[contains(.,'30')])[20]",tiempo)
    
    #Para hacer click en otra area y perder el foco
    #page.mouse.click(0,50)   #x , y
    #F.Mouse_xy(0,50)
    
    #Función para dar clic al teclado en la opción Tab
    #page.keyboard.press("Tab")
    F.Tab(3)
    
    
    
    #Submit
    F.Click("//button[contains(@id,'wsf-1-field-77')]",tiempo)
    
    #Validar Confirmación
    F.Validar_texto_img("//p[contains(.,'Gracias por tu encuesta.')]","Gracias",ruta+"Respuesta.png",tiempo)    
    
    #validar url
    F.Validar_url("https://testingqarvn.com.es/calendarios/",tiempo)
    
    
    F.Esperar(2)
    context.close()
    browser.close()