"""
@author: ympalacios
"""

import unittest
import Tkinter as tk
import Dummylator_ as DL
import Interface as Int

class TestDummylator(unittest.TestCase):
        
    def test_instance_Dummylator(self):
        try:
            self.app = DL.Dummylator()
        except NameError:
            raise AssertionError("La clase Dummylator no está definida")
        return True

    def test_funcNumero(self):
        try:
            DL.Dummylator().funcNumero(4)
        except ValueError:
            return True
        raise AssertionError("No verifica si el numero fue ingresado") 

    def test_funcOperacion(self):
        try:
            DL.Dummylator().funcOperacion("Suma")
        except ValueError:
            return True
        raise AssertionError("No verifica si la función fue ingresada") 

    def test_funcBorrar(self):
        try:
            DL.Dummylator().funcBorrar()
        except ValueError:
            return True
        raise AssertionError("No verifica si la operación fue borrada") 
        
    def test_activarFuncion(self):
        try:
            DL.Dummylator().activarFuncion()
        except ValueError:
            return True
        raise AssertionError("No verifica si la función fue activada")
        
    def test_operacionSigno(self):
        try:
            DL.Dummylator().operacionCambioSigno()
        except ValueError:
            return True
        raise AssertionError("No verifica si se cambio el signo")
        
    
    def test_instance_Interface(self):
        try:
            self.app = Int.Visualizacion()
        except NameError:
            raise AssertionError("La clase Interface no está definida")
        return True
    
    def test_crearVentanaPrincipal(self):
        self.app = Int.Visualizacion()
        self.ventana = Int.Visualizacion.crearVentanaPrincipal(self.app)
        return isinstance(self.ventana,tk.Tk)
    
    def test_crearNuevaVentana(self):
        self.app = Int.Visualizacion()
        self.ventanaNueva = Int.Visualizacion.crearNuevaVentana(self.app,"test nueva ventana")
        return isinstance(self.ventanaNueva,tk.Tk)
        
   def test_crearBoton(self):
        self.app = Int.Visualizacion()
        self.ventana = Int.Visualizacion.crearVentanaPrincipal(self.app)
        boton = Int.Visualizacion.crearBoton(self.app,ventana=self.ventana,
        texto="5",bg="gray20",comando=self.DL.funcNumero(1))
        return isinstance(boton,tk.button)
    
    def test_crearEntrada(self):
        self.app = Int.Visualizacion()
        self.ventana = Int.Visualizacion.crearNuevaVentana(self.app, "test_Entrada")
        entrada = Int.Visualizacion.crearEntrada(ventana,21)
        return isinstance(entrada,tk.Entry)
    
    def test_cargarWidgetsPrimaria(self):
        try:
            Int.Visualizacion.cargarOpcionesIniciales()
        except ValueError:
            return True
        raise AssertionError("No verifica si se cargaron las opciones iniciales")
        

if __name__=="__main__":
    unittest.main()
    
    