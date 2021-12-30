"""
  pydia: Rectangle.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Rectangle']=None

class Rectangle:
    """Class Rectangle
The dia.Rectangle does not only provide access trough it's members but also via a sequence interface."""
   
    # Attributes:
    
    bottom = None  # () int or double: lower edge y coordinate 
    left = None  # () int or double: left edge x coordinate 
    right = None  # () int or double: right edge x coordinate 
    top = None  # () int or double: upper edge y coordinate 
    
    # Operations
    
    def __init__(self) :
        self.bottom = None # 
        self.left = None # 
        self.right = None # 
        self.top = None # 


_once.imported['Rectangle']= Rectangle
for name, object in _once.imported.items():
    globals()[name]=object
