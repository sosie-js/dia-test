"""
  pydia: Matrix.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Matrix']=None

class Matrix:
    """Class Matrix
Dia's matrix to do affine transformation    """
    # Attributes:
    x0 = None  # () double 
    xx = None  # () double 
    xy = None  # () double 
    y0 = None  # () double 
    yx = None  # () double 
    yy = None  # () double 
    
    # Operations
    def __init__(self) :
        self.x0 = None # 
        self.xx = None # 
        self.xy = None # 
        self.y0 = None # 
        self.yx = None # 
        self.yy = None # 



_once.imported['Matrix']= Matrix
for name, object in _once.imported.items():
    globals()[name]=object
