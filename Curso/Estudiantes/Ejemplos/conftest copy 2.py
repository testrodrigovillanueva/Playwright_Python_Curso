import re
import time
import random
import pytest
import sys
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

tiempo=0.5
ruta="Imagenes/Upload/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"
url="https://www.saucedemo.com/"

# @pytest.fixture(scope="function")
# def set_up(playwright: Playwright)-> None:
#     browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)  
#     context = browser.new_context(
#       viewport={ 'width': 1500, 'height': 800 }
#       #record_video_dir="Videos/Checkbox/"
#     )    
#     #Inicia Trace Viewer 
#     context.tracing.start(screenshots=True, snapshots=True, sources=True)
#     page=context.new_page()    
#     page.goto(url)   
#     page.set_default_timeout(5000) 

#     yield page  

#     #Cierre de Trace Viewer 
#     context.tracing.stop(path="trace.zip")     
   
#     context.close()
#     browser.close()
    
@pytest.fixture(scope="session")
def set_up(playwright: Playwright)-> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)  
    context = browser.new_context(
      viewport={ 'width': 1500, 'height': 800 }
      #record_video_dir="Videos/Checkbox/"
    )    
    #Inicia Trace Viewer 
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page=context.new_page()    
    page.goto(url)   
    page.set_default_timeout(5000) 
    
    F=Funciones_Globales(page)    
    F.Validar_titulo_pagina("Swag Labs")
    #time.sleep(1)
    #page.mouse.wheel(0, 400)
    F.Scroll_xy(0,400)
    F.Esperar(tiempo)  
    
    F.Click("[data-test='username']",tiempo)   
    F.Texto("[data-test=\"username\"]","standard_user",tiempo)   
    F.Click("[data-test=\"password\"]",tiempo)
    F.Texto("[data-test=\"password\"]","secret_sauce",tiempo)
    F.Click("[data-test=\"login-button\"]")

    yield page

    #Cierre de Trace Viewer 
    context.tracing.stop(path="trace.zip")     
   
    context.close()
    browser.close()
    
    
    