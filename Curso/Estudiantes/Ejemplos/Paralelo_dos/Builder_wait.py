import re
import time
import random
import pytest
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#pytest Sesion2.py -s -v
#pytest Paralelo_uno.py -s -v --browser-channel=chrome
#v-17
#playwright codegen   https://www.saucedemo.com/

#Variables globales
tiempo=0.9
ruta="Imagenes/Upload/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"

"""
def test_sesion1(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Termina Test uno")
    
    
    # #espera de un selector 
    # page.wait_for_selector("//div[contains(@class,'app_logo')]")
    # print("Encontro el logo de la Página")
    # #click Agregra al carrito
    # F.Click("//button[contains(@id,'add-to-cart-sauce-labs-backpack')]",2)
    
    #segunda prueba 
    # if page.wait_for_selector("//div[contains(@class,'app_logo')]"):
    #     print("Logo encontrado")
    #     #click Agregra al carrito
    #     F.Click("//button[contains(@id,'add-to-cart-sauce-labs-backpack')]",2)
    
    #Tercera prueba 
    if page.is_visible("//div[contains(@class,'app_logo')]"):
        print("Logo encontrado tercera vez")
        #click Agregra al carrito
        F.Click("//button[contains(@id,'add-to-cart-sauce-labs-backpack')]",2)
"""
    

def test_sesion2(set_up)-> None:
    page=set_up
    
    F=Funciones_Globales(page)
    #F.Validar_titulo_pagina("Swag Labs")
    
    #intentos con while 
    bandera=True
    intentos=0
    #apretando el boton de Agregar
    F.Click("//button[contains(@id,'add-to-cart-sauce-labs-backpack')]")
    
    while bandera:
        if not page.is_visible("//button[contains(@id,'add-to-cart-sauce-labs-backpack')]"):
            intentos += 1
            print(f"Esperando el Boton de Agregar: {intentos}")
            F.Esperar(0.5)
            if intentos==4:
                F.Click("//button[contains(@id,'remove-sauce-labs-backpack')]") 
                print("Se presiona el Boton remover ya que no encontro el de Agregar")               
                bandera=False
           
   
    F.Click("//button[contains(@id,'add-to-cart-sauce-labs-bike-light')]",tiempo)
    F.Esperar(2)
    print("Termina Test dos")
 

