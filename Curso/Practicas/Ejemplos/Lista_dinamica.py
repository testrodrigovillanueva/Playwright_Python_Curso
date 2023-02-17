import re
import time
import random
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#playwright codegen https://demoqa.com/automation-practice-form

tiempo=0.1
ruta="Imagenes/Reto/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"


def test_Lista_dinamica(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)
    #context=browser.new_context()    
    #context=browser.new_context(record_video_dir="Videos/Checkbox/")
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 700 }
      #record_video_dir="Videos/Checkbox/"
    )
    page=context.new_page()    
    page.goto("https://www.google.com/")
    
    
    
    page.set_default_timeout(5000)
    page.mouse.wheel(0, 400)
    time.sleep(1)
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Google")
    
    
    
    
    #Validar la url
    F.Validar_url("https://www.google.com/")  
    F.Texto("(//input[contains(@aria-label,'Buscar')])[1]","Ferra",1)  
    #solucion uno
    #F.Click("(//span[contains(.,'Ferrari')])[1]",2)
    #solucion dos 
    F.Click_primero("text=Ferrari",1)
   
    F.Esperar(5)
    
    #expect(page).to_have_url(re.compile(".*docs/intro"))
    
    
    context.close()
    browser.close()
    
    
    