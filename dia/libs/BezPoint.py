"""
  pydia: BezPoint.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""

import _once
_once.imported['BezPoint']=None

class BezPoint:
    """Class BezPoint
A dia.Point, a bezier type and two control points (dia.Point) make a bezier point."""
   
    # Attributes:
    
    p1 = None  # () Point: first control point for CURVETO 
    p2 = None  # () Point: second control point for CURVETO 
    p3 = None  # () Point: target point for CURVETO 
    type = None  # () int: MOVETO, LINETO using p1 only;  CURVETO all 3 points 
    
    # Operations

    def __init__(self) :
        self.p1 = None # 
        self.p2 = None # 
        self.p3 = None # 
        self.type = None # 


_once.imported['BezPoint']= BezPoint
for name, object in _once.imported.items():
    globals()[name]=object
