"""
@author: ympalacios
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Dummylator_ as Dummylator
from functools import partial


class Visualizacion(object):
    
    def __init__(self,raiz):
       self.ventanaPrincipal = raiz
       self.Dummylator = Dummylator.Dummylator()
       self.crearVentanaPrincipal()
       self.cargarOpcionesIniciales()

    def crearVentanaPrincipal(self):
       self.ventanaPrincipal.title("Dummylator")
       self.ventanaPrincipal.geometry("500x500")
       self.ventanaPrincipal.config(background = "gray85") 
   
    def crearNuevaVentana(self, titulo):
       self.ventanaNueva = tk.Toplevel()
       self.ventanaNueva.title(titulo)
       self.ventanaNueva.geometry("500x500")
       self.ventanaNueva.config(background = "gray85")
       return self.ventanaNueva
   
    def destruirVentana(self,ventana):
        if ventana:
            ventana.destroy()
            return ventana
   
    def mostrarError(self,mensaje): 
       self.ventanaError = tk.Tk()
       self.ventanaError.title("Error")
       self.ventanaError.geometry("100x100")
       self.ventanaError.config(background = "gray85")
       
       tk.Label(self.ventanaError,text=mensaje,font='Arial 10 bold', background="white").place(x=15,y=20)
       tk.Button(self.ventanaError, text="OK", command=self.ventanaError.destroy,background="gray20",font='Arial 11 bold').place(x=140,y=60)
       
       return self.ventanaError
   
    def crearBoton(self,ventana,texto,bg,comando):
        boton = tk.Button(ventana, text=texto,bg=bg,fg="white",activebackground="LightCyan3", width = 2, height = 2,command=comando) 
        return boton

    def crearBotonNivel(self,ventana,texto,comando):
        botonNivel = tk.Button(ventana, text=texto,activebackground="gray90",command=comando)
        botonNivel["font"] = ('Comic Sans MS', 8, 'bold italic')
        return botonNivel
        
    
    def crearEntrada(self,ventana,width):
        self.textoEntrada = tk.StringVar()
        self.textoEntrada.set('0')
        entrada = tk.Entry(ventana, font=('Comic Sans MS', 14, 'bold italic'),
                           width=width,textvariable=self.Dummylator.textoEntrada,
                           bd=4,insertwidth=4,justify="right")
        return entrada
    
        
    def cargarOpcionesIniciales(self):
        self.etiquetaOpciones = tk.Label(self.ventanaPrincipal, text = "Dummylator")
        self.etiquetaOpciones["font"] = ('Comic Sans MS', 10, 'bold italic')
        self.etiquetaOpciones["background"] = "gray85"
        self.etiquetaOpciones.pack()
        
        self.botonPrimaria = self.crearBotonNivel(self.ventanaPrincipal, "Primaria",self.cargarWidgetsPrimaria).place(x=10,y=5)
        self.botonSecundaria = self.crearBotonNivel(self.ventanaPrincipal, "Secundaria",self.cargarWidgetsSecundaria).place(x=10,y=38)
        self.botonUniversidad = self.crearBotonNivel(self.ventanaPrincipal, "Universidad",self.cargarWidgetsUniversidad).place(x=10,y=71)

        self.panelEntradas = self.crearEntrada(self.ventanaPrincipal,21).place(x=100, y=200)
        self.combobox = self.Dummylator.modoEntrada(self.ventanaPrincipal, ["Simple","Formula"])
        
        
        self.botonUno = self.crearBoton(self.ventanaPrincipal,"1","gray20",lambda:self.Dummylator.funcNumero(1)).place(x=120,y=260)
        
        self.butonDos = self.crearBoton(self.ventanaPrincipal,"2","gray20",lambda:self.Dummylator.funcNumero(2)).place(x=170,y=260)

        self.botonTres = self.crearBoton(self.ventanaPrincipal,"3","gray20",lambda:self.Dummylator.funcNumero(3)).place(x=220,y=260)
                                         
        self.botonSuma = self.crearBoton(self.ventanaPrincipal,"+","gray20",lambda:self.Dummylator.funcOperacion('Suma')).place(x=270,y=260)
        
        self.botonResta = self.crearBoton(self.ventanaPrincipal,"-","gray20",lambda:self.Dummylator.funcOperacion('Resta')).place(x=320,y=260)
                    
        self.botonCuatro = self.crearBoton(self.ventanaPrincipal,"4","gray20",lambda:self.Dummylator.funcNumero(4)).place(x=120,y=310)

        self.botonCinco = self.crearBoton(self.ventanaPrincipal,"5","gray20",lambda:self.Dummylator.funcNumero(5)).place(x=170,y=310)
                                         
        self.botonSeis = self.crearBoton(self.ventanaPrincipal,"6","gray20",lambda:self.Dummylator.funcNumero(6)).place(x=220,y=310)
    
        self.botonSiete = self.crearBoton(self.ventanaPrincipal,"7","gray20",lambda:self.Dummylator.funcNumero(7)).place(x=120,y=360)

        self.botonOcho = self.crearBoton(self.ventanaPrincipal,"8","gray20",lambda:self.Dummylator.funcNumero(8)).place(x=170,y=360)

        self.botonNueve = self.crearBoton(self.ventanaPrincipal,"9","gray20",lambda:self.Dummylator.funcNumero(9)).place(x=220,y=360)

        self.botonIgual = self.crearBoton(self.ventanaPrincipal, "=","gray20",lambda:self.Dummylator.funcOperacion('Igual')).place(x=270,y=310)   
                                         
        self.botonCero = self.crearBoton(self.ventanaPrincipal,"0","gray20",lambda:self.Dummylator.funcNumero(0)).place(x=170,y=410)

        self.botonBorrar = self.crearBoton(self.ventanaPrincipal,"AC","gray20",lambda:self.Dummylator.funcBorrar()).place(x=320,y=310)  
        
        self.botonHistorial = self.crearBotonNivel(self.ventanaPrincipal,"Historial",lambda:self.Dummylator.Historial()).place(x=400,y=450)
        
        
    def cargarWidgetsPrimaria(self):
        
        self.ventanaPrimaria = self.crearNuevaVentana('Primaria')
        self.panelEntradas = self.crearEntrada(self.ventanaPrimaria,21).place(x=100, y=200)
        self.combobox = self.Dummylator.modoEntrada(self.ventanaPrimaria, ["Simple","Formula"])
        
        self.botonSecundaria = self.crearBotonNivel(self.ventanaPrimaria, "Secundaria",self.cargarWidgetsSecundaria).place(x=10,y=38)
        self.botonUniversidad = self.crearBotonNivel(self.ventanaPrimaria, "Universidad",self.cargarWidgetsUniversidad).place(x=10,y=71)

        self.botonUno = self.crearBoton(self.ventanaPrimaria,"1","gray20",lambda:self.Dummylator.funcNumero(1)).place(x=120,y=260)
        
        self.botonDos = self.crearBoton(self.ventanaPrimaria,"2","gray20",lambda:self.Dummylator.funcNumero(2)).place(x=170,y=260)

        self.botonTres = self.crearBoton(self.ventanaPrimaria,"3","gray20",lambda:self.Dummylator.funcNumero(3)).place(x=220,y=260)
                                         
        self.botonSuma = self.crearBoton(self.ventanaPrimaria,"+","slate gray",lambda:self.Dummylator.funcOperacion('Suma')).place(x=270,y=260)
        
        self.botonResta = self.crearBoton(self.ventanaPrimaria,"-","slate gray",lambda:self.Dummylator.funcOperacion('Resta')).place(x=320,y=260)
                    
        self.botonCuatro = self.crearBoton(self.ventanaPrimaria,"4","gray20",lambda:self.Dummylator.funcNumero(4)).place(x=120,y=310)

        self.botonCinco = self.crearBoton(self.ventanaPrimaria,"5","gray20",lambda:self.Dummylator.funcNumero(5)).place(x=170,y=310)
                                         
        self.botonSeis = self.crearBoton(self.ventanaPrimaria,"6","gray20",lambda:self.Dummylator.funcNumero(6)).place(x=220,y=310)
        
        self.botonMult = self.crearBoton(self.ventanaPrimaria,"x","slate gray",lambda:self.Dummylator.funcOperacion('Multipl')).place(x = 270, y= 310)    
    
        self.botonDivision = self.crearBoton(self.ventanaPrimaria,"/","slate gray",lambda:self.Dummylator.funcOperacion('Division')).place(x = 320, y= 310)  
    
        self.botonSiete = self.crearBoton(self.ventanaPrimaria,"7","gray20",lambda:self.Dummylator.funcNumero(7)).place(x=120,y=360)

        self.botonOcho = self.crearBoton(self.ventanaPrimaria,"8","gray20",lambda:self.Dummylator.funcNumero(8)).place(x=170,y=360)

        self.botonNueve = self.crearBoton(self.ventanaPrimaria,"9","gray20",lambda:self.Dummylator.funcNumero(9)).place(x=220,y=360)

        self.botonIgual = self.crearBoton(self.ventanaPrimaria, "=","gray20",lambda:self.Dummylator.funcOperacion('Igual')).place(x=270,y=360)   
                                         
        self.botonCero = self.crearBoton(self.ventanaPrimaria,"0","gray20",lambda:self.Dummylator.funcNumero(0)).place(x=170,y=410)
        
        self.botonPunto = self.crearBoton(self.ventanaPrimaria, ".","gray20",lambda:self.Dummylator.funcOperacion('Decimal')).place(x = 220, y= 410)

        self.botonBorrar = self.crearBoton(self.ventanaPrimaria,"AC","gray20",lambda:self.Dummylator.funcBorrar()).place(x=320,y=360)  
        
        self.botonHistorial = self.crearBotonNivel(self.ventanaPrimaria,"Historial",lambda:self.Dummylator.Historial()).place(x=400,y=450)
        
    def cargarWidgetsSecundaria(self):

        self.ventanaSecundaria = self.crearNuevaVentana('Secundaria')
        self.panelEntradas = self.crearEntrada(self.ventanaSecundaria,25).place(x=100, y=200)
        self.combobox = self.Dummylator.modoEntrada(self.ventanaSecundaria, ["Simple","Formula"])
        
        self.botonPrimaria = self.crearBotonNivel(self.ventanaSecundaria, "Primaria",self.cargarWidgetsPrimaria).place(x=10,y=5)
        self.botonUniversidad = self.crearBotonNivel(self.ventanaSecundaria, "Universidad",self.cargarWidgetsUniversidad).place(x=10,y=71)

        self.botonUno = self.crearBoton(self.ventanaSecundaria,"1","gray20",lambda:self.Dummylator.funcNumero(1)).place(x=120,y=260)
        
        self.botonDos = self.crearBoton(self.ventanaSecundaria,"2","gray20",lambda:self.Dummylator.funcNumero(2)).place(x=170,y=260)

        self.botonTres = self.crearBoton(self.ventanaSecundaria,"3","gray20",lambda:self.Dummylator.funcNumero(3)).place(x=220,y=260)
                                         
        self.botonSuma = self.crearBoton(self.ventanaSecundaria,"+","slate gray",lambda:self.Dummylator.funcOperacion('Suma')).place(x=270,y=260)
        
        self.botonResta = self.crearBoton(self.ventanaSecundaria,"-","slate gray",lambda:self.Dummylator.funcOperacion('Resta')).place(x=320,y=260)
                    
        self.botonCuatro = self.crearBoton(self.ventanaSecundaria,"4","gray20",lambda:self.Dummylator.funcNumero(4)).place(x=120,y=310)

        self.botonCinco = self.crearBoton(self.ventanaSecundaria,"5","gray20",lambda:self.Dummylator.funcNumero(5)).place(x=170,y=310)
                                         
        self.botonSeis = self.crearBoton(self.ventanaSecundaria,"6","gray20",lambda:self.Dummylator.funcNumero(6)).place(x=220,y=310)
        
        self.botonMult = self.crearBoton(self.ventanaSecundaria,"x","slate gray",lambda:self.Dummylator.funcOperacion('Multipl')).place(x = 270, y= 310)    
    
        self.botonDivision = self.crearBoton(self.ventanaSecundaria,"/","slate gray",lambda:self.Dummylator.funcOperacion('Division')).place(x = 320, y= 310)  
    
        self.botonSiete = self.crearBoton(self.ventanaSecundaria,"7","gray20",lambda:self.Dummylator.funcNumero(7)).place(x=120,y=360)

        self.botonOcho = self.crearBoton(self.ventanaSecundaria,"8","gray20",lambda:self.Dummylator.funcNumero(8)).place(x=170,y=360)

        self.botonNueve = self.crearBoton(self.ventanaSecundaria,"9","gray20",lambda:self.Dummylator.funcNumero(9)).place(x=220,y=360)

        self.botonIgual = self.crearBoton(self.ventanaSecundaria, "=","gray20",lambda:self.Dummylator.funcOperacion('Igual')).place(x=270,y=410)   
                                         
        self.botonCero = self.crearBoton(self.ventanaSecundaria,"0","gray20",lambda:self.Dummylator.funcNumero(0)).place(x=170,y=410)
        
        self.botonPunto = self.crearBoton(self.ventanaSecundaria, ".","gray20",lambda:self.Dummylator.funcOperacion('Decimal')).place(x = 220, y= 410)

        self.botonBorrar = self.crearBoton(self.ventanaSecundaria,"AC","gray20",lambda:self.Dummylator.funcBorrar()).place(x=320,y=410)
        
        self.botonSen = self.crearBoton(self.ventanaSecundaria, "Sen","khaki3",lambda:self.Dummylator.funcOperacion('Sen')).place(x = 370, y= 260)

        self.botonCos = self.crearBoton(self.ventanaSecundaria, "Cos","khaki3",lambda:self.Dummylator.funcOperacion('Cos')).place(x = 370, y= 310)        

        self.botonTan = self.crearBoton(self.ventanaSecundaria, "Tan","khaki3",lambda:self.Dummylator.funcOperacion('Tan')).place(x = 370, y= 360)
        
        self.botonRaiz = self.crearBoton(self.ventanaSecundaria, "sqrt","khaki3",lambda:self.Dummylator.funcOperacion('sqrt')).place(x=270,y=360)
        
        self.botonLog = self.crearBoton(self.ventanaSecundaria,"Log","khaki3",lambda:self.Dummylator.funcOperacion('log')).place(x=320,y=360)
        
        self.butonHistorial = self.crearBotonNivel(self.ventanaSecundaria,"Historial",lambda:self.Dummylator.Historial()).place(x=400,y=450)


    def cargarWidgetsUniversidad(self):
        
        self.ventanaUniversidad = self.crearNuevaVentana('Universidad')
        self.panelEntradas = self.crearEntrada(self.ventanaUniversidad,26).place(x=100, y=200)
        self.combobox = self.Dummylator.modoEntrada(self.ventanaUniversidad, ["Simple","Formula"])
        
        self.botonPrimaria = self.crearBotonNivel(self.ventanaUniversidad, "Primaria",self.cargarWidgetsPrimaria).place(x=10,y=5)
        self.botonSecundaria = self.crearBotonNivel(self.ventanaUniversidad, "Secundaria",self.cargarWidgetsSecundaria).place(x=10,y=38)

        self.botonUno = self.crearBoton(self.ventanaUniversidad,"1","gray20",lambda:self.Dummylator.funcNumero(1)).place(x=100,y=260)
        
        self.botonDos = self.crearBoton(self.ventanaUniversidad,"2","gray20",lambda:self.Dummylator.funcNumero(2)).place(x=150,y=260)

        self.botonTres = self.crearBoton(self.ventanaUniversidad,"3","gray20",lambda:self.Dummylator.funcNumero(3)).place(x=200,y=260)
                                         
        self.botonSuma = self.crearBoton(self.ventanaUniversidad,"+","slate gray",lambda:self.Dummylator.funcOperacion('Suma')).place(x=250,y=260)
        
        self.botonResta = self.crearBoton(self.ventanaUniversidad,"-","slate gray",lambda:self.Dummylator.funcOperacion('Resta')).place(x=300,y=260)
                    
        self.botonCuatro = self.crearBoton(self.ventanaUniversidad,"4","gray20",lambda:self.Dummylator.funcNumero(4)).place(x=100,y=310)

        self.botonCinco = self.crearBoton(self.ventanaUniversidad,"5","gray20",lambda:self.Dummylator.funcNumero(5)).place(x=150,y=310)
                                         
        self.botonSeis = self.crearBoton(self.ventanaUniversidad,"6","gray20",lambda:self.Dummylator.funcNumero(6)).place(x=200,y=310)
        
        self.botonMult = self.crearBoton(self.ventanaUniversidad,"x","slate gray",lambda:self.Dummylator.funcOperacion('Multipl')).place(x=250,y=310)    
    
        self.botonDivision = self.crearBoton(self.ventanaUniversidad,"/","slate gray",lambda:self.Dummylator.funcOperacion('Division')).place(x=300,y=310)  
    
        self.botonSiete = self.crearBoton(self.ventanaUniversidad,"7","gray20",lambda:self.Dummylator.funcNumero(7)).place(x=100,y=360)

        self.botonOcho = self.crearBoton(self.ventanaUniversidad,"8","gray20",lambda:self.Dummylator.funcNumero(8)).place(x=150,y=360)

        self.botonNueve = self.crearBoton(self.ventanaUniversidad,"9","gray20",lambda:self.Dummylator.funcNumero(9)).place(x=200,y=360)

        self.botonIgual = self.crearBoton(self.ventanaUniversidad, "=","gray20",lambda:self.Dummylator.funcOperacion('Igual')).place(x=200,y=410)   
                                         
        self.botonCero = self.crearBoton(self.ventanaUniversidad,"0","gray20",lambda:self.Dummylator.funcNumero(0)).place(x=100,y=410)
        
        self.botonPunto = self.crearBoton(self.ventanaUniversidad, ".","gray20",lambda:self.Dummylator.funcOperacion('Decimal')).place(x=150,y=410)

        self.botonBorrar = self.crearBoton(self.ventanaUniversidad,"AC","gray20",lambda:self.Dummylator.funcBorrar()).place(x=350,y=410)
        
        self.botonSen = self.crearBoton(self.ventanaUniversidad, "Sen","khaki3",lambda:self.Dummylator.funcOperacion('Sen')).place(x=350,y=260)

        self.botonCos = self.crearBoton(self.ventanaUniversidad, "Cos","khaki3",lambda:self.Dummylator.funcOperacion('Cos')).place(x=350,y=310)        

        self.botonTan = self.crearBoton(self.ventanaUniversidad, "Tan","khaki3",lambda:self.Dummylator.funcOperacion('Tan')).place(x=350,y=360)
        
        self.botonRaiz = self.crearBoton(self.ventanaUniversidad, "sqrt","khaki3",lambda:self.Dummylator.funcOperacion('sqrt')).place(x=250,y=360)
        
        self.botonLog = self.crearBoton(self.ventanaUniversidad,"Log","khaki3",lambda:self.Dummylator.funcOperacion('log')).place(x=300,y=360)
        
        self.botonExp = self.crearBoton(self.ventanaUniversidad, "Exp","salmon3",lambda:self.Dummylator.funcOperacion('Exp')).place(x=250,y=410)
        
        self.botonFactorial = self.crearBoton(self.ventanaUniversidad, "!","salmon3",lambda:self.Dummylator.funcOperacion('Factorial')).place(x=300,y=410)
        
        self.botonSen = self.crearBoton(self.ventanaUniversidad, "Senh","salmon3",lambda:self.Dummylator.funcOperacion('Senh')).place(x=400,y=260)

        self.botonCos = self.crearBoton(self.ventanaUniversidad, "Cosh","salmon3",lambda:self.Dummylator.funcOperacion('Cosh')).place(x=400,y=310)        

        self.botonTan = self.crearBoton(self.ventanaUniversidad, "Tanh","salmon3",lambda:self.Dummylator.funcOperacion('Tanh')).place(x=400,y=360)
        
        self.butonHistorial = self.crearBotonNivel(self.ventanaUniversidad,"Historial",lambda:self.Dummylator.Historial()).place(x=400,y=450)

if __name__=="__main__":
    raiz = tk.Tk()
    App = Visualizacion(raiz)
    raiz.mainloop() 