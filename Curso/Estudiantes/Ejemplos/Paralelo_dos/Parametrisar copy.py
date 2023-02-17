import re
import time
import random
import pytest 
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#pytest Parametrisar.py 
#pytest Paralelo_uno.py -s -v --browser-channel=chrome
#v-17
#playwright codegen   https://www.saucedemo.com/
#https://docs.pytest.org/en/7.2.x/how-to/parametrize.html
#https://docs.pytest.org/en/7.2.x/example/parametrize.html#paramexamples

#https://www.saucedemo.com/

#Variables globales
tiempo=0.5
ruta="Imagenes/Upload/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"


 
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
    

data= [("rodrigo","villanueva","rod@gmail.com"),
      ("juan","Perez","juan@gmail.com"),
      ("erika","paz","erika@gmail.com"),]
@pytest.mark.parametrize("nom,ape,email",data)  
# @pytest.mark.parametrize("nom,ape,email",
#                          [("rodrigo","villanueva","rod@gmail.com"),
#                          ("juan","Perez","juan@gmail.com"),
#                          ("erika","paz","erika@gmail.com")])
def test_sesion1(set_up_vnr,nom,ape,email)-> None:
    page=set_up_vnr     
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Datos Personales | TestingQaRvn")
    
    F.Scroll_xy(0,600)
    F.Texto("//input[contains(@id,'wsf-1-field-21')]",nom)
    F.Texto("//input[contains(@id,'wsf-1-field-22')]",ape)
    F.Texto("//input[contains(@id,'wsf-1-field-23')]",email)
    F.Esperar(2)
    

@pytest.mark.parametrize("us,pa",
                         [("standard_user","secret_sauce"),
                         ("problem_user","secret_sauce"),
                         ("erika","paz"),
                         ("rodrigo","villanueva")])
def test_sesion2(set_up_sauce,us,pa)-> None:
    page=set_up_sauce    
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Swag Labs")
    print("Validando test")
    
    F.Scroll_xy(0,600)
    #F.Esperar(tiempo)  
    
    F.Click("[data-test='username']",tiempo)   
    F.Texto("[data-test=\"username\"]",us,tiempo)   
    F.Click("[data-test=\"password\"]",tiempo)
    F.Texto("[data-test=\"password\"]",pa,tiempo)
    F.Click("[data-test=\"login-button\"]")

    
   
    
