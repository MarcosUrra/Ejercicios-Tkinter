from cProfile import label
from sqlite3 import Cursor
from tkinter import *
from tkinter import messagebox

#-----------------------------------------------
ventanaPrincipal=Tk()
ventanaPrincipal.geometry("500x400+370+50")
ventanaPrincipal.resizable(width=FALSE, height=FALSE)
ventanaPrincipal.title("Adivinador")
fondo=PhotoImage(file="ISAUI.png")
fondo1=Label(ventanaPrincipal, image=fondo)
fondo1.place(x=0, y=0, relwidth=1, relheight=1)
bienvenido=Label(ventanaPrincipal, font="arial, 13", fg="lawn green", bg="grey15", text="Bienvenido / Welcome\n Selecciona el idioma en el que quieres jugar\n Select the language in which you want to play")
bienvenido.place(x=75, y=7)

opcionIdioma=IntVar()
idiomaEspañol=Radiobutton(ventanaPrincipal, variable=opcionIdioma, text="ESPAÑOL", value=1, font="verdana, 10", fg="lawn green", bg="grey15")
idiomaEspañol.place(x=60, y=340)
idiomaIngles=Radiobutton(ventanaPrincipal, variable=opcionIdioma, text="INGLES", value=2, font="verdana, 10", fg="lawn green", bg="grey15")
idiomaIngles.place(x=160, y=340)

#-----------------------------------------------

def ventanaJuego():
    if opcionIdioma.get()==1:
        ventana=Toplevel()
        ventana.geometry("500x400+370+50")
        ventana.resizable(width=FALSE, height=FALSE)
        ventana.title("Adivinador")
        ventana.config(bg="gray32")
        
        
        pensaUnNumero=Label(ventana, text="-Pensá un número de dos cifras (que no sean iguales)", bg="gray32", font="verdana, 13", fg="lawn green")
        pensaUnNumero.place(x=20, y=20)
        invertilo=Label(ventana, text="-Invertí el orden de las cifras", bg="gray32", font="verdana, 13", fg="lawn green")
        invertilo.place(x=20, y=60)
        
        restaElNumero=Label(ventana, text="-Restale ese número al primero que pensaste", bg="gray32", font="verdana, 13", fg="lawn green")
        restaElNumero.place(x=20, y=100)
        ingresaElNumero1=Label(ventana, text="-Ingresa ese numero aquí-->", bg="gray32", font="verdana, 13", fg="lawn green").place(x=20, y=140)
        sumaLasDosCifras=Label(ventana, text="-Ahora sumá las cifras del número que pensaste al principio", bg="gray32", font="verdana, 13", fg="lawn green")
        sumaLasDosCifras.place(x=20, y=180)
        ingresaElNumero2=Label(ventana, text="-Ingresa ese numero aquí-->", bg="gray32", font="verdana, 13", fg="lawn green").place(x=20, y=220)

        ingreso1=IntVar(value="")
        boxIngresaElNumero1=Entry(ventana,textvariable=ingreso1)
        boxIngresaElNumero1.place(x=245, y=142)
        ingreso2=IntVar(value="")
        boxIngresaElNumero2=Entry(ventana, textvariable=ingreso2)
        boxIngresaElNumero2.place(x=245, y=225)

        variableResultado=StringVar()

        def adivinar():
            
                resultadoDiv9=ingreso1.get()/9
                operacion1=(ingreso2.get()-resultadoDiv9)/2 
                operacion2=(ingreso2.get()+resultadoDiv9)/2
                a=int(operacion1)
                b=int(operacion2)
                messagebox.showinfo(title="Lo adiviné", message=(b,a))
            
        botonAdivinar=Button(ventana, text="Adiviná mi número", cursor="hand2", font="verdana, 13", bg="lawn green", bd=5, command=adivinar)
        botonAdivinar.place(x=160, y=280)
#---------------------------------------------------------------------------
    elif opcionIdioma.get()==2:
        ventana=Toplevel()
        ventana.geometry("500x400+370+50")
        ventana.resizable(width=FALSE, height=FALSE)
        ventana.title("Diviner")
        ventana.config(bg="gray32")
    
        pensaUnNumero=Label(ventana, text="-Think of a two-digit number (that are not the same)", bg="gray32", font="verdana, 13", fg="lawn green")
        pensaUnNumero.place(x=20, y=20)
        invertilo=Label(ventana, text="-I reversed the order of the numbers", bg="gray32", font="verdana, 13", fg="lawn green")
        invertilo.place(x=20, y=60)
        restaElNumero=Label(ventana, text="-Subtract that number from the first you thought of", bg="gray32", font="verdana, 13", fg="lawn green")
        restaElNumero.place(x=20, y=100)
        ingresaElNumero1=Label(ventana, text="-Enter that number here-->", bg="gray32", font="verdana, 13", fg="lawn green").place(x=20, y=140)
        sumaLasDosCifras=Label(ventana, text="-Now add the digits of the number you thought of at first", bg="gray32", font="verdana, 13", fg="lawn green")
        sumaLasDosCifras.place(x=20, y=180)
        ingresaElNumero2=Label(ventana, text="-Enter that number here-->", bg="gray32", font="verdana, 13", fg="lawn green").place(x=20, y=220)

        ingreso1=IntVar(value="")
        boxIngresaElNumero1=Entry(ventana,textvariable=ingreso1)
        boxIngresaElNumero1.place(x=245, y=142)
        ingreso2=IntVar(value="")
        boxIngresaElNumero2=Entry(ventana, textvariable=ingreso2)
        boxIngresaElNumero2.place(x=245, y=225)


        def adivinar():
            resultadoDiv9=ingreso1.get()/9
            operacion1=(ingreso2.get()-resultadoDiv9)/2 
            operacion2=(ingreso2.get()+resultadoDiv9)/2
            a=int(operacion1)
            b=int(operacion2)
            messagebox.showinfo(title="Guessed!!!", message=(b,a))

        botonAdivinar=Button(ventana, text="Guess my number", cursor="hand2", font="verdana, 15", bg="lawn green", bd=5, command=adivinar)
        botonAdivinar.place(x=150, y=280)
#----------------------------------------------------------------------------------------------

botonSeleccionar=Button(ventanaPrincipal,text="Seleccionar/select", command=ventanaJuego, cursor="hand2", bd=7, font="arial, 12", fg="lawn green", bg="grey27")
botonSeleccionar.place(x=270, y=330)

ventanaPrincipal.mainloop()