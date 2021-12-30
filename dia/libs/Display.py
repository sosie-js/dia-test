"""
  pydia:Display .py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Display']=None


class Display :
    '''A Diagram can have multiple displays but every Display has just one Diagram.'''

    # Attributes:

    diagram = None  # () Diagram displayed. 
    origin = None  # () Point in diagram coordinates of the top-left corner of the visible area. 
    visible = None  # () Tuple(real: top, real: left, real: bottom, real: right) : visible area 
    zoom_factor = None  # () Real: zoom-factor 

    # Operations

    def __init__(self, diagram) :
        self.diagram = diagram 
        self.origin = None # 
        self.visible = None # 
        self.zoom_factor = None # 

    def add_update_all (self) :
        """ add_update_all() -> None.  Add the diagram visible area to the update queue. """
        pass

    def close (self) :
        """ close() -> None.  Close the display possibly asking to save. """
        pass

    def flush (self) :
        """ flush() -> None.  If no display update is queued, queue update. """
        pass

    def resize_canvas (self, width, height) :
        """ resize_canvas(int: width, int: height) -> None.  BEWARE: Changing the drawing area but not the window size. """
        pass
        
    def scroll (self, dx, dy) :
        """ scroll(real: dx, real: dy) -> None.  Scroll the visible area by the given delta. """
        pass

    def scroll_down (self) :
        """ scroll_down() -> None. Scroll downwards by a fixed amount. """
        pass

    def scroll_left (self) :
        """ scroll_left() -> None. Scroll to the left by a fixed amount. """
        pass

    def scroll_right (self) :
        """ scroll_right() -> None. Scroll to the right by a fixed amount. """
        pass

    def scroll_up (self) :
        """ scroll_up() -> None. Scroll upwards by a fixed amount. """
        pass

    def set_origion (self, x, y) :
        """ set_origion(real: x, real, y) -> None.  Move the given diagram point to the top-left corner of the visible area. """
        # returns 
        pass
        
    def set_title (self, title) :
        """ set_title(string: title) -> None.  Temporary change of the diagram title. """
        pass

    def zoom (self, point, factor) :
        """ zoom(real[2]: point, real: factor) -> None.  Zoom around the given point. """
        # returns 
        pass

_once.imported['Display']= Display

if not 'Diagram' in _once.imported.keys() :
    try:
        from dia.libs.Diagram import Diagram
    except:
        from .Diagram import Diagram

for name, object in _once.imported.items():
    globals()[name]=object
