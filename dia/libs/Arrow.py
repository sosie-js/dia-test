"""
  pydia: Arrow.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Arrow']=None

class Arrow:
    """Class Arrow
Dia's line objects usually ends with an dia.Arrow    """

    # Attributes:
    
    length = None  # () double: length along the line 
    type = None  # () int: the shape of the arrow 
    width = None  # () double: corresponding to line width 
    
    # Operations
    
    def __init__(self) :
        self.length = None # 
        self.type = None # 
        self.width = None # 

_once.imported['Arrow']= Arrow
for name, object in _once.imported.items():
    globals()[name]=object
