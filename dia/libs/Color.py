"""
  pydia: Color.py - 2021.09
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Color']=None

class Color:
    """Class Color
A color either defined by a color string or by a tuple with three elements (r, g, b) with type float 0.0 ... 1.0 or range int 0 ... 65535"""

    # Attributes:
    
    alpha = None  # () double: alpha color component [0 .. 1.0] 
    blue = None  # () double: blue color component [0 .. 1.0] 
    green = None  # () double: green color component [0 .. 1.0] 
    red = None  # () double: red color component [0 .. 1.0] 
    
    # Operations
        	
    def __init__(self) :
        self.alpha = None # 
        self.blue = None # 
        self.green = None # 
        self.red = None # 
        pass

_once.imported['Color']= Color
for name, object in _once.imported.items():
    globals()[name]=object
