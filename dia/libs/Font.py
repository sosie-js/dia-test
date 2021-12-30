"""
  pydia: Font.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Font']=None

class Font:
    """Class Font
Provides access to some objects font property.    """

    # Attributes:
    
    family = None  # () string: family name of the font 
    name = None  # () string: legacy name of the font 
    style = None  # () int: style flags 
    
    # Operations

    def __init__(self) :
        self.family = None # 
        self.name = None # 
        self.style = None # 
        pass


_once.imported['Font']= Font
for name, object in _once.imported.items():
    globals()[name]=object
