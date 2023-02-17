import re
import time
import random
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#Variables globales
tiempo=0.3
ruta="Imagenes/Upload/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"

def test_Upload(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)  
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 800 }
      #record_video_dir="Videos/Checkbox/"
    )
    page=context.new_page()    
    page.goto("https://testingqarvn.com.es/upload-files/")   
    
    page.set_default_timeout(5000)    
    
   
    numA2=random.sample(range(1,100000),6)
    numA3=random.sample(range(1,100000),6)
    
    #Creando nuestro Objeto de tipo Funciones Globales
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Upload Files | TestingQaRvn")
    #time.sleep(1)
    #page.mouse.wheel(0, 400)
    F.Scroll_xy(0,400)
    F.Esperar(tiempo)
    
    #nombre
    F.Texto_img("//*[@id='wsf-1-field-80']","Rodrigo"+str(numA2[0]),ruta+"Nombre"+str(numA2[0])+".png",tiempo)
    F.Texto("//*[@id='wsf-1-field-81']","Villanueva",tiempo)
    F.Texto("//*[@id='wsf-1-field-82']","rodrigo@gmail.com",tiempo)
    F.Texto_img("//*[@id='wsf-1-field-83']","5544"+str(numA3[0]),ruta+"Tel.png",tiempo)
    F.Texto("//*[@id='wsf-1-field-84']","Demo de la Dirección",tiempo)
    
    
    
    #checkbox
    F.Scroll_xy(0,700)
    F.Click("//label[contains(@id,'wsf-1-label-85-row-1')]",tiempo)
    F.Click_img("//label[contains(@id,'wsf-1-label-86-row-3')]",ruta+"Radio.png",tiempo)
    
    #ComboBox
    F.Combo_value_img("//select[contains(@id,'wsf-1-field-87')]","Linux",ruta+"Combo.png",tiempo)
    
    #Metodo Random
    numA=random.sample(range(1,4),1)
    print(numA[0])    
    
    if numA[0]==1:
      print("Es el uno")
      F.Combo_label_img("//select[contains(@id,'wsf-1-field-89')]","Ubuntu",ruta+"Combo2.png",tiempo)
    elif numA[0]==2:
      print("es el dos")
      F.Combo_label_img("//select[contains(@id,'wsf-1-field-89')]","Debian",ruta+"Combo2.png",tiempo)
    elif numA[0]==3:
      print("es el tres")
      F.Combo_label_img("//select[contains(@id,'wsf-1-field-89')]","Read Hat",ruta+"Combo2.png",tiempo)
    
    
    #Calendarios
    #F.Texto("//input[contains(@id,'wsf-1-field-79')]","Septiembre 23, 2022",tiempo)
    # F.Click("//input[contains(@id,'wsf-1-field-79')]",tiempo)
    # F.Click("(//div[contains(.,'24')])[9]",tiempo)
    F.Click("//*[@id='wsf-1-field-91']",tiempo)
    F.Click("(//div[contains(.,'29')])[10]")
    
    #Calendario2
    #F.Texto("//input[contains(@id,'wsf-1-field-78')]","Septiembre 24, 2022",tiempo)
    # F.Click("//input[contains(@id,'wsf-1-field-78')]",tiempo)
    # F.Click("(//div[contains(.,'29')])[20]",tiempo)
    F.Click("//*[@id='wsf-1-field-92']",tiempo)
    F.Click("(//div[contains(.,'30')])[20]",tiempo)
    
    #Para hacer click en otra area y perder el foco
    #page.mouse.click(0,50)   #x , y
    #F.Mouse_xy(0,50)
    
    #Función para dar clic al teclado en la opción Tab
    #page.keyboard.press("Tab")
    F.Tab(1)
    
    
    #Upload File 
    #F.Upload_file('//input[contains(@type, "file")]',pdf1,tiempo)
    F.Upload_file_img('//input[contains(@type, "file")]',pdf1,ruta+"Upload.png",tiempo)
    
    #Remove File
    F.Upload_file_remove('//input[contains(@type, "file")]',3)
    
    #Upload File 
    #F.Upload_file('//input[contains(@type, "file")]',pdf1,tiempo)
    F.Upload_file_img('//input[contains(@type, "file")]',pdf1,ruta+"Upload.png",tiempo)
    
    
    
    
    
    #Submit
    F.Click("//*[@id='wsf-1-field-93']",tiempo)
    
    #Validar Confirmación
    F.Validar_texto_img("//p[contains(.,'Gracias por tu encuesta.')]","Gracias",ruta+"Respuesta.png",tiempo)    
    
    #validar url
    F.Validar_url("https://testingqarvn.com.es/upload-files/",tiempo)
    
    
    F.Esperar(2)
    context.close()
    browser.close()