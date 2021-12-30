"""
  pydia: Property.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Property']=None
if not 'BezPoint' in _once.imported.keys() :
    from dia.libs.BezPoint import BezPoint
if not 'Image' in _once.imported.keys() :
    from dia.libs.Image import Image
if not 'Point' in _once.imported.keys() :
    from dia.libs.Point import Point
if not 'Arrow' in _once.imported.keys() :
    from dia.libs.Arrow import Arrow
if not 'Font' in _once.imported.keys() :
    from dia.libs.Font import Font
if not 'Text' in _once.imported.keys() :
    from dia.libs.Text import Text
if not 'Matrix' in _once.imported.keys() :
    from dia.libs.Matrix import Matrix

class Property:
    """Class Property
Interface to so called StdProps, the mechanism to control most of Dia's canvas     """
   
    # Attributes:
    
    name = None  # () string: the name of the property 
    type = None  # () string: the type name of the object 
    value = None  # () various: the value is of type char, bool, dict, int, real, string, Text, Point, 
    visible = None  # () bool: visibility of the property 
    
    # Operations
    
    def __init__(self, name, type, value, visible):
        self.name = name
        self.type = type
        self.value = value
        self.visible = visible
        


_once.imported['Property']= Property
for name, object in _once.imported.items():
    globals()[name]=object
