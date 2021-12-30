"""
  pydia: Text.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Text']=None

class Text:
    """Class Text
Many objects (dia.Object) having text to display provide this property.    """
    
    # Attributes:
    
    color = None  # () Color: color of the text 
    font = None  # () Font: read-only reference to font used 
    height = None  # () real: height of the font 
    position = None  # () Point: alignment position of the text 
    text = None  # () string: text data 
    
    # Operations

    def __init__(self) :
        self.color = None # 
        self.font = None # 
        self.height = None # 
        self.position = None # 
        self.text = None # 
        pass


_once.imported['Text']= Text
for name, object in _once.imported.items():
    globals()[name]=object
