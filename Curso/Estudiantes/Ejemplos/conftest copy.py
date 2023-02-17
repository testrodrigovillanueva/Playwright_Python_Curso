import re
import time
import random
import pytest
import sys
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales


tiempo=1.3
ruta="Imagenes/Upload/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"

@pytest.fixture(scope="function")
def set_up(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)  
    context = browser.new_context(
    viewport={ 'width': 1500, 'height': 800 }
    #record_video_dir="Videos/Checkbox/"
    )      
    #Inicia Trace Viewer 
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page=context.new_page()    
    page.goto("https://testingqarvn.com.es/upload-files/")    
    page.set_default_timeout(5000)     
    context.tracing.stop(path="trace.zip") 
    yield page    
    context.close()
    browser.close()
    