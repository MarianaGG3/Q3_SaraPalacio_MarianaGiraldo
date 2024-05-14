import cv2
import pydicom
import matplotlib.pyplot as plt
import os
from pydicom import dcmread
import nibabel as nib
import numpy as np
from clases import *


p=Paciente()
c=Cargar()

#def main():
while True:
    menu=int(input("""
    1. Ingresar paciente
    2. Ingresar imagenes
    3. Hacer transformacion geometrica
    4. Manipulacion de imagenes
    5. Salir:  """))


    if menu==1:
         if menu == 1:
            archivo = input("Ingrese nombre de la carpeta con archivos DICOM: ")
            c.cargar_paciente(archivo, dicc_pacientes, dicc_archivos)
            print("Pacientes cargados:")
            print(dicc_pacientes)

    elif menu == 2:
        archivo = input('Ingrese nombre del archivo de la imagen: ')
        key = input('crear clave de la imagen: ')
        ima = cv2.imread(archivo)
        dicc_archivos[key] = ima
        print(dicc_archivos)
    elif menu == 3:

        key = input('Ingrese la clave de la imagen DICOM que desea rotar: ')
        grados = input('Ingrese el valor de rotación de la imagen (90, 180, 270): ')
        p.rotar_imagen(key, grados)

    elif menu == 4:
        key = input('ingrese la clave de la imagen que desea modificar: ')
        umb = input('Ingrese el numero de umbral que tendra la imagen: ')
        kernel = input('Ingrese el numero del kernel que tendra la imagen: ')
        p.procesar_imagen(key, umb, kernel)
    elif menu == 5:
        break