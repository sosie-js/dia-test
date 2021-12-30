"""
  pydia: ConnectionPoint.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""

import _once
_once.imported['ConnectionPoint']=None

class ConnectionPoint:
    """Class ConnectionPoint
One of the major features of Dia are connectable objects. They work by this type accesible through dia.Object.connections[]."""
    
    # Attributes:
    
    connected = None  # () List of Object: read-only list of connected objects 
    directions = None  # () Preferred directions away from the object (e.g. DIR_NORTH=0x1) 
    flags = None  # () Flags, e.g. CP_FLAGS_MAIN (=0x3) 
    object = None  # () Object: the object owning this connection point 
    pos = None  # () Point: read-only position of the connection point 
    
    # Operations
    
    def __init__(self, obj) :
        self.connected = [] # 
        self.directions = None # 
        self.flags = None # 
        self.object = obj 
        self.pos = None # 

_once.imported['ConnectionPoint']= ConnectionPoint
for name, object in _once.imported.items():
    globals()[name]=object
