import re
import time
import random
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#playwright codegen   https://www.saucedemo.com/

#Variables globales
tiempo=0.2
ruta="Imagenes/Upload/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"

def test_Generate(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)  
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 800 }
      #record_video_dir="Videos/Checkbox/"
    )
    
    #Inicia Trace Viewer 
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    
    page=context.new_page()    
    page.goto("https://www.saucedemo.com/")   
    
    page.set_default_timeout(5000)    
    
   
    numA2=random.sample(range(1,100000),6)
    numA3=random.sample(range(1,100000),6)
    
    #Creando nuestro Objeto de tipo Funciones Globales
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    #time.sleep(1)
    #page.mouse.wheel(0, 400)
    F.Scroll_xy(0,400)
    F.Esperar(tiempo)
    
    # Click [data-test="username"]
    F.Click("[data-test='username']",1)
    # Fill [data-test="username"]
    F.Texto("[data-test=\"username\"]","standard_user",3)
    # Click [data-test="password"]
    page.locator("[data-test=\"password\"]").click()
    # Fill [data-test="password"]
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    # Click [data-test="login-button"]
    page.locator("[data-test=\"login-button\"]").click()
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    # Click [data-test="add-to-cart-sauce-labs-backpack"]
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    # Click text=Open Menu
    page.locator("text=Open Menu").click()
    # Click text=Logout
    page.locator("text=Logout").click()
    page.wait_for_url("https://www.saucedemo.com/")
    
    context.close()
    browser.close()
    