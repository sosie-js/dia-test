"""
  pydia: PaperInfo.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Paperinfo']=None

class Paperinfo:
    """Class Paperinfo
dia.Paperinfo is part of dia.DiagramData describing the paper    """
    
    # Attributes:
    
    height = None  # () real: height of the drawable area (sans margins) 
    is_portrait = None  # () int: paper orientation 
    name = None  # () string: paper name, e.g. A4 or Letter 
    scaling = None  # () real: factor to zoom the diagram on the paper 
    width = None  # () real: width of the drawable area (sans margins) 
    
    # Operations
    
    def __init__(self) :
        self.height = None # 
        self.is_portrait = None # 
        self.name = None # 
        self.scaling = None # 
        self.width = None # 

_once.imported['Paperinfo']= Paperinfo
for name, object in _once.imported.items():
    globals()[name]=object
