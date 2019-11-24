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
            raise AssertionError("La clase Dummylator no esta definida")
        return True

    def test_funcNumero(self):
        self.app = DL.Dummylator()
        numero = self.app.funcNumero(4)
        return self.assertEqual(numero, 4)
    
    def test_operacionSigno(self):
        self.app = DL.Dummylator()
        cambio = self.app.operacionCambioSigno()
        return unittest.skip(cambio)
    
    def test_funcOperacion(self):
        self.app = DL.Dummylator()
        operacion = self.app.funcOperacionSimple("Suma")
        return self.assertEqual(operacion, "Suma")

    def test_funcBorrar(self):
        self.app = DL.Dummylator()
        borrar = self.app.funcBorrar()
        self.assertIsNone(borrar)
    
    
    """
    def test_activarFuncion(self):
        raiz = tk.Tk()
        self.app = DL.Dummylator(raiz)
        activar = self.app.activarFuncion()
        self.assertIsNone(activar)
    """
    
    def test_instance_Interface(self):
        try:
            raiz = tk.Tk()
            self.app = Int.Visualizacion(raiz)
        except NameError:
            raise AssertionError("La clase Interface no esta definida")
        return True
    
    """
    def test_crearVentanaPrincipal(self):
        raiz = tk.Tk()
        self.app = Int.Visualizacion(raiz)
        ventanaP = self.app.crearVentanaPrincipal(self.app)
        self.assertIsInstance(ventanaP)
        
    
    def test_crearNuevaVentana(self):
        raiz = tk.Tk()
        self.app = Int.Visualizacion(raiz)
        ventanaNueva = self.app.crearNuevaVentana(self.app,"test nueva ventana")
        self.assertFalse(ventanaNueva)
        #return isinstance(self.ventanaNueva, tk.Tk)
    
        
    def test_crearBoton(self):
       app = Int.Visualizacion(tk.Tk())
       ventana = app.crearVentanaPrincipal(app)
       boton = Int.Visualizacion.crearBoton(app,ventana=self.ventana,
                                            texto="5",bg="gray20",comando=None)
       self.assertIsInstance(boton,tk.button)
       app.destruirVentana(ventana)
    
    def test_crearEntrada(self):
        app = Int.Visualizacion(tk.Tk())
        ventana = app.crearNuevaVentana(app, None)
        entrada = app.crearEntrada(ventana,None)
        self.assertIsInstance(entrada,tk.Entry)
        app.destruirVentana(ventana)
    """

    def test_cargarWidgetsPrimaria(self):
        raiz = tk.Tk()
        self.app = Int.Visualizacion(raiz)
        primaria = self.app.cargarWidgetsPrimaria()
        return isinstance(primaria, tk.Tk)
    
    def test_cargarWidgetsSecundaria(self):
        raiz = tk.Tk()
        self.app = Int.Visualizacion(raiz)
        secundaria = self.app.cargarWidgetsSecundaria()
        return isinstance(secundaria, tk.Tk)
    
    def test_cargarWidgetsUniversidad(self):
        raiz = tk.Tk()
        self.app = Int.Visualizacion(raiz)
        universidad = self.app.cargarWidgetsUniversidad()
        return isinstance(universidad, tk.Tk)
    
        

if __name__=="__main__":
    unittest.main()
    
    
