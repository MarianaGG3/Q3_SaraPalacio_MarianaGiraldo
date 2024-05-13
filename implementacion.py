import cv2
import pydicom
import matplotlib.pyplot as plt
import os
from pydicom.data import get_testdata_file
from pydicom import dcmread
import nibabel as nib
import numpy as np
from clases import *
dicc_archivos={}
dicc_pacientes={}
p=Paciente
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
            #arch_dicom=[]
            print(os.listdir(archivo))
            if n.endswith('.dcm'):  
                lectura = os.path.join(archivo, n)
                dcm = pydicom.dcmread(lectura)
                #arch_dicom.append(dcm)
                im = dcm.pixel_array
                imagen_nifti = nib.Nifti1Image(im, np.eye(4))
                nombre_nifti = os.path.splitext(n)[0] + ".nii.gz"
                nib.save(imagen_nifti, nombre_nifti)

                nombre = input("Ingrese el nombre: ")
                id = int(input("Ingrese la cedula: "))
                edad= int(input("ingrese la edad"))

                dicc_archivos[id]=[nombre,edad] 

                # plt.imshow(im)
                # plt.show()

        elif menu==2:
            pass
        elif menu==3:
            pass
        elif menu==4:
            pass
        elif menu==5:
            break


