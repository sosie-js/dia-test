"""
  pydia: DiagramData.py - 2022.01
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""

import _once
_once.imported['DiagramData']=None
if not 'Color' in _once.imported.keys() :
    from dia.libs.Color import Color
if not 'Rectangle' in _once.imported.keys() :
    from dia.libs.Rectangle import Rectangle
if not 'Object' in _once.imported.keys() :
    from dia.libs.Object import Object
if not 'Paperinfo' in _once.imported.keys() :
    from dia.libs.Paperinfo import Paperinfo
#if not 'Display' in _once.imported.keys() :
#    from dia.libs.Display import Display
    
import sys
python2 = (sys.version_info[0] == 2)    
    
class DiagramData :
    '''
    The 'low level' diagram object. It contains everything to manipulate diagrams
    from im- and export filters as well as from the UI. It does not provide any access
    to GUI elements related to the diagram.Use the subclass dia.Diagram object for such matters.
    '''

    # Attributes:
    
    active_layer = None  # () Layer currently active in the diagram. 
    bg_color = None  # () Color of the diagram's background. 
    extents = None  # () Rectangle covering all object's bounding boxes. 
    grid_visible = None  # () bool: visibility of the grid. 
    grid_width = None  # () Tuple(real: x, real: y) : describing the grid size. 
    hguides = None  # () List of real: horizontal guides. 
    layers = None  # () Read-only list of the diagrams layers. 
    paper = None  # () Paperinfo of the diagram. 
    selected = None  # () List of Object: current selection. 
    vguides = None  # () List of real: vertical guides. 

    # Operations
    
    def __init__(self) :
        self.active_layer = None # 
        self.bg_color = None # 
        self.extents = None # 
        self.grid_visible = None # 
        self.grid_width = None # 
        self.hguides = None # 
        self.layers = [] # 
        self.paper = Paperinfo() # 
        self.selected = None # 
        self.vguides = None # 
        #self._signals = {}

    def add_layer(self, layer, position = 0) :
        """ add_layer(Layer: layer[, int: position]) -> Layer.  Add a layer to the diagram at the top or the given position counting from bottom. """
        self.layers.insert(position, Layer(layer))
        return self.layers[position]
        
    def connect_after (self, signal_name, callback) :
        """ connect_after(string: signal_name, Callback: func) -> None.  Listen to diagram events in ['object_add', 'object_remove']. """
        #self._signals[signal_name] = callback
        pass
        
    def delete_layer (self, layer) :
        """ delete_layer(Layer: layer) -> None.  Remove the given layer from the diagram. """
        self.layers.remove(layer)
        
    def get_sorted_selected (self) :
        """ get_sorted_selected() -> list.  Return the current selection sorted by Z-Order. """
        # returns 
        pass

    def lower_layer (self) :
        """ lower_layer() -> None.  Move the layer towards the bottom. """
        # returns 
        pass

    def raise_layer (self) :
        """ raise_layer() -> None.  Move the layer towards the top. """
        # returns 
        pass
        
    def set_active_layer (self, layer) :
        """ set_active_layer(Layer: layer) -> None.  Make the given layer the active one. """
        self.active_layer = layer

    def update_extents (self) :
        """ update_extents() -> None.  Recalculation of the diagram extents. """
        min_x = None 
        min_y = None
        max_x = None 
        max_y = None
        
        for layer in self.layers :
            
            items=layer.extents
            left=items.left
            top=items.top
            right=items.right
            bottom=items.bottom
            
            # "h: %g w: %g" % (bb.bottom - bb.top, bb.right - bb.left)
            #print(bb.left, bb.top, bb.right, bb.bottom)
            items=[(left, top),(right, bottom)]

            for item in items:
                
                if min_x is None or item[0] < min_x :
                  min_x = item[0]

                if max_x is None or item[0] > max_x:
                  max_x = item[0]

                if min_y is None  or item[1] < min_y:
                  min_y = item[1]

                if max_y is None  or item[1] > max_y:
                  max_y = item[1]

        class Lists (list):

            def __init__(self,left,top,right,bottom):
                self.thelist=[None,None,None,None]
                self.left = left
                self.top = top
                self.right = right
                self.bottom = bottom
            
            def __setattr__(self, name, value):
                if python2:
                    super(list, self).__setattr__(name, value)
                else:
                    # in python3+ you can omit the arguments to super:
                    super().__setattr__(name, value) 
                
                if name == 'left':   
                    self.thelist[0]=value
                if name == 'top':   
                    self.thelist[1]=value
                if name == 'right':   
                    self.thelist[2]=value
                if name == 'bottom':   
                    self.thelist[3]=value
                
            def __getitem__(self, index):
                return self.thelist[index]

            def __setitem__(self, index, value):
                self.thelist[index] = value

            def __repr__(self):
                return repr(thelist)
        
        
        self.extents = Lists(min_x, min_y,max_y,max_y)

            

_once.imported['DiagramData']= DiagramData
for name, object in _once.imported.items():
    globals()[name]=object
