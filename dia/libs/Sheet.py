"""
  pydia: Sheet.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Sheet']=None
if not 'ObjectType' in _once.imported.keys() :
    from dia.libs.ObjectType import ObjectType

class Sheet:
    """Class Sheet
returned by dia.register_export() but not used otherwise yet.    """
    
    # Attributes:
    
    description = None  # () The description for the sheet. 
    filename = None  # () The filename for the sheet. 
    name = None  # () The name for the sheet. 
    objects = None  # () The list of sheet objects referenced by the sheet. 
    user = None  # () The sheet scope is user provided, not system. 
    
    # Operations
  
    def __init__(self) :
        self.description = None # 
        self.filename = None # 
        self.name = None # 
        self.objects = None # 
        self.user = None # 

_once.imported['Sheet']= Sheet
for name, object in _once.imported.items():
    globals()[name]=object
