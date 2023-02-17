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
#url="https://testingqarvn.com.es/datos-personales/"
#pytest Excel_1.py -s -v

ancho=1900
alto=800
scroll=800

@pytest.fixture(scope="function")
def set_up_excel(playwright: Playwright)-> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)  
    context = browser.new_context(
      viewport={ 'width': ancho, 'height': alto }
      #record_video_dir="Videos/Checkbox/"
    )    
    #Inicia Trace Viewer 
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page=context.new_page() 
    url="https://testingqarvn.com.es/datos-personales/"     
    page.goto(url)   
    page.set_default_timeout(5000) 

    yield page  
    #Cierre de Trace Viewer 
    context.tracing.stop(path="trace.zip")    
    context.close()
    browser.close()


@pytest.fixture(scope="function")    
def set_up(playwright: Playwright)-> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)     
    context = browser.new_context(
      viewport={ 'width': ancho, 'height': alto }
      #record_video_dir="Videos/Checkbox/"
    )    
    #Inicia Trace Viewer 
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page=context.new_page()  
    url="https://www.saucedemo.com/"   
    page.goto(url)   
    page.set_default_timeout(5000) 

    yield page  

    #Cierre de Trace Viewer 
    context.tracing.stop(path="trace.zip")     
   
    context.close()
    browser.close()
 