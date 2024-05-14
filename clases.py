import cv2
import pydicom
import matplotlib.pyplot as plt
import os
from pydicom import dcmread
import nibabel as nib
import numpy as np
dicc_archivos={}
dicc_pacientes={}

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

    def rotar_imagen(self, key, grados):
        if key in dicc_archivos:
            dcm = dicc_archivos[key]
            img = dcm.pixel_array
            img_rotada = np.rot90(img, int(grados) // 90)
            
            fig, axs = plt.subplots(1, 2, figsize=(10, 5))
            axs[0].imshow(img, cmap='gray')
            axs[0].set_title('Imagen Original')
            axs[0].axis('off')
            axs[1].imshow(img_rotada, cmap='gray')
            axs[1].set_title(f'Imagen Rotada {grados}°')
            axs[1].axis('off')
            plt.show()

            nombre_rotada = f"{key}_rotada_{grados}.png"
            cv2.imwrite(nombre_rotada, img_rotada)
            dicc_archivos[nombre_rotada] = img_rotada
            print(f"Imagen rotada guardada como: {nombre_rotada}")
        else:
            print("Clave de imagen no encontrada en los archivos DICOM.")

    def rotar_imagen(self, key, grados):
        if key in dicc_archivos:
            dcm = dicc_archivos[key]
            img = dcm.pixel_array
            img_rotada = np.rot90(img, int(grados) // 90)
            
            fig, axs = plt.subplots(1, 2, figsize=(10, 5))
            axs[0].imshow(img, cmap='gray')
            axs[0].set_title('Imagen Original')
            axs[0].axis('off')
            axs[1].imshow(img_rotada, cmap='gray')
            axs[1].set_title(f'Imagen Rotada {grados}°')
            axs[1].axis('off')
            plt.show()

            nombre_rotada = f"{key}rotada{grados}.png"
            cv2.imwrite(nombre_rotada, img_rotada)
            dicc_archivos[nombre_rotada] = img_rotada
            print(f"Imagen rotada guardada como: {nombre_rotada}")
        else:
            print("Clave de imagen no encontrada en los archivos DICOM.")

    def procesar_imagen(self, key, umb, kernel_tam):
        img = dicc_archivos[key].copy()
        _, binarizada = cv2.threshold(img, int(umb), 255, cv2.THRESH_BINARY)
        kernel = np.ones((int(kernel_tam), int(kernel_tam)), np.uint8)
        morfologia = cv2.morphologyEx(binarizada, cv2.MORPH_OPEN, kernel)
        texto = f"Imagen binarizada, Umbral: {umb}, Tamaño de kernel: {kernel_tam}"
        color = (255, 255, 255)  # Color blanco
        grosor = 2
        altura, anchura = morfologia.shape[:2]
        (ancho_texto, alto_texto), _ = cv2.getTextSize(texto, cv2.FONT_HERSHEY_SIMPLEX, 1, grosor)
        x = (anchura - ancho_texto) // 2
        y = altura - alto_texto - 10
        cv2.putText(morfologia, texto, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, color, grosor, cv2.LINE_AA)
        cv2.imshow("Imagen procesada", morfologia)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite("imagen_procesada.png", morfologia)

class Cargar:
    def cargar_paciente(self, archivo, dicc_pacientes, dicc_archivos):
        for n in os.listdir(archivo):
            if n.endswith('.dcm'):
                lectura = os.path.join(archivo, n)
                dcm = pydicom.dcmread(lectura)
                
                paciente = Paciente()
                paciente.asignarNombre(dcm.PatientName)
                paciente.asignarEdad(dcm.PatientAge)
                paciente.asignarId(dcm.PatientID)
                paciente.asignarImagen(lectura)

                dicc_pacientes[str(dcm.PatientID)] = {
                    "Nombre": paciente.verNombre(),
                    "Edad": paciente.verEdad(),
                    "Imagen": paciente.verImagen()
                }
                
                dicc_archivos[str(dcm.PatientID)] = dcm  
                
                im = dcm.pixel_array
                imagen_nifti = nib.Nifti1Image(im, np.eye(4))
                nombre_nifti = os.path.splitext(n)[0] + ".nii.gz"
                nib.save(imagen_nifti, nombre_nifti)
                dicc_archivos[nombre_nifti] = imagen_nifti




                
                

    