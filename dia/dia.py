"""
  pydia: dia.py - 2021.12
  ================================================
  
  Template code initially generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""

import warnings
try:
    import cPickle as pickle
except:
    import _pickle as pickle #cPickle uses _pickle in python3
    


def install_shared_module(step ='create'):
    """ Create or init the _once.py that will serve as a shared memory between modules"""
    
    if step == 'init':
        
        import io, json, os
        
        base = os.path.abspath(os.path.dirname(__file__))
        
        #version='0.97.3+git20160930-8.1'   #2016 - apt,python2, 830 types
        version='0_97_0-2406-gaa4e99118+' #2021 - git,python3, 1295 types
        
        ## Load core files generated with core/diacoredump.py under dia

        # Load sheets definitions 
        
        with io.open(os.path.join(base, "core", version, "sheets.json"),"r") as fp:
            js=fp.read()
            
        _once.registered["sheets"]=json.loads(js)
        
        # Load registered types 
        
        with io.open(os.path.join(base,"core", version, "registered_types.json"),"r") as fp:
            js=fp.read()
        
        _once.registered["types"] = json.loads(js)
         
        #import web_pdb; web_pdb.set_trace()
         
        #print("REGISTRATION DONE")
         
    else: #create
        
        try:
            with open("_once.py", 'w') as outfile:
                outfile.write("#Class holder containing imports to prevent circular imports\n")
                outfile.write("imported={}\n")
                outfile.write("diagram=None\n")
                outfile.write("registered={}\n")
                outfile.write("registered['types']=None\n")
                outfile.write("registered['sheets']=None\n")
        except:
            raise(Exception("dia:install_shared_module() can not write in the current directory , Crash!"))

#Beware not to use simply "import _once", it is not python2-3 universal
#we have to use an other strategy in three steps
#to have a shared module with libs/ modules 
install_shared_module('create')
from . import _once
install_shared_module('init')

#imported will be the shared dict classname -> class used by the loader
#so we can split into module files matching classes name into libs/
_once.imported['dia']=None


import sys
python2 = (sys.version_info[0] == 2)

if python2 :
    
    if not 'Display' in _once.imported.keys() :
        from .libs.Display import Display
    if not 'ObjectType' in _once.imported.keys() :
        from .libs.ObjectType import ObjectType
    if not 'Sheet' in _once.imported.keys() :
        from .libs.Sheet import Sheet
    if not 'Diagram' in _once.imported.keys() :
        from .libs.Diagram import Diagram

else:
    
    if not 'Display' in _once.imported.keys() :
        from dia.libs.Display import Display
    if not 'ObjectType' in _once.imported.keys() :
        from dia.libs.ObjectType import ObjectType
    if not 'Sheet' in _once.imported.keys() :
        from dia.libs.Sheet import Sheet
    if not 'Diagram' in _once.imported.keys() :
        from dia.libs.Diagram import Diagram


class dia:
    '''The dia module allows to write Python plug-ins for Dia [http://live.gnome.org/Dia/Python]

This modules is designed to run Python scripts embedded in Dia. To make your script accessible
to Dia you have to put it into $HOME/.dia/python and let it call one of the register_*() functions.
It is possible to write import filters [register_import()] and export filters [register_export()], as well as scripts to manipulate existing diagrams or create new ones [register_action()].

For stand-alone Python bindings to Dia see http://mail.gnome.org/archives/dia-list/2007-March/msg00092.html'''
    
    # Attributes:
    _active_display = None
    _diagrams = []
    _actions = {}
    _callbacks = {}
    _import = {}
    _export = {}
    _plugins = []
    _sheets = []
    _registered_types = {}
        
    # Operations
    
    def __init__(self):
        
        dia._sheets = _once.registered["sheets"]
        
        registered_types= {}
        for type , type_def in _once.registered["types"].items():
            name = type_def["name"] #matches type
            version = type_def["version"]
            registered_types[type]=ObjectType(name,version)
        
        dia._registered_types = registered_types
        
        #print("DIA REGISTERED")

    def active_display(self):
        """ active_display() -> Display.  Delivers the currently active display 'dia.Display' or None"""
        if not self._active_display :
            if(len(self._diagrams) == 0):
                diagram=self.new("Diagram1.dia")
                data=diagram.data
                layer=data.add_layer("Background")
                data.set_active_layer(layer)
                self._active_display = diagram.display()
            elif self._diagrams[0] : 
                self._active_display = self._diagrams[0].display() #normaly Diagram active
        return self._active_display

    def diagrams(self):
        """ diagrams() -> List of Diagram.  Returns the list of currently open diagrams """
        return self._diagrams
    
    @staticmethod
    def get_object_type (type) :
        """ get_object_type(string: type) -> ObjectType.  From a type name like "Standard - Line" return the factory to create objects of that type, see: DiaObjectType """

        otypes=dia.registered_types()
        
        #print("DIA.GET_OBJECT_TYPE("+type+")")
        
        if type in  otypes.keys():
            otype=ObjectType(type)
            otype.version= otypes[type].version
        else :
            raise("Unregistered Object Type '"+type+"'")
       
        return otype 
    
    def group_create (self, objs) :
        """ group_create(List of Object: objs) -> Object.  Create a group containing the given list of dia.Object(s) """
        return Object("Group", objs)
    
    def load (self, filename) :
        """ load(string: name) -> Diagram.  Loads a diagram from the given filename """
        diagram = pickle.load(open(filename, "rb"))
        self._diagrams.append(diagram)
        return self._diagrams[len(self._diagrams)-1]
    
    def message (self, type, msg) :
        """ message(int: type, string: msg) -> None.  Popup a dialog with given message """
        if type == 2 :
            warnings.error(msg)
        else :
            warnings.warn(msg)
            
    def new(self, name):
        """ new(string: name) -> Diagram.  Create an empty diagram """
       
        diagram = Diagram(name)
        self._diagrams.append(diagram)
        return diagram
    
    def register_action (self, action, description, menupath, func) :
        """ register_action(string: action, string: description, string: menupath, Callback: func) -> None.  Register a callback function which appears in the menu. Depending on the menu path used during registrationthe callback gets called with the current DiaDiagramData object """
        self._actions[action] = [(description, menupath, func)]
        
    def register_callback (self, description, menupath, func) :
        """ register_callback(string: description, string: menupath, Callback: func) -> None.  Register a callback function which appears in the menu. Depending on the menu path used during registrationthe callback gets called with the current DiaDiagramData object """
        self._callbacks[description] = [(menupath, func)]

    def register_export (self, name, extension, r) :
        """ register_export(string: name, string: extension, Renderer: r) -> None.  Allows to register an export filter written in Python. It needs to conform to the DiaRenderer interface. """
        self._export[name] = [(extension, r)]

    def register_import (self, name, extension, func) :
        """ register_import(string: name, string: extension, Callback: func) -> None.  Allows to register an import filter written in Python, that is mainly a callback function which fills thegiven DiaDiagramData from the given filename """
        self._import[name] = [(extension, func)]

    def register_plugin (self, filename) :
        """ register_plugin(string: filename) -> None.  Registers a single plug-in given its filename, that is load a dynamic module. """
        self._plugins.append(filename)

    def registered_sheets (self) :
        """ registered_sheets() -> List of registered sheets.  A list of all registered sheets. """
        return self._sheets
        
    @staticmethod
    def registered_types () :
        """ registered_types() -> Dict of ObjectType indexed by their name.  A dictionary of all registered object factories, aka. DiaObjectType """
        return dia._registered_types
    
    def update_all (self) :
        """ update_all() -> None.  Force an asynchronous update of all existing diagram displays """
        for diagram in self._diagrams :
            diagram.flush()
    
#dia=dia()

_once.imported['dia']= dia

for name, object in _once.imported.items():
    globals()[name]=object
