"""
  pydia: ObjectType.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""

import _once
_once.imported['ObjectType']=None
if not 'Object' in _once.imported.keys() :
    from dia.libs.Object import Object



class ObjectType:
    """Class ObjectType
The dia.Object factory. Allows to create objects of the specific type. Use: fac    """
    # Attributes:
    name = None  # () string: the unique type indentifier of the object type. 
    version = None  # () int: version number 
    
    # Operations
    def __init__(self, name, version=0):
        self.name = name
        self.version = version

    #@staticmethod
    def create (self, x=0,y=0) :
        """ create(real: x, real: y) -> (Object: o, Handle: h1, Handle: h2)  Create a new object of this type. Returns a tuple containing the new object and up to two handles. """
        o = Object(self)
        h1 = Handle(o)
        h2 = Handle(o)
        return o , h1, h2
    

_once.imported['ObjectType']= ObjectType
for name, object in _once.imported.items():
    globals()[name]=object
