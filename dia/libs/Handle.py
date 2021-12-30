"""
  pydia: Handle.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""

import _once
_once.imported['Handle']=None

class Handle:
    """Class Handle
A handle is used to connect objects or for object resizing.    """
    
    # Attributes:
    
    connect_type = None  # () NONCONNECTABLE=0. 
    connected_to = None  # () The connected ConnectionPoint object or None. 
    id = None  # () Can be used to derive preferred directions from it. 
    pos = None  # () The position of the connection point. 
    type = None  # () NON_MOVABLE=0, MAJOR_CONTROL=1, MINOR_CONTROL=2 
    
    # Operations
    
    def __init__(self, obj) :
        self.connect_type = None # 
        self.connected_to = None # 
        self.obj = obj #extra?
        self.id = None # 
        self.pos = None # 
        self.type = None # 

    def connect (self, cp) :
        """ connect(ConnectionPoint: cp) -> None.  Connect object A's handle with object B's connection point. To disconnect a handle pass in None. """
        self.connected_to = cp
        cp.connected.append(self.obj)


_once.imported['Handle']= Handle
for name, object in _once.imported.items():
    globals()[name]=object
