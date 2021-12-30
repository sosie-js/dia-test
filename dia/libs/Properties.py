"""
  pydia: Properties.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Properties']=None
if not 'Property' in _once.imported.keys() :
    from dia.libs.Property import Property


class Properties(dict):
    """Class Properties
    A dictionary interface to dia.Object's standard properties.
    Many propertiescan be get and set through this. If there is a specific method
    to change anobjects property like o.move() or o.move_handle() use that instead.   """

    # Attributes:
    
    # Operations
    
    def __init__(self, props, *args):
        dict.__init__(self, args) #I wonder if we really need this
        for prop in props.values():
            name = prop["name"] 
            type = prop["type"]
            value = prop["value"]
            visible = prop["visible"]
            self.__dict__[name] =Property(name, type, value, visible)
            
    def __setitem__(self, name, type, value, visible):
        prop = Property(name, type, value, visible)
        self.__dict__[key] = prop #item

    def __getitem__(self, key):
        #Make object subscritable ie if 'properties' is an instance of Properties
        #make properties[key] possible, equivalent in our case to properties.get(key)"""
        return self.__dict__[key]
        
    def get (self, key) :
        """get(key: str) -> Property
        returns the property matching the key """
        val = self[key] 
        return val

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        """has_key(key: str) -> bool
        returns True if a property matching the key exists else False
        """
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        """keys() -> list of str
        Get the list of property names
        """
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __unicode__(self):
        return unicode(repr(self.__dict__))


_once.imported['Properties']= Properties
for name, object in _once.imported.items():
    globals()[name]=object

"""
foo={"n1":{"name":"n1","type":"t1","value":"v1","visible":"d1"}}
bar=Properties(foo)
print(bar.keys())
print("--")
print(bar.has_key("n1"))
print(bar.get("n1"))
"""