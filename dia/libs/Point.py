"""
  pydia: Point.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Point']=None

class Point:
    """Class Point
The dia.Point does not only provide access trough it's members but also via a s    """
    
    # Attributes:
    
    x = None  # () double: coordinate horizontal part 
    y = None  # () double: coordinate vertical part 
    
    # Operations
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return str([ self.x , self.y]) 

_once.imported['Point']= Point
for name, object in _once.imported.items():
    globals()[name]=object
