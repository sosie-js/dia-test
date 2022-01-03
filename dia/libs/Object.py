"""
  pydia: Object.py - 2022.01
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Object']=None
if not 'Layer' in _once.imported.keys() :
    from dia.libs.Layer import Layer
if not 'Properties' in _once.imported.keys() :
    from dia.libs.Properties import Properties
if not 'ConnectionPoint' in _once.imported.keys() :
    from dia.libs.ConnectionPoint import ConnectionPoint
if not 'Handle' in _once.imported.keys() :
    from dia.libs.Handle import Handle
if not 'Menuitem' in _once.imported.keys() :
    from dia.libs.Menuitem import Menuitem


class Object:
    """Class Object
The main building block of diagrams.    """

    # Attributes:
    
    bounding_box = None  # () Box covering all the object. 
    connections = None  # () Vector of connection points. 
    handles = None  # () Vector of handles. 
    parent = None  # () The parent object when parenting is in place, None otherwise. 
    properties = None  # () Dictionary of object properties. 
    
    # Operations

    def __init__(self, type, *args) :
        
        self.connections = [ConnectionPoint(self) for _ in range(8)]
        self.handles = [Handle(self) for _ in range(8)] 
        self.parent = None # 
        
        
        
        #import the default properties from the registered types
        # print('Creating Object "'+type.name+'" with default properties')
        
        #! NOTE registered_types=dia.registered_types() does not work
        # as dia class is not yet declared, we have to use our special registration...
        
        from .._once import registered
        
        if registered["types"] is None:
            raise(Exception("No type registered, this sucks!")) 
            
        registered_types= registered["types"]


        if type.name in registered_types.keys() :
            #...so we can retrieve the default properties values
            props=registered_types[type.name]["properties"]
            #..as if we have instantiated the object
            self.properties = Properties(props)        
        else:
            print("Cannot retrieve Object type '"+type.name+"' from defs ",registered_types.keys())
            self.properties = Properties(self)
            self.properties["elem_width"] = 20
            self.properties["elem_height"] = 20
        
        self.bounding_box = self.properties["obj_bb"] # 
        self.type = type #extra?

    def add_property(self, key, value) :
        if key in ('attributes','operations') :
            end = self.connections.pop()
            for _ in range(len(value.value)*2) :
                self.connections.append(ConnectionPoint(self))
            self.connections.append(end)

    def copy(self):
        """ copy() -> Object.  Create a new object copy. """
        pass

    def destroy (self) :
        """ destroy() -> None.  Release the object. Must not be called when already added to a group or layer. """
        # returns 
        pass

    def distance_from (self) :
        """ distance_from(real: x, real: y) -> real.  Calculate the object's distance from the given point. """
        # returns 
        pass

    def draw (self, renderer) :
        """ draw(dia.Renderer: r) -> None.  Draw the object with the given renderer """
        pass

    def get_object_menu (self) :
        """ get_object_menu() -> Tuple.  Returns a named list of Menuitem(s). """
        # returns 
        pass

    def move(self, x, y):
        """ move(real: x, real: y) -> None.  Move the entire object. The given point is the new object.obj_pos. """
        c=Point(x,y)
        #Matches the getter "elem_corner"
        self.properties["obj_pos"].value=str(c) #[c.x, c.y]
        
    
    def move_handle(self, h, pos):
        """ move_handle(Handle: h, (real: x, real: y)[int: reason, int: modifiers]) -> None.  Move the given handle of the object to the given position """
        # returns 
        pass


_once.imported['Object']= Object

#if not 'ObjectType' in _once.imported.keys() :
#    from dia.libs.ObjectType import ObjectType

for name, object in _once.imported.items():
    globals()[name]=object
