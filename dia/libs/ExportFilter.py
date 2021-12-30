"""
  pydia: ExportFilter.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['ExportFilter']=None

class ExportFilter:
    """Class ExportFilter
returned by dia.register_export() but not used otherwise yet.    """
    
    # Attributes:
    
    name = None  # () The description for the filter. 
    unique_name = None  # () A unique name within filters to allow disambiguation. 
    
    # Operations
    
    def __init__(self) :
        self.name = None # 
        self.unique_name = None # 


_once.imported['ExportFilter']= ExportFilter
for name, object in _once.imported.items():
    globals()[name]=object
