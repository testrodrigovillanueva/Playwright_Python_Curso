import re
import time
import random
import pytest
from playwright.sync_api import Page, expect,Playwright, sync_playwright
from funciones import Funciones_Globales

#pytest Sesion3.py -s -v
#pytest Sesion2.py -s -v -n 5
#pytest Sesion3.py -s -v --browser-channel=chrome -n 4
#v-17
#playwright codegen   https://www.saucedemo.com/

#Variables globales
tiempo=0.9
ruta="Imagenes/Upload/"
pdf1="C:/Users/Usuario1/Documents/VIDEOS_UDEMY/PLAYWRIGHT/Curso/Practicas/Ejemplos/Pdf/Documento1.pdf"

"""
@pytest.mark.parametrize("numero,esperando", [("3+5", 8), 
                                            ("2+4", 6),
                                            ("9*5", 45),
                                            pytest.param("6*9", 42, marks=pytest.mark.xfail)])
def test_eval(numero, esperando):
    assert eval(numero) == esperando
""" 
    
@pytest.mark.parametrize("nom,ape",[("rodrigo,villanueva"),
                                    ("juan,Perez"),
                                    ("Erika,Paz"),])
def set_up(set_up,nom,ape)-> None:
    page=set_up     
    F=Funciones_Globales(page)
    F.Validar_titulo_pagina("Datos Personales | TestingQaRvn")
    
    F.Scroll_xy(0,600)
    F.Texto("//input[contains(@id,'wsf-1-field-21')]",nom,1)
    F.Texto("//input[contains(@id,'wsf-1-field-22')]",ape,1)
    F.Esperar(2)