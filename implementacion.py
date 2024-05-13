import cv2
import pydicom
import matplotlib.pyplot as plt
import os
from pydicom.data import get_testdata_file
from pydicom import dcmread
import nibabel as nib
import numpy as np
import clases 
dicc_archivos={}
dicc_pacientes={}

def main():
    while True:
        menu=int(input("""
        1. Ingresar paciente
        2. Ingresar imagenes
        3. Hacer transformacion geometrica
        4. Manipulacion de imagenes
        5. Salir"""))


        if menu==1:
            archivo=input("ingrese nombre de la carpeta con archivos dicom")
            key=input('crear clave asociada al paciente:')
            cargar_paciente(archivo)
            p=paciente()
            dicc_pacientes[key]=p 
            dicc_archivos[key]=nombre_nifti
           

                # plt.imshow(im)
                # plt.show()

        elif menu==2:
            archivo= input('Ingrese nombre del archivo de la imagen')
            key=input('crear clave de la imagen: ')
            ima=cv2.imread(archivo)
            dicc_archivos[key]=ima
        elif menu==3:
            key=input('ingrese la clave de la imagen que desea rotar: ')
            grados=input('elige a que grados deseas rotar la imagen.\n 1. 90° \n 2. 180° \n 3. 270°')
            rotar_imagen(key, grados)
        elif menu==4:
            key=input('ingrese la clave de la imagen que desea rotar: ')
            umb= input('Ingrese el numero de umbral que tendra la imagen: ')
            kernel=input('Ingrese el numero del kernel que tendra la imagen: ')
            procesar_imagen(key, umb,kernel)
        elif menu==5:
            break
menu()



