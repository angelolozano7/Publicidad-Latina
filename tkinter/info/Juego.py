import random

# ============================================
# OPERACIONES PARA MODO TEXTO
# ============================================

##def auxiliar1(dato):
##    """
##    """
##    global c1,c2,c3,c4,c5,c6,c7,c8
##    if(dato == 1):
##        return c1
##    elif(dato == 2):
##        return c2
##    elif(dato == 3):
##        return c3
##    elif(dato == 4):
##        return c4
##    elif(dato == 5):
##        return c5
##    elif(dato == 6):
##        return c6
##    elif(dato == 7):
##        return c7
##    elif(dato == 8):
##        return c8
##
##def auxiliar2(dato):
##    """
##    """
##    global e1,e2,e3,e4,e5,e6,e7,e8
##    if(dato == 1):
##        e1 = 1
##    elif(dato == 2):
##        e2 = 1
##    elif(dato == 3):
##        e3 = 1
##    elif(dato == 4):
##        e4 = 1
##    elif(dato == 5):
##        e5 = 1
##    elif(dato == 6):
##        e6 = 1
##    elif(dato == 7):
##        e7 = 1
##    elif(dato == 8):
##        e8 = 1
##
##
##def escogerCarta():
##    """
##    """
##    dato1 = eval(input("Escoja la primera carta: "))
##    dato2 = eval(input("Escoja la segunda carta: "))
##    carta1 = auxiliar1(dato1)
##    carta2 = auxiliar1(dato2)
##
##    if(carta1 == carta2):
##        auxiliar2(dato1)
##        auxiliar2(dato2)
##
##def printJuego():
##    """
##    """
##    global c1,c2,c3,c4,c5,c6,c7,c8,e1,e2,e3,e4,e5,e6,e7,e8
##
##    print("JUEGO MEMORIA")
##    print("=============")
##    print("")
##    cadena = ""
##    if(e1 == 0):
##        cadena = cadena + "[ ] "
##    else:
##        cadena = cadena + " " + c1 + "  "
##    if(e2 == 0):
##        cadena = cadena + "[ ] "
##    else:
##        cadena = cadena + " " + c2 + "  "
##    if(e3 == 0):
##        cadena = cadena + "[ ] "
##    else:
##        cadena = cadena + " " + c3 + "  "
##    if(e4 == 0):
##        cadena = cadena + "[ ] "
##    else:
##        cadena = cadena + " " + c4 + "  "
##    print(cadena)
##    cadena = ""
##    if(e5 == 0):
##        cadena = cadena + "[ ] "
##    else:
##        cadena = cadena + " " + c5 + "  "
##    if(e6 == 0):
##        cadena = cadena + "[ ] "
##    else:
##        cadena = cadena + " " + c6 + "  "
##    if(e7 == 0):
##        cadena = cadena + "[ ] "
##    else:
##        cadena = cadena + " " + c7 + "  "
##    if(e8 == 0):
##        cadena = cadena + "[ ] "
##    else:
##        cadena = cadena + " " + c8 + "  "
##    print(cadena)
##    print("")

# ============================================
# OPERACIONES PARA MODO GRAFICO (CON TKINTER)
# ============================================

import tkinter
import time

presion1=0
presion2=0
contador=0
verificando=False
parejas=0

botonSeleccionado = ""
cartaSeleccionada = ""

def escogerCarta():
    """
    """
    global contador,presion1,presion2,parejas,verificando

    while verificando==False:
        if parejas==4:
            print("Felicidades ganó")
            verificando==True
    algo()

def boton1():
    global c1,presion2,presion1,contador,carta1,botonSeleccionado,cartaSeleccionada
    contador=contador+1
    if(c1 == "J"):
        print(c1)
        photo=tkinter.PhotoImage(file="J.gif")
    elif(c1 == "Q"):
        photo=tkinter.PhotoImage(file="Q.gif")
    elif(c1 == "K"):
        photo=tkinter.PhotoImage(file="K.gif")
    elif(c1 == "A"):
        photo=tkinter.PhotoImage(file="As.gif")
    carta1.config(image=photo,width="150",height="223")
    carta1.photo = photo
    evaluar1()
    if(botonSeleccionado == ""):
        botonSeleccionado = carta1
        cartaSeleccionada = c1
    else:
        if(c1 != cartaSeleccionada):
            time.sleep(1)
            photo=tkinter.PhotoImage(file="reverso.gif")
            carta1.config(image=photo,width="150",height="223")
            carta1.photo = photo
            botonSeleccionado.config(image=photo,width="150",height="223")
            botonSeleccionado.photo = photo
        botonSeleccionado = ""
        cartaSeleccionada = ""


