# importa el listado de notas de la rasberry, es un archivo de python que define las freciencias de cada nota
from notas import *    #  <<<---Este archivo debe estar guardado en la memoria de la raspberry

from machine import Pin, PWM
from utime import sleep

#definición del pin donde se conecta el buzzer
buzzer = PWM(Pin(15))

# este es el tiempo de la canción, con él se puede hacer mas lento o rápido la canción
tempo = 200

# array con la canción , el primer elemento es la nota y el segundo es el tiempo de espera de cada nota
# esto tiene una profundidad musical que yo no quiero investigar, pero
# sé que los negativos duran menos que una nota normal <---cosas raras de musica, si alguien sabe, me explica <---gracias!
MarioBros = [
    "NOTE_E5",8, "NOTE_E5",8, "REST",8, "NOTE_E5",8, "REST",8, "NOTE_C5",8, "NOTE_E5",8, 
"NOTE_G5",4, "REST",4, "NOTE_G4",8, "REST",4, 
"NOTE_C5",-4, "NOTE_G4",8, "REST",4, "NOTE_E4",-4, 
"NOTE_A4",4, "NOTE_B4",4, "NOTE_AS4",8, "NOTE_A4",4,
"NOTE_G4",-8, "NOTE_E5",-8, "NOTE_G5",-8, "NOTE_A5",4, "NOTE_F5",8, "NOTE_G5",8,
"REST",8, "NOTE_E5",4,"NOTE_C5",8, "NOTE_D5",8, "NOTE_B4",-4,
"NOTE_C5",-4, "NOTE_G4",8, "REST",4, "NOTE_E4",-4, 
"NOTE_A4",4, "NOTE_B4",4, "NOTE_AS4",8, "NOTE_A4",4,
"NOTE_G4",-8, "NOTE_E5",-8, "NOTE_G5",-8, "NOTE_A5",4, "NOTE_F5",8, "NOTE_G5",8,
"REST",8, "NOTE_E5",4,"NOTE_C5",8, "NOTE_D5",8, "NOTE_B4",-4,

"REST",4, "NOTE_G5",8, "NOTE_FS5",8, "NOTE_F5",8, "NOTE_DS5",4, "NOTE_E5",8,
"REST",8, "NOTE_GS4",8, "NOTE_A4",8, "NOTE_C4",8, "REST",8, "NOTE_A4",8, "NOTE_C5",8, "NOTE_D5",8,
"REST",4, "NOTE_DS5",4, "REST",8, "NOTE_D5",-4,
"NOTE_C5",2, "REST",2,

"REST",4, "NOTE_G5",8, "NOTE_FS5",8, "NOTE_F5",8, "NOTE_DS5",4, "NOTE_E5",8,
"REST",8, "NOTE_GS4",8, "NOTE_A4",8, "NOTE_C4",8, "REST",8, "NOTE_A4",8, "NOTE_C5",8, "NOTE_D5",8,
"REST",4, "NOTE_DS5",4, "REST",8, "NOTE_D5",-4,
"NOTE_C5",2, "REST",2,

"NOTE_C5",8, "NOTE_C5",4, "NOTE_C5",8, "REST",8, "NOTE_C5",8, "NOTE_D5",4,
"NOTE_E5",8, "NOTE_C5",4, "NOTE_A4",8, "NOTE_G4",2,

"NOTE_C5",8, "NOTE_C5",4, "NOTE_C5",8, "REST",8, "NOTE_C5",8, "NOTE_D5",8, "NOTE_E5",8,
"REST",1, 
"NOTE_C5",8, "NOTE_C5",4, "NOTE_C5",8, "REST",8, "NOTE_C5",8, "NOTE_D5",4,
"NOTE_E5",8, "NOTE_C5",4, "NOTE_A4",8, "NOTE_G4",2,
"NOTE_E5",8, "NOTE_E5",8, "REST",8, "NOTE_E5",8, "REST",8, "NOTE_C5",8, "NOTE_E5",4,
"NOTE_G5",4, "REST",4, "NOTE_G4",4, "REST",4, 
"NOTE_C5",-4, "NOTE_G4",8, "REST",4, "NOTE_E4",-4,

"NOTE_A4",4, "NOTE_B4",4, "NOTE_AS4",8, "NOTE_A4",4,
"NOTE_G4",-8, "NOTE_E5",-8, "NOTE_G5",-8, "NOTE_A5",4, "NOTE_F5",8, "NOTE_G5",8,
"REST",8, "NOTE_E5",4,"NOTE_C5",8, "NOTE_D5",8, "NOTE_B4",-4,

"NOTE_C5",-4, "NOTE_G4",8, "REST",4, "NOTE_E4",-4, 
"NOTE_A4",4, "NOTE_B4",4, "NOTE_AS4",8, "NOTE_A4",4,
"NOTE_G4",-8, "NOTE_E5",-8, "NOTE_G5",-8, "NOTE_A5",4, "NOTE_F5",8, "NOTE_G5",8,
"REST",8, "NOTE_E5",4,"NOTE_C5",8, "NOTE_D5",8, "NOTE_B4",-4,

"NOTE_E5",8, "NOTE_C5",4, "NOTE_G4",8, "REST",4, "NOTE_GS4",4,
"NOTE_A4",8, "NOTE_F5",4, "NOTE_F5",8, "NOTE_A4",2,
"NOTE_D5",-8, "NOTE_A5",-8, "NOTE_A5",-8, "NOTE_A5",-8, "NOTE_G5",-8, "NOTE_F5",-8,

"NOTE_E5",8, "NOTE_C5",4, "NOTE_A4",8, "NOTE_G4",2, 
"NOTE_E5",8, "NOTE_C5",4, "NOTE_G4",8, "REST",4, "NOTE_GS4",4,
"NOTE_A4",8, "NOTE_F5",4, "NOTE_F5",8, "NOTE_A4",2,
"NOTE_B4",8, "NOTE_F5",4, "NOTE_F5",8, "NOTE_F5",-8, "NOTE_E5",-8, "NOTE_D5",-8,
"NOTE_C5",8, "NOTE_E4",4, "NOTE_E4",8, "NOTE_C4",2,

"NOTE_C5",8, "NOTE_C5",4, "NOTE_C5",8, "REST",8, "NOTE_C5",8, "NOTE_D5",8, "NOTE_E5",8,
"REST",1,

"NOTE_C5",8, "NOTE_C5",4, "NOTE_C5",8, "REST",8, "NOTE_C5",8, "NOTE_D5",4, 
"NOTE_E5",8, "NOTE_C5",4, "NOTE_A4",8, "NOTE_G4",2,
"NOTE_E5",8, "NOTE_E5",8, "REST",8, "NOTE_E5",8, "REST",8, "NOTE_C5",8, "NOTE_E5",4,
"NOTE_G5",4, "REST",4, "NOTE_G4",4, "REST",4, 
"NOTE_E5",8, "NOTE_C5",4, "NOTE_G4",8, "REST",4, "NOTE_GS4",4,
"NOTE_A4",8, "NOTE_F5",4, "NOTE_F5",8, "NOTE_A4",2,
"NOTE_D5",-8, "NOTE_A5",-8, "NOTE_A5",-8, "NOTE_A5",-8, "NOTE_G5",-8, "NOTE_F5",-8,

"NOTE_E5",8, "NOTE_C5",4, "NOTE_A4",8, "NOTE_G4",2, 
"NOTE_E5",8, "NOTE_C5",4, "NOTE_G4",8, "REST",4, "NOTE_GS4",4,
"NOTE_A4",8, "NOTE_F5",4, "NOTE_F5",8, "NOTE_A4",2,
"NOTE_B4",8, "NOTE_F5",4, "NOTE_F5",8, "NOTE_F5",-8, "NOTE_E5",-8, "NOTE_D5",-8,
"NOTE_C5",8, "NOTE_E4",4, "NOTE_E4",8, "NOTE_C4",2,

#//game over sound
"NOTE_C5",-4, "NOTE_G4",-4, "NOTE_E4",4, 
"NOTE_A4",-8, "NOTE_B4",-8, "NOTE_A4",-8, "NOTE_GS4",-8, "NOTE_AS4",-8, "NOTE_GS4",-8,
"NOTE_G4",8, "NOTE_D4",8, "NOTE_E4",-2,

    ]

def playtone(frequency):
    """ define la frecuencia de trabajo del pin PWM
        recibe el valor de frecuencia a la que suena cada tono 
    """ 
    buzzer.duty_u16(10000)
    buzzer.freq(frequency)
    
def bequiet():
    """funcion que define la frecuencia en cero, es decir, para la señal PWM"""
    buzzer.duty_u16(0)

def playsong(mysong):
    """función para reproducir la canción
        recibe la lista que es definida por una nota y su duración
        reproduce la canción en cada instante
    """

    wholenote = (60000 * 4) / tempo  
    for i in list(range(0,len(mysong),2)): #recorre el listado de la canción
        
        #primer if define la nota que se debe reproducir
        if mysong[i] == "REST":  # rest es para deterner la reproducción de sonido
            bequiet()
        else:                    
            playtone(tones[mysong[i]])
        
        #segundo if define el tiempo que debe durar la nota 
        if mysong[i+1] > 0:
            sleep(wholenote / (abs(mysong[i+1])*1000))
        else:
            sleep((wholenote / (abs(mysong[i+1])*1000))*1.5)
            
    bequiet() 
        
if __name__ == "__main__":  #entry point
    
    playsong(MarioBros)