"""
  pydia: Diagram.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Diagram']=None

if not 'DiagramData' in _once.imported.keys() :
    from dia.libs.DiagramData import DiagramData
if not 'Layer' in _once.imported.keys() :
    from dia.libs.Layer import Layer
if not 'Display' in _once.imported.keys() :
    from dia.libs.Display import Display

class Diagram :
    '''Subclass of dia.DiagramData (at least in the C implementation) adding interfacing the GUI elements.'''

    # Attributes:
    
    data = None  # () Backward-compatible base-class access 
    displays = None  # () The list of current displays of this diagram. 
    filename = None  # () Filename in utf-8 encoding. 
    modified = None  # () Modification state. 
    selected = None  # () The current object selection. 
    unsaved = None  # () True if the diagram was not saved yet. 

    # Operations

    def __init__(self, filename) :
        self.data = DiagramData() # 
        self.displays = [] # 
        self.filename = filename 
        self.modified = None # 
        self.selected = None
        #self._signals = {}

    def add_update (self, top, left, bottom, right) :
        """ add_update(real: top, real: left, real: bottom, real: right) -> None.  Add the given rectangle to the update queue. """
        # returns 
        pass

    def add_update_all (self) :
        """ add_update_all() -> None.  Add the diagram visible area to the update queue. """
        # returns 
        pass

    def connect_after (self, signal_name, callback) :
        """ connect_after(string: signal_name, Callback: func) -> None.  Listen to diagram events in ['removed', 'selection_changed']. """
        #self._signals[signal_name] = callback
        pass

    def display (self) :
        """ display() -> Display.  Create a new display of the diagram. """
        new_display = Display(self)
        self.displays.append(new_display)
        return new_display

    def find_clicked_object (self) :
        """ find_clicked_object(real[2]: point, real: distance) -> Object.  Find an object in the given distance of the given point. """
        # returns 
        pass
        
    def find_closest_connectionpoint (self, x, y, obj = None) :
        """ find_closest_connectionpoint(real: x, real: y[, Object: o]) -> (real: dist, ConnectionPoint: cp).  Given a point and an optional object to exclude, return the distance and closest connection point or None. """
        # returns 
        pass

    def find_closest_handle (self, point) :
        """ find_closest_handle(real[2]: point) -> (real: distance, Handle: h, Object: o).  Find the closest handle from point and return a tuple of the search results.  Handle and Object might be None. """
        # returns 
        pass

    def flush (self) :
        """ flush() -> None.  If no display update is queued, queue update. """
        pass

    def get_sorted_selected (self) :
        """ get_sorted_selected() -> list.  Return the current selection sorted by Z-Order. """
        # returns 
        pass

    def get_sorted_selected_remove (self) :
        """ get_sorted_selected_remove() -> list.  Return sorted selection and remove it from the diagram. """
        # returns 
        pass
        
    def group_selected (self) :
        """ group_selected() -> None.  Turn the current selection into a group object. """
        pass

    def is_selected (self, obj) :
        """ is_selected(Object: o) -> bool.  True if the given object is already selected. """
        # returns 
        pass

    def remove_all_selected (self) :
        """ remove_all_selected() -> None.  Delete all selected objects. """
        pass
        
    def save (self, filename) :
        """ save(string: filename) -> None.  Save the diagram under the given filename. """
        pickle.dump(self, open(filename, "wb"))

    def select (self, obj) :
        """ select(Object: o) -> None.  Add the given object to the selection. """
        pass

    def ungroup_selected (self) :
        """ ungroup_selected() -> None.  Split all groups in the current selection into single objects. """
        pass

    def unselect (self, obj) :
        """ unselect(Object: o) -> None.  Remove the given object from the selection) """
        pass

    def update_connections (self, obj) :
        """ update_connections(Object: o) -> None.  Update all connections of the given object. Might move connected objects. """
        pass

    def update_extents (self) :
        """ update_extents() -> None.  Force recaculation of the diagram extents. """
        pass


_once.imported['Diagram']= Diagram
for name, object in _once.imported.items():
    globals()[name]=object