def boton2():
    global c2,presion2,presion1,contador,carta2,botonSeleccionado,cartaSeleccionada
    contador=contador+1
    print(presion1)
    print(presion2)
    if(c2 == "J"):
        print(c1)
        photo=tkinter.PhotoImage(file="J.gif")
    elif(c2 == "Q"):
        photo=tkinter.PhotoImage(file="Q.gif")
    elif(c2 == "K"):
        photo=tkinter.PhotoImage(file="K.gif")
    elif(c2 == "A"):
        photo=tkinter.PhotoImage(file="As.gif")
    carta2.config(image=photo,width="150",height="223")
    carta2.photo = photo
    evaluar2()
    if(botonSeleccionado == ""):
        botonSeleccionado = carta2
        cartaSeleccionada = c2
    else:
        if(c2 != cartaSeleccionada):
            time.sleep(10)
            photo=tkinter.PhotoImage(file="reverso.gif")
            carta2.config(image=photo,width="150",height="223")
            carta2.photo = photo
            botonSeleccionado.config(image=photo,width="150",height="223")
            botonSeleccionado.photo = photo
        botonSeleccionado = ""
        cartaSeleccionada = ""

def boton3():
    global c3,presion2,presion1,contador,carta3,botonSeleccionado,cartaSeleccionada
    contador=contador+1
    print(presion1)
    print(presion2)
    if(c3 == "J"):
        print(c1)
        photo=tkinter.PhotoImage(file="J.gif")
    elif(c3 == "Q"):
        photo=tkinter.PhotoImage(file="Q.gif")
    elif(c3 == "K"):
        photo=tkinter.PhotoImage(file="K.gif")
    elif(c3 == "A"):
        photo=tkinter.PhotoImage(file="As.gif")
    carta3.config(image=photo,width="150",height="223")
    carta3.photo = photo
    evaluar3()
    if(botonSeleccionado == ""):
        botonSeleccionado = carta3
        cartaSeleccionada = c3
    else:
        if(c3 != cartaSeleccionada):
            photo=tkinter.PhotoImage(file="reverso.gif")
            carta3.config(image=photo,width="150",height="223")
            carta3.photo = photo
            botonSeleccionado.config(image=photo,width="150",height="223")
            botonSeleccionado.photo = photo
        botonSeleccionado = ""
        cartaSeleccionada = ""

def boton4():
    global c4,presion2,presion1,contador,carta4,botonSeleccionado,cartaSeleccionada
    contador=contador+1
    print(presion1)
    print(presion2)
    if(c4 == "J"):
        print(c1)
        photo=tkinter.PhotoImage(file="J.gif")
    elif(c4 == "Q"):
        photo=tkinter.PhotoImage(file="Q.gif")
    elif(c4 == "K"):
        photo=tkinter.PhotoImage(file="K.gif")
    elif(c4 == "A"):
        photo=tkinter.PhotoImage(file="As.gif")
    carta4.config(image=photo,width="150",height="223")
    carta4.photo = photo
    evaluar4()
    if(botonSeleccionado == ""):
        botonSeleccionado = carta4
        cartaSeleccionada = c4
    else:
        if(c4 != cartaSeleccionada):
            photo=tkinter.PhotoImage(file="reverso.gif")
            carta4.config(image=photo,width="150",height="223")
            carta4.photo = photo
            botonSeleccionado.config(image=photo,width="150",height="223")
            botonSeleccionado.photo = photo
        botonSeleccionado = ""
        cartaSeleccionada = ""

def boton5():
    global c5,presion2,presion1,contador,carta5,botonSeleccionado,cartaSeleccionada
    contador=contador+1
    if(c5 == "J"):
        print(c1)
        photo=tkinter.PhotoImage(file="J.gif")
    elif(c5 == "Q"):
        photo=tkinter.PhotoImage(file="Q.gif")
    elif(c5 == "K"):
        photo=tkinter.PhotoImage(file="K.gif")
    elif(c5 == "A"):
        photo=tkinter.PhotoImage(file="As.gif")
    carta5.config(image=photo,width="150",height="223")
    carta5.photo = photo
    evaluar5()
    if(botonSeleccionado == ""):
        botonSeleccionado = carta5
        cartaSeleccionada = c5
    else:
        if(c5 != cartaSeleccionada):
            photo=tkinter.PhotoImage(file="reverso.gif")
            carta5.config(image=photo,width="150",height="223")
            carta5.photo = photo
            botonSeleccionado.config(image=photo,width="150",height="223")
            botonSeleccionado.photo = photo
        botonSeleccionado = ""
        cartaSeleccionada = ""

