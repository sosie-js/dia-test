"""
  pydia: MenuItem.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Menuitem']=None

class Menuitem:
    """Class Menuitem
dia.Menuitem is holding menu functions for dia.Object    """
    # Attributes:
    active = None  # () boolean: if it is callable 
    text = None  # () string: what would be written in the menu 
    
    # Operations
    def __init__(self):
        self.active = None # 
        self.text = None # 

    def call(self):
        """call() -> None.  Invoke the menuitem callback on object."""
        raise(NotImplementedError())
        return None 
    
_once.imported['Menuitem']= Menuitem
for name, object in _once.imported.items():
    globals()[name]=object
