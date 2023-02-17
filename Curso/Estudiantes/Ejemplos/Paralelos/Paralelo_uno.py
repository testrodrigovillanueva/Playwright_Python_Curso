import re
import time
import random
import pytest
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#pytest Sesion2.py -s -v
#pytest Paralelo_uno.py -s -v --browser-channel=chrome -n 4
#v-17
#playwright codegen   https://www.saucedemo.com/

#Variables globales
tiempo=0.9
ruta="Imagenes/Upload/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"

def test_sesion1(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test uno")
    
    
   
def test_sesion2(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    #F.Validar_titulo_pagina("Swag Labs")
    
    F.Click("//button[contains(@id,'add-to-cart-sauce-labs-backpack')]",tiempo)
    F.Click("//button[contains(@id,'add-to-cart-sauce-labs-bike-light')]",tiempo)
    F.Esperar(2)
    print("Termina Test dos")
    

   
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
    F.Validar_titulo_pagina("Swag Labs")
    
def test_sesion5(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test cinco")
    
def test_sesion6(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test seis")
    
def test_sesion7(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test siete")
    
def test_sesion8(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test ocho")
    
def test_sesion9(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test nueve")
      
def test_sesion10(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test diez")
    
def test_sesion11(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test Once")
    
def test_sesion12(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test doce")
    
def test_sesion13(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test trece")

def test_sesion14(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test catorce")
  
def test_sesion15(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test quince")
    
def test_sesion15(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test quince")
    
def test_sesion15(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test quince")


    