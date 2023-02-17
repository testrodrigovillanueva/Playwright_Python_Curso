import re
import time
import random
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#Correr el Viewer 
#playwright show-trace trace.zip

tiempo=0.3
ruta="Imagenes/Upload/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"


def test_select1(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)
    #context=browser.new_context()    
    #context=browser.new_context(record_video_dir="Videos/Checkbox/")
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 800 }
      #record_video_dir="Videos/Checkbox/"
    )
    #Iniciar trace Viewer
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page=context.new_page()    
    page.goto("https://testingqarvn.com.es/upload-files/")
    
    
    
    page.set_default_timeout(5000)
    page.mouse.wheel(0, 400)
    time.sleep(1)
    F=Funciones_Globales(page)
    #expect(page).to_have_title("ComboBox | TestingQaRvn")
    F.Validar_titulo_pagina("Upload Files | TestingQaRvn")
    
    #Lanzando el Debug 
    #set PWDEBUG=1 
    #pytest Debug.py -s
    
    
    
    F.Texto_Img("//input[contains(@id,'wsf-1-field-80')]","Rodrigo",ruta+"nombre.png",tiempo)
    
    #Pausa para el Debug
    page.pause()


    F.Texto_Img("//input[contains(@id,'wsf-1-field-81')]","Villanueva",ruta+"apellido.png",tiempo)
    F.Texto("//input[contains(@id,'wsf-1-field-82')]","rodrigo@gmail.com",tiempo)
    F.Texto("//input[contains(@id,'wsf-1-field-83')]","667567",tiempo)
    F.Texto("//textarea[contains(@id,'wsf-1-field-84')]","Demo de la Dirección",tiempo)
    page.mouse.wheel(0, 700)
    time.sleep(1)
    
    #Random
    numAleatorio=random.sample(range(1, 3),1)  
    print(numAleatorio[0])   
    #Checkbox
    #F.Click("//label[contains(@id,'wsf-1-label-71-row-3')]",tiempo)
    #F.Click_Img("//label[contains(@id,'wsf-1-label-72-row-1')]",ruta+"combo2.png",tiempo)
    
    if numAleatorio[0]==1:          
          F.Click("//label[contains(@id,'wsf-1-label-85-row-1')]",tiempo)
    elif numAleatorio[0]==2:
          F.Click("//label[contains(@id,'wsf-1-label-85-row-2')]",tiempo)          
    elif numAleatorio[0]==3:
          F.Click("//label[contains(@id,'wsf-1-label-85-row-3')]",tiempo)
          
    F.Click("//label[contains(@id,'wsf-1-label-86-row-2')]",tiempo)
  
    
    
    
    #combo por valor 
    # F.Combo_value("//select[contains(@id,'wsf-1-field-61')]","Windows",tiempo)
    # F.Combo_label("//select[contains(@id,'wsf-1-field-63')]","Windows 10",tiempo)
    
    
    print(numAleatorio[0])  
    F.Combo_value("//select[contains(@id,'wsf-1-field-87')]","Windows",tiempo)
    
    if numAleatorio[0]==1:
          #print("es un uno")
          F.Combo_label("//select[contains(@id,'wsf-1-field-88')]","Windows 7",tiempo)
    elif numAleatorio[0]==2:
          #print("es un dos")
          F.Combo_label("//select[contains(@id,'wsf-1-field-88')]","Windows 10",tiempo)          
    elif numAleatorio[0]==3:
          #print("es un tres")
          F.Combo_label("//select[contains(@id,'wsf-1-field-88')]","Windows Server",tiempo)
          
    
    
    #Calendarios 
    #F.Texto("//input[contains(@id,'wsf-1-field-79')]","Septiembre 23, 2022",tiempo)
    F.Click("//input[contains(@id,'wsf-1-field-91')]")
    F.Click("(//div[contains(.,'23')])[9]")
    
    
    #Calendario2
    #F.Texto("//input[contains(@id,'wsf-1-field-78')]","Septiembre 24, 2022",tiempo)
    F.Click("//input[contains(@id,'wsf-1-field-92')]")
    F.Click("(//div[contains(.,'28')])[18]")
    #page.mouse.click(0,50)
    #F.Mouse_xy(0,50)
    #page.keyboard.press("Tab")
    F.Tab(2)
    #F.Esperar(2)
    
    #Upload file
    F.Upload_file("//input[contains(@id,'wsf-1-field-94')]",pdf1,1)
    
    #Mover el upload
    F.Upload_file_remove("//input[contains(@id,'wsf-1-field-94')]",1)
    
    #Upload file
    F.Upload_file_img("//input[contains(@id,'wsf-1-field-94')]",pdf1,ruta+"Upload.png",1)
    
    
    
    #Enviar
    F.Click("//button[contains(@id,'wsf-1-field-93')]",tiempo)
    F.Esperar(2)
    
    #Validar la url
    #expect(page).to_have_url(re.compile(".*datos-personales/"))   
    F.Validar_url(".*upload-files/")
    
    #Validar Texto 
    F.Validar_texto("//p[contains(.,'Gracias por tu encuesta.')]","Gracias")
    print("Se valida el Texto Gracias")
    
    #expect(page).to_have_url(re.compile(".*docs/intro"))
    
    
    #Cerrar y crear el viewer
    context.tracing.stop(path = "trace.zip")
    
    context.close()
    browser.close()
    
    
    