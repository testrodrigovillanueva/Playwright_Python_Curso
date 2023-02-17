import re
import time
import random
import pytest
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#pytest Sesion_comandos.py -s -v -k  sesion2       #correr un test especifico

#playwright codegen   https://www.saucedemo.com/

#Variables globales
tiempo=0.9
ruta="Imagenes/Upload/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"

def test_sesion1(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    
    
   
def test_sesion2(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    #F.Validar_titulo_pagina("Swag Labs")
    
    F.Click("//button[contains(@id,'add-to-cart-sauce-labs-backpack')]",tiempo)
    F.Click("//button[contains(@id,'add-to-cart-sauce-labs-bike-light')]",tiempo)
    F.Esperar(2)
    
   
def test_sesion3(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    #F.Validar_titulo_pagina("Swag Labs")
    
    F.Click("//button[contains(@id,'react-burger-menu-btn')]",tiempo)
    F.Click("//a[contains(@id,'link')][@class='bm-item menu-item'][contains(.,'Reset App State')]",tiempo)
    F.Click("//button[contains(@id,'react-burger-cross-btn')]",tiempo)
  
    F.Esperar(2)    
    
def test_sesion4(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    #F.Validar_titulo_pagina("Swag Labs")
    
    F.Click("//button[contains(@id,'remove-sauce-labs-backpack')]",tiempo)
    F.Click("//button[contains(@id,'remove-sauce-labs-bike-light')]",tiempo)
    F.Click("//button[contains(@id,'react-burger-menu-btn')]",tiempo)
    F.Click("//a[contains(@id,'link')][@class='bm-item menu-item'][contains(.,'Logout')]",tiempo)
  
    F.Esperar(2)    


    