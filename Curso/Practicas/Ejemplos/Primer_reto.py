import re
import time
import random
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#playwright codegen https://demoqa.com/automation-practice-form

tiempo=0.1
ruta="Imagenes/Reto/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"


def test_primer_Reto(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)
    #context=browser.new_context()    
    #context=browser.new_context(record_video_dir="Videos/Checkbox/")
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 700 }
      #record_video_dir="Videos/Checkbox/"
    )
    page=context.new_page()    
    page.goto("https://demoqa.com/automation-practice-form")
    
    
    
    page.set_default_timeout(5000)
    page.mouse.wheel(0, 400)
    time.sleep(1)
    F=Funciones_Globales(page)
    #expect(page).to_have_title("ComboBox | TestingQaRvn")
    F.Validar_titulo_pagina("ToolsQA")
    
    
    
    #Datos
    F.Texto_img("//*[@id='firstName']","Rodrigo",ruta+"nombre.png",tiempo)
    F.Texto_img("//*[@id='lastName']","Villanueva",ruta+"apellido.png",tiempo)
    F.Texto("//*[@id='userEmail']","rodrigo@gmail.com",tiempo)

    #Gender
    F.Click("//label[@for='gender-radio-1'][contains(.,'Male')]",tiempo)
    
    #Mobile
    F.Texto("//*[@id='userNumber']","5540786567",tiempo)
    
    #Fiesta 
    F.Click("//*[@id='dateOfBirthInput']",tiempo)
    F.Click("(//div[contains(.,'28')])[23]",tiempo)
    
    #Subjects
#     F.Click("//div[6]/div[2]/div[1]/div[1]/div[1]",2)
#     F.Texto("//div[6]/div[2]/div[1]/div[1]/div[1]","En",3)
#     F.Mouse_xy(0,30)

    page.locator(".subjects-auto-complete__value-container").click()
    page.locator("text=Subjects 0 results available. Use Up and Down to choose options, press Enter to  >> input[type=\"text\"]").fill("en")
    page.locator("#react-select-2-option-0").click()
    
    #Hobbie
    F.Click("//label[@for='hobbies-checkbox-1'][contains(.,'Sports')]",tiempo)
    
    #Archivo
    F.Upload_file("//input[contains(@id,'uploadPicture')]",pdf1,tiempo)
    
    #Dirección
    F.Texto("//*[@id='currentAddress']","Demo de la Dirección uno",tiempo)
    
    F.Scroll_xy(0,600,tiempo)
    
    #City 
    F.Doble_Click("//div[@class=' css-1wa3eu0-placeholder'][contains(.,'Select State')]",2)
    F.Mouse_xy(0,30,1)
    
    #Select city 
    F.Doble_Click("//div[@class=' css-1hwfws3'][contains(.,'Select City')]",2)
    F.Mouse_xy(0,20,1)
    
    #Enter
    
    #page.locator("//button[@type='submit'][contains(.,'Submit')]").click()
    F.Mouse_xy(200,0,2)
    F.Enter()
    F.Esperar(10)
    
   
    
    
    
    
   
    
    #Validar la url
    #expect(page).to_have_url(re.compile(".*datos-personales/"))   
    F.Validar_url("https://demoqa.com/automation-practice-form")    
   
    
    #expect(page).to_have_url(re.compile(".*docs/intro"))
    
    
    context.close()
    browser.close()
    
    
    