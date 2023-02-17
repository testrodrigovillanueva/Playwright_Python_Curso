import re
import time
import random
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales


#Generate
#playwright codegen https://www.saucedemo.com/

tiempo=0.3
ruta="Imagenes/Upload/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"

def test_generate(playwright: Playwright) -> None:
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
    page.goto("https://www.saucedemo.com/")
    
    page.locator("[data-test='username']").click()
    # Fill [data-test="username"]
    page.locator("[data-test=\"username\"]").fill("standard_user")
    # Press Tab
    page.locator("[data-test=\"username\"]").press("Tab")
    # Fill [data-test="password"]
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    # Click [data-test="login-button"]
    page.locator("[data-test=\"login-button\"]").click()
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    # Click text=Open Menu
    page.locator("text=Open Menu").click()
    # Click text=Logout
    page.locator("text=Logout").click()
    page.wait_for_url("https://www.saucedemo.com/")
    # ---------------------
    context.close()
    browser.close()
