"""
  pydia: Error.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Error']=None

class Error:
    """Class Error
The error object is just a helper to redirect errors to messages    """
    # Attributes:
    
    # Operations
    def __init__(self):
        pass

    def write(self):
        """function write"""
        raise(NotImplementedError())

_once.imported['Error']= Error
for name, object in _once.imported.items():
    globals()[name]=object
