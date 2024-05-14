import cv2
import pydicom
import matplotlib.pyplot as plt
import os
from pydicom.data import get_testdata_file
from pydicom import dcmread
import nibabel as nib
import numpy as np


class Paciente:
    def __init__(self):
    
        self.__nombre = ""
        self.__ID = int
        self.__edad = int
        self.__imagen = ""
        
    def verNombre(self):
        return self.__nombre
    def verImagen(self):
        return self.__imagen
    def verEdad(self):
        return self.__edad
    def verId(self):
        return self.__id
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarImagen(self,s):
        self.__imagen = s
    def asignarEdad(self,g):
        self.__edad = g
    def asignarId(self,c):
        self.__id = c

    def cargar_paciente(self, archivo):
        if archivo.endswith('.dcm'):  
                lectura = os.path.join(archivo, n)
                dcm = pydicom.dcmread(lectura)
                
                nombre=dcm.PatientName
                edad= dcm.PatientAge
                ID=dcm.PatientID

                im = dcm.pixel_array
                imagen_nifti = nib.Nifti1Image(im, np.eye(4))
                nombre_nifti = os.path.splitext(n)[0] + ".nii.gz"
                nib.save(imagen_nifti, nombre_nifti)
                

    def rotar_imagen(key, grados):
        img= dicc_archivos[key] 
    def procesar_imagen(key,umb,kernel_tam):
        img= dicc_archivos[key] 
        binarizada = cv2.threshold(img, umb, 255, cv2.THRESH_BINARY)
        kernel = np.ones((kernel_tam, kernel_tam), np.uint8)
        morfologia = cv2.morphologyEx(binarizada, cv2.MORPH_OPEN, kernel)
