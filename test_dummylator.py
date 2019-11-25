"""
@author: ympalacios
"""

import unittest
import Tkinter as tk
import Dummylator_ as DL
import Interface as It

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
    
    def test_reiniciarInfo(self):
        self.app = DL.Dummylator()
        reiniciar = self.app.reiniciarInfo()
        return unittest.skip(reiniciar)
    
    def test_funcOperacionSimple(self):
        self.app = DL.Dummylator()
        operacion = self.app.funcOperacionSimple("Suma")
        return self.assertEqual(operacion, "Suma")
    
    def test_funcOperacionFormula(self):
        self.app = DL.Dummylator()
        operacion = self.app.funcOperacionFormula("Multipl")
        return self.assertEqual(operacion, "Multipl")
    
    def test_funcOperacionFormulaD(self):
        self.app = DL.Dummylator()
        operacion = self.app.funcOperacionFormula("Division")
        return self.assertEqual(operacion, "Division")
    
    def test_funcBorrar(self):
        self.app = DL.Dummylator()
        borrar = self.app.funcBorrar()
        return self.assertEqual(borrar, None)
    
    def test_instance_Interface(self):
        try:
            raiz = tk.Tk()
            self.app = It.Visualizacion(raiz)
        except NameError:
            raise AssertionError("La clase Interface no esta definida")
        return True

    def test_crearVentanaPrincipal(self):
        raiz = tk.Tk()
        self.app = It.Visualizacion(raiz)
        ventanaP = self.app.crearVentanaPrincipal()
        return isinstance(ventanaP, tk.Tk)
    
    def test_modoEntrada(self):
        self.app1 = DL.Dummylator()
        self.app2 = It.Visualizacion(tk.Tk())
        ventana = self.app2.crearVentanaPrincipal()
        modoEntrada = self.app1.modoEntrada(ventana,None)
        return isinstance(modoEntrada, tk.Tk)
    
    def test_seleccionEntrada(self):
        self.app1 = DL.Dummylator()
        self.app2 = It.Visualizacion(tk.Tk())
        ventana = self.app2.crearVentanaPrincipal()
        modoEntrada = self.app1.modoEntrada(ventana,None)
        selEntrada = self.app1.seleccionEntrada(modoEntrada)
        return isinstance(selEntrada, tk.Tk)

    def test_crearNuevaVentana(self):
        raiz = tk.Tk()
        self.app = It.Visualizacion(raiz)
        ventanaNueva = self.app.crearNuevaVentana(None)
        return isinstance(ventanaNueva, tk.Tk)
    
    def test_crearBoton(self):
        raiz = tk.Tk()
        self.app = It.Visualizacion(raiz)
        ventana = self.app.crearVentanaPrincipal()
        boton = self.app.crearBoton(ventana,"5","gray20",None)
        return isinstance(boton,tk.Tk)
    
    def test_crearBotonNivel(self):
        raiz = tk.Tk()
        self.app = It.Visualizacion(raiz)
        ventana = self.app.crearVentanaPrincipal()
        botonNivel = self.app.crearBotonNivel(ventana,"Nivel",None)
        return isinstance(botonNivel,tk.Tk)
    
    def test_crearEntrada(self):
        raiz = tk.Tk()
        app = It.Visualizacion(raiz)
        ventana = app.crearNuevaVentana(None)
        entrada = app.crearEntrada(ventana,21)
        return isinstance(entrada,tk.Tk)
    
    def test_cargarOpcionesIniciales(self):
        raiz = tk.Tk()
        self.app = It.Visualizacion(raiz)
        opciones = self.app.cargarOpcionesIniciales()
        return isinstance(opciones, tk.Tk)

    def test_cargarWidgetsPrimaria(self):
        raiz = tk.Tk()
        self.app = It.Visualizacion(raiz)
        primaria = self.app.cargarWidgetsPrimaria()
        return isinstance(primaria, tk.Tk)
    
    def test_cargarWidgetsSecundaria(self):
        raiz = tk.Tk()
        self.app = It.Visualizacion(raiz)
        secundaria = self.app.cargarWidgetsSecundaria()
        return isinstance(secundaria, tk.Tk)
    
    def test_cargarWidgetsUniversidad(self):
        raiz = tk.Tk()
        self.app = It.Visualizacion(raiz)
        universidad = self.app.cargarWidgetsUniversidad()
        return isinstance(universidad, tk.Tk)    

if __name__=="__main__":
    unittest.main()
    