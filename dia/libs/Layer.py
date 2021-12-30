"""
  pydia: Layer.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Layer']=None
if not 'DiagramData' in _once.imported.keys() :
    from dia.libs.DiagramData import DiagramData


class Layer :
    '''A Layer is part of a Diagram and can contain objects.'''

    # Attributes:

    extents = None  # () Rectangle covering all object's bounding boxes. 
    name = None  # () The name of the layer. 
    objects = None  # () The list of objects in the layer. 
    visible = None  # () The visibility of the layer. 

    # Operations

    def __init__(self, name) :
        self.extents = None # 
        self.name = name
        self.objects = [] # 
        self.visible = 1 # 

    def add_object (self, o,position=-1) :
        """ add_object(Object: o[, int: position]) -> None.  Add the object to the layer at the top or the given position counting from bottom. """
        if position == -1 : 
            self.objects.append(o)
        else:
            self.objects.insert(position, o)

    def destroy (self) :
        """ Release the layer. Must not be called when already added to a diagram. """
        pass

    def find_closest_connection_point (self, x, y, obj = None) :
        """ find_closest_connectionpoint(real: x, real: y[, Object: o]) -> (real: dist, ConnectionPoint: cp).  Given a point and an optional object to exclude return the distance and the closest connection point or None. """
        #(real: dist, ConnectionPoint: cp)
        pass

    def find_closest_object (self, x, y, maxdist) :
        """ find_closest_object(real: x, real: y, real: maxdist) -> Object.  Find an object in the given maximum distance of the given point. """
        pass

    def find_objects_in_rectangle (self, top, left, bottom, right) :
        """ find_objects_in_rectangle(real: top, real left, real: bottom, real: right) -> Objects  Returns a list of objects found in the given rectangle. """
        pass

    def object_get_index (self, obj) :
        """ object_get_index(Object: o) -> int.  Returns the index of the object in the layers list of objects. """
        return self.objects.index(obj)

    def remove_object (self, obj) :
        """ remove_object(Object: o) -> None  Remove the object from the layer and delete it. """
        self.objects.remove(obj)
        del obj

    def render (self, r) :
        """ render(dia.Renderer: r) -> None.  Render the layer with the given renderer """
        pass

    def update_extents (self) :
        """ update_extents() -> None.  Force recaculation of the layer extents. """
        pass


_once.imported['Layer']= Layer
for name, object in _once.imported.items():
    globals()[name]=object
