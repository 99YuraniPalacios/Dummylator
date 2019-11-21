"""
@author: ympalacios
"""

import unittest
import Tkinter as tk
import Dummylator as DLS

class TestDummylator(unittest.TestCase):
        
    def test_instance_Calculator(self):
        try:
            self.app = DLS.Calculator(master)
        except NameError:
            raise AssertionError("The class Calculator does not exist")
        return True

    def test_funcNumber(self):
        root = tk.Tk()
        self.app = DLS.Calculator(root)
        number = self.app.funcNumber(4)
        self.assertEqual(number, 4)

    def test_funcOperator(self):
        root = tk.Tk()
        self.app = DLS.Calculator(root)
        operator = self.app.funcOperator('Sum')
        self.assertEqual(operator, 'Sum')
        
    def test_funcDelete(self):
        root = tk.Tk()
        self.app = DLS.Calculator(root)
        delete = self.app.funcDelete()
        self.assertEqual(delete)
        
    def test_WindowPrimary(self):
        root = tk.Tk()
        self.app = DLS.Calculator(root)
        primaryWindow = self.app.loadPrimaryWindow()
        self.assertIsInstance(primaryWindow,root)
        
    def test_windowSecundary(self):
        root = tk.Tk()
        self.app = DLS.Calculator(root)
        secundaryWindow = self.app.loadSecundaryWindow()
        self.assertIsInstance(secundaryWindow,root)
        
    def test_windowUniversity(self):
        root = tk.Tk()
        self.app = DLS.Calculator(root)
        universityWindow = self.app.loadUniversityWindow()
        self.assertIsInstance(universityWindow, root)

if __name__=="__main__":
    unittest.main()
    
    