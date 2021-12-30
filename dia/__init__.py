
__doc__="""The dia module allows to write Python plug-ins for
Dia [http://live.gnome.org/Dia/Python]  This modules
is designed to run Python scripts embedded in Dia. To
make your script accessible to Dia you have to put it
into $HOME/.dia/python and let it call one of the
register_*() functions. It is possible to write
import filters [register_import()] and export filters
[register_export()], as well as scripts to manipulate
existing diagrams or create new ones
[register_action()].  For stand-alone Python bindings
to Dia see
http://mail.gnome.org/archives/dia-list/2007-March/msg00092.html"""




try:
    from dia import * #To expose modules classes as atributes
    import dia.dia.dia as dia  # module.file.class to make dumpObj happy in python3!
except:
    #in python3, the next line
    # from dia.dia import *
    #is equivalent to 
    #from .dia import * # this includes dia but does not improve dumpObj output in python2
    #from .lib import * 
    from .dia import *
    
_dia=dia()
    
def active_display() :
    """ active_display() -> Display.  Delivers the
                        currently active display 'dia.Display' or None""" 
    global _dia
    return _dia.active_display()

def diagrams() :
    """diagrams() -> List of Diagram.  Returns the list of
                        currently open diagrams"""
    global _dia
    return _dia.diagrams()

def get_object_type(type) :
    """get_object_type(string: type) -> ObjectType.  From
                    a type name like "Standard - Line" return the
                    factory to create objects of that type, see:
                    DiaObjectType"""
    #global _dia
    return dia.get_object_type(type)

def group_create(objs) :
    """group_create(List of Object: objs) -> Object. 
                        Create a group containing the given list of
                        dia.Object(s)"""
    global _dia
    return _dia.group_create("Group", objs)

def load(filename) :
    """load(string: name) -> Diagram.  Loads a diagram
                        from the given filename"""
    global _dia
    return _dia.load(filename)

def message(type, msg) :
    """message(int: type, string: msg) -> None.  Popup a
                        dialog with given message"""
    global _dia
    _dia.message(type, msg)

def new(name) :
    """new(string: name) -> Diagram.  Create an empty
                        diagram"""
    global _dia
    return _dia.new(name)

def register_action(action, description, menupath, func) :
    """register_action(string: action, string:
                        description, string: menupath, Callback: func) ->
                        None.  Register a callback function which appears
                        in the menu. Depending on the menu path used during
                        registrationthe callback gets called with the
                        current DiaDiagramData object"""
    global _dia
    _dia.register_action(action, description, menupath, func)

def register_callback(description, menupath, func) :
    """register_callback(string: description, string:
                        menupath, Callback: func) -> None.  Register a
                        callback function which appears in the menu.
                        Depending on the menu path used during
                        registrationthe callback gets called with the
                        current DiaDiagramData object"""
    global _dia
    _dia.register_callback(description, menupath, func)
	
def register_export(name, extension, r) :
    """ register_export(string: name, string: extension,
                        Renderer: r) -> None.  Allows to register an export
                        filter written in Python. It needs to conform to
                        the DiaRenderer interface."""
    global _dia
    _dia.register_export(name, extension, r)

def register_import(name, extension, func) :
    """register_import(string: name, string: extension,
                        Callback: func) -> None.  Allows to register an
                        import filter written in Python, that is mainly a
                        callback function which fills thegiven
                        DiaDiagramData from the given filename"""
    global _dia
    _dia.register_import(name, extension, func)

def register_plugin(filename) :
    """register_plugin(string: filename) -> None. 
                        Registers a single plug-in given its filename, that
                        is load a dynamic module."""
    global _dia
    _dia.register_plugin(filename)

def registered_sheets() :
    """registered_sheets() -> List of registered sheets. 
                        A list of all registered sheets."""
    global _dia
    return _dia.registered_sheets()

def registered_types() :
    """registered_types() -> Dict of ObjectType indexed by
                        their name.  A dictionary of all registered object
                        factories, aka. DiaObjectType"""
    #global _dia
    return dia.registered_types()

def update_all() :
    """update_all() -> None.  Force an asynchronous update
                        of all existing diagram displays"""
    global _dia
    _dia.update_all()
