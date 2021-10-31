from pyttsx3 import engine
import serial
import speech_recognition as sr
import pyttsx3

#Comunicacion serial es un proceso de envio de datos de un bit a la vez
#Para convertir de voz en texto, la unica clase que se necesita es Recognizer
listener = sr.Recognizer()

#Objeto serial, verifica si tienes el mismo puerto("COM#") que en tu codigo de arduino 
dev = serial.Serial("COM3",9600)
name = "siri"

#Incialización para el asistente de voz
engine = pyttsx3.init()

#Configuracion del estilo de voz que tendra nuestro asistente
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#Esta funcion hara que nuestro asistente hable a partir del dato que recibe, en este caso "text"
def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
        
            print("Escuchando .... :)")

            voz = listener.listen(source)
            rec = listener.recognize_google(voz,language='es-ES')
            rec=rec.lower()

    except:
        pass
    return rec

def prendido():
    talk("prendiendo el led")
    dev.write("1".encode('ascii'))

def apagado():
    talk("apagando el led")
    dev.write("0".encode('ascii'))


def run():
    while True:
        rec=listen()
        if "siri" in rec:
            if "prende" in rec:
                prendido()                
            elif "apaga" in rec:
                apagado()

run()


#Links que pueden ayudar con la documetacion
#https://realpython.com/python-speech-recognition/#appendix-recognizing-speech-in-languages-other-than-english