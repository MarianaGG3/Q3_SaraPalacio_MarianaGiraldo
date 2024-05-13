import cv2
import pydicom
import matplotlib.pyplot as plt
import os
from pydicom.data import get_testdata_file
from pydicom import dcmread

def main():
    while True:
        menu=int(input("""
        1. Ingresar paciente
        2. Ingresar imagenes
        3. Hacer transformacion geometrica
        4. Manipulacion de imagenes
        5. Salir"""))


        if menu==1:
            pass
        elif menu==2:
            pass
        elif menu==3:
            pass
        elif menu==4:
            pass
        elif menu==5:
            break


