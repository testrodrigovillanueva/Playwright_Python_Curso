import re
import time
import random
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#playwright codegen   https://www.saucedemo.com/

#Variables globales
tiempo=0.9
ruta="Imagenes/Upload/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"

def test_s1(set_up) -> None:
    page=set_up
 
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
   
    
def test_s2(set_up) -> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")       
  
   
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    # Click [data-test="add-to-cart-sauce-labs-backpack"]
    F.Click("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
    F.Click("text=Open Menu")
   
    
    
def test_s3(set_up) -> None:
    page=set_up
    #Creando nuestro Objeto de tipo Funciones Globales
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    
  
   
    page.wait_for_url("https://www.saucedemo.com/inventory.html")      
    F.Click("text=Logout")
    page.wait_for_url("https://www.saucedemo.com/")
    
    
    