"""
@author: ympalacios
"""

from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import numpy as np

class Dummylator(object):
    
    def __init__(self):
        
        self.valorActual = 0 
        self.valorGuardado = 0 
        self.operacionActual = '' 
        self.positivo = True
        self.siguienteDecimal = False
        self.decimales = 0
        self.historial = 0
        
        self.textoEntrada = tk.StringVar()
        self.textoEntrada.set('0')
    
    def funcNumero(self,valor):
        if self.positivo:
            if self.siguienteDecimal:
                self.decimales += 1
                self.valorActual = self.valorActual + (valor * (10**-self.decimales))
            else:
                self.valorActual = (self.valorActual * 10) + valor
        else:
            if self.siguienteDecimal:
                self.decimales += 1
                self.valorActual= self.valorActual - (valor * (10**-self.decimales))
            else:
                self.valorActual = (self.valorActual * 10) - valor
        self.textoEntrada.set(self.valorActual)
        return self.valorActual

    def operacionCambioSigno(self):
        self.positivo = not self.positivo
        self.valorActual *= -1
        self.textoEntrada.set(self.valorActual)
        return self.valorActual

    def reiniciarInfo(self):            
        self.valorActual = 0
        self.positivo = True
        self.siguienteDecimal = False
        self.decimales = 0
        return self.valorActual,self.positivo,self.siguienteDecimal,self.decimales
                
    def funcOperacionSimple(self,operacion):
        if operacion == 'Decimal':
            self.siguienteDecimal = True
        else:
            if operacion == 'CambioSigno':
                self.operacionCambioSigno()
                
            elif operacion == 'Igual':
                if self.operacionActual == 'Suma':
                    self.valorActual += self.valorGuardado
                    
                elif self.operacionActual == 'Resta':
                    self.valorActual = self.valorGuardado - self.valorActual
                    
                elif self.operacionActual == 'Multipl':
                    self.valorActual *= self.valorGuardado
                    
                elif self.operacionActual == 'Division':
                    self.valorActual = self.valorGuardado / self.valorActual
                    
                elif self.operacionActual == 'Sen':
                    self.valorActual = np.sin(self.valorGuardado)
                    
                elif self.operacionActual == 'Senh':
                    self.valorActual = np.sinh(self.valorGuardado)
                    
                elif self.operacionActual == 'Cos':
                    self.valorActual = np.cos(self.valorGuardado)
                    
                elif self.operacionActual == 'Cosh':
                    self.valorActual = np.cosh(self.valorGuardado)
                    
                elif self.operacionActual == 'Tan':
                    self.valorActual = np.tan(self.valorGuardado)
                
                elif self.operacionActual == 'Tanh':
                    self.valorActual = np.tanh(self.valorGuardado)
                    
                elif self.operacionActual == 'Factorial':
                    self.valorActual = np.math.factorial(self.valorActual)   
                    
                elif self.operacionActual == 'Exp':
                    self.valorActual = (self.valorGuardado)**(self.valorGuardado)
                    
                elif self.operacionActual == 'sqrt':
                    self.valorActual = np.math.sqrt(self.valorGuardado)
                    
                elif self.operacionActual == 'log':
                    self.valorActual = np.log(self.valorGuardado)
                    
                elif self.operacionActual == 'Potencia':
                    self.valorActual = pow(self.valorGuardado, self.valorActual)
                
                self.valorGuardado = 0
                self.textoEntrada.set(self.valorActual)
                
            elif operacion in ["Decimal","Suma","Resta","Multipl","Division", "Sen","Senh","Cos","Cosh",
                               "Tan","Tanh","Factorial","Exp","sqrt","log","Potencia"]:
                
                self.valorGuardado = self.valorActual
                self.operacionActual = operacion
                self.reiniciarInfo()
                
        return operacion
                
    
    def funcOperacionFormula(self,operacion):
        if operacion == 'Decimal':
            self.siguienteDecimal = True
        else:
            if operacion == 'CambioSigno':
                self.operacionCambioSigno()
                
            elif operacion == 'Igual':
                if self.operacionActual == 'Suma':
                    self.valorActual += self.valorGuardado
                    
                elif self.operacionActual == 'Resta':
                    self.valorActual = self.valorGuardado - self.valorActual
                    
                elif self.operacionActual == 'Multipl':
                    self.valorActual *= self.valorGuardado
                    
                elif self.operacionActual == 'Division':
                    self.valorActual = self.valorGuardado / self.valorActual
                    
                elif self.operacionActual == 'Sen':
                    self.valorActual = np.sin(self.valorActual)
                    
                elif self.operacionActual == 'Senh':
                    self.valorActual = np.sinh(self.valorActual)
                    
                elif self.operacionActual == 'Cos':
                    self.valorActual = np.cos(self.valorActual)
                    
                elif self.operacionActual == 'Cosh':
                    self.valorActual = np.cosh(self.valorActual)
                    
                elif self.operacionActual == 'Tan':
                    self.valorActual = np.tan(self.valorActual)
                
                elif self.operacionActual == 'Tanh':
                    self.valorActual = np.tanh(self.valorActual)
                    
                elif self.operacionActual == 'Factorial':
                    self.valorActual = np.math.factorial(self.valorGuardado)   
                    
                elif self.operacionActual == 'Exp':
                    self.valorActual = (self.valorGuardado)**(self.valorGuardado)
                    
                elif self.operacionActual == 'sqrt':
                    self.valorActual = np.math.sqrt(self.valorActual)
                    
                elif self.operacionActual == 'log':
                    self.valorActual = np.log(self.valorActual)
                    
                elif self.operacionActual == 'Potencia':
                    self.valorActual = pow(self.valorGuardado, self.valorActual)
                
                self.valorGuardado = 0
                self.textoEntrada.set(self.valorActual)
                
            elif operacion in ["Decimal","Suma","Resta","Multipl","Division", "Sen","Senh","Cos","Cosh","Tan",
                               "Tanh","Factorial","Exp","sqrt","log","Potencia"]:
                
                self.valorGuardado = self.valorActual
                self.operacionActual = operacion
                self.reiniciarInfo()
        return operacion
                
    def activarFuncion(self):
        mensaje = messagebox.showinfo(message="Debe seleccionar un modo de entrada antes de empezar a utilizar la calculadora",
                            title="Funcionalidad")
        return mensaje
        
    def modoEntrada(self,ventana,opciones):
        self.opc = tk.StringVar(ventana)
        combobox = ttk.Combobox(ventana,font=('Comic Sans MS',8,"bold italic"),textvariable=self.opc)
        combobox.config(values=opciones)
        combobox["font"] = ('Comic Sans MS', 8, 'bold italic')
        combobox.set("Modo de Entrada")
        combobox.pack()
        combobox.place(x=320,y=10)
        combobox.bind("<<ComboboxSelected>>", self.seleccionEntrada)
        return combobox

    def seleccionEntrada(self,event):
        select=self.opc.get()
        if select == "Simple":
            self.funcOperacion = self.funcOperacionSimple
            messagebox.showinfo(message="El modo de entrada es'Simple': En este modo primero debe digitar el numero y despues la funcion", 
                                title="Modo de Entrada")
            
        elif select == "Formula":
            self.funcOperacion = self.funcOperacionFormula
            messagebox.showinfo(message="El modo de entrada es 'Formula': En este modo primero debe digitar la funcion y despues el numero", 
                                title="Modo de Entrada")
        
    def funcBorrar(self):
        self.valorGuardado = 0
        self.textoEntrada.set(self.valorActual)
        self.reiniciarInfo()
        
    def Historial(self):
        self.historial = self.funcOperacion('Igual')
        self.f = open('Historial.txt','w')
        self.f.write(str(self.historial))
        self.f.close()
        