def boton6():
    global c6,presion2,presion1,contador,carta6,botonSeleccionado,cartaSeleccionada
    contador=contador+1
    if(c6 == "J"):
        print(c1)
        photo=tkinter.PhotoImage(file="J.gif")
    elif(c6 == "Q"):
        photo=tkinter.PhotoImage(file="Q.gif")
    elif(c6 == "K"):
        photo=tkinter.PhotoImage(file="K.gif")
    elif(c6 == "A"):
        photo=tkinter.PhotoImage(file="As.gif")
    carta6.config(image=photo,width="150",height="223")
    carta6.photo = photo
    evaluar6()
    if(botonSeleccionado == ""):
        botonSeleccionado = carta6
        cartaSeleccionada = c6
    else:
        if(c6 != cartaSeleccionada):
            photo=tkinter.PhotoImage(file="reverso.gif")
            carta6.config(image=photo,width="150",height="223")
            carta6.photo = photo
            botonSeleccionado.config(image=photo,width="150",height="223")
            botonSeleccionado.photo = photo
        botonSeleccionado = ""
        cartaSeleccionada = ""

def boton7():
    global c7,presion2,presion1,contador,carta7,botonSeleccionado,cartaSeleccionada
    contador=contador+1
    if(c7 == "J"):
        print(c1)
        photo=tkinter.PhotoImage(file="J.gif")
    elif(c7 == "Q"):
        photo=tkinter.PhotoImage(file="Q.gif")
    elif(c7 == "K"):
        photo=tkinter.PhotoImage(file="K.gif")
    elif(c7 == "A"):
        photo=tkinter.PhotoImage(file="As.gif")
    carta7.config(image=photo,width="150",height="223")
    carta7.photo = photo
    evaluar7()
    if(botonSeleccionado == ""):
        botonSeleccionado = carta7
        cartaSeleccionada = c7
    else:
        if(c7 != cartaSeleccionada):
            photo=tkinter.PhotoImage(file="reverso.gif")
            carta7.config(image=photo,width="150",height="223")
            carta7.photo = photo
            botonSeleccionado.config(image=photo,width="150",height="223")
            botonSeleccionado.photo = photo
        botonSeleccionado = ""
        cartaSeleccionada = ""

def boton8():
    global c8,presion2,presion1,contador,carta8,botonSeleccionado,cartaSeleccionada
    contador=contador+1
    if(c8 == "J"):
        print(c1)
        photo=tkinter.PhotoImage(file="J.gif")
    elif(c8 == "Q"):
        photo=tkinter.PhotoImage(file="Q.gif")
    elif(c8 == "K"):
        photo=tkinter.PhotoImage(file="K.gif")
    elif(c8 == "A"):
        photo=tkinter.PhotoImage(file="As.gif")
    carta8.config(image=photo,width="150",height="223")
    carta8.photo = photo
    evaluar8()
    if(botonSeleccionado == ""):
        botonSeleccionado = carta8
        cartaSeleccionada = c8
    else:
        if(c8 != cartaSeleccionada):
            photo=tkinter.PhotoImage(file="reverso.gif")
            carta8.config(image=photo,width="150",height="223")
            carta8.photo = photo
            botonSeleccionado.config(image=photo,width="150",height="223")
            botonSeleccionado.photo = photo
        botonSeleccionado = ""
        cartaSeleccionada = ""

def evaluar1():
    global contador,presion1,presion2
    if contador%2==0:
        presion2=c1
        algo()
    else:
        presion1=c1

def evaluar2():
    global contador,presion1,presion2
    if contador%2==0:
        presion2=c2
        algo()
    else:
        presion1=c2

def evaluar3():
    global contador,presion1,presion2
    if contador%2==0:
        presion2=c3
        algo()
    else:
        presion1=c3

def evaluar4():
    global contador,presion1,presion2
    if contador%2==0:
        presion2=c4
        algo()
    else:
        presion1=c4

def evaluar5():
    global contador,presion1,presion2
    if contador%2==0:
        presion2=c5
        algo()
    else:
        presion1=c5       
def evaluar6():
    global contador,presion1,presion2
    if contador%2==0:
        presion2=c6
        algo()
    else:
        presion1=c6

def evaluar7():
    global contador,presion1,presion2
    if contador%2==0:
        presion2=c7
        algo()
    else:
        presion1=c7

def evaluar8():
    global contador,presion1,presion2
    if contador%2==0:
        presion2=c8
        algo()
    else:
        presion1=c8 

def algo():
    """
    """
    global contador,presion1,presion2,parejas
    
    if (contador!=0) and (presion1==presion2):
        parejas=parejas+1
    print ("Lleva "+str(parejas)+" parejas.")
    
    if parejas==4:
        print("Felicidades ganó")
        verificando==True

def printJuego():
    """
    """
    global contador,presion1,presion2,parejas,carta1,carta2,carta3,carta4,carta5,carta6,carta7,carta8
    
    window = tkinter.Tk()
    topFrame = tkinter.Frame(window)
    topFrame.pack()
    bottomFrame = tkinter.Frame(window)
    bottomFrame.pack(side = tkinter.BOTTOM)

    photo=tkinter.PhotoImage(file="reverso.gif")
    carta1= tkinter.Button(topFrame, command=boton1)
    carta1.config(image=photo,width="150",height="223")
    carta2= tkinter.Button(topFrame, command=boton2)
    carta2.config(image=photo,width="150",height="223")
    carta3= tkinter.Button(topFrame, command=boton3)
    carta3.config(image=photo,width="150",height="223")
    carta4= tkinter.Button(topFrame, command=boton4)
    carta4.config(image=photo,width="150",height="223")
    carta5= tkinter.Button(bottomFrame, command=boton5)
    carta5.config(image=photo,width="150",height="223")
    carta6= tkinter.Button(bottomFrame, command=boton6)
    carta6.config(image=photo,width="150",height="223")
    carta7= tkinter.Button(bottomFrame, command=boton7)
    carta7.config(image=photo,width="150",height="223")
    carta8= tkinter.Button(bottomFrame, command=boton8)
    carta8.config(image=photo,width="150",height="223")

    carta1.pack(side= tkinter.LEFT)
    carta2.pack(side= tkinter.LEFT)
    carta3.pack(side= tkinter.LEFT)
    carta4.pack(side= tkinter.LEFT)
    carta5.pack(side= tkinter.LEFT)
    carta6.pack(side= tkinter.LEFT)
    carta7.pack(side= tkinter.LEFT)
    carta8.pack(side= tkinter.LEFT)
            
    window.mainloop()  

    

def asignarDatos(letra):
    """
    """
    global c1,c2,c3,c4,c5,c6,c7,c8
    
    valorTomado = False
    while(valorTomado == False):
        x = random.randint(1,8)
        if(x == 1 and c1 == ""):
            c1 = letra
            valorTomado = True
        elif(x == 2 and c2 == ""):
            c2 = letra
            valorTomado = True
        elif(x == 3 and c3 == ""):
            c3 = letra
            valorTomado = True
        elif(x == 4 and c4 == ""):
            c4 = letra
            valorTomado = True
        elif(x == 5 and c5 == ""):
            c5 = letra
            valorTomado = True
        elif(x == 6 and c6 == ""):
            c6 = letra
            valorTomado = True
        elif(x == 7 and c7 == ""):
            c7 = letra
            valorTomado = True
        elif(x == 8 and c8 == ""):
            c8 = letra
            valorTomado = True

def chequearFinal():
    """
    """
    global e1,e2,e3,e4,e5,e6,e7,e8
    
    if(e1 == 1 and e2 == 1 and e3 == 1 and e4 == 1 and
       e5 == 1 and e6 == 1 and e7 == 1 and e8 == 1):
        return True
    else:
        return False


def juego():
    """
    Procedimiento para jugar Memoria
    """
    global c1,c2,c3,c4,c5,c6,c7,c8,e1,e2,e3,e4,e5,e6,e7,e8

    c1 = ""
    c2 = ""
    c3 = ""
    c4 = ""
    c5 = ""
    c6 = ""
    c7 = ""
    c8 = ""

    e1 = 0
    e2 = 0
    e3 = 0
    e4 = 0
    e5 = 0
    e6 = 0
    e7 = 0
    e8 = 0
    
    asignarDatos("J")
    asignarDatos("J")
    asignarDatos("Q")
    asignarDatos("Q")
    asignarDatos("K")
    asignarDatos("K")
    asignarDatos("A")
    asignarDatos("A")

    printJuego()

    juegoTerminado = False
    while(not juegoTerminado):
        escogerCarta()
        printJuego()
        if(chequearFinal() == True):
            juegoTerminado = True
    
juego()
