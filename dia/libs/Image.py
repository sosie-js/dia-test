"""
  pydia: Image.py - 2021.11
  ================================================
  
  Template code generated from UML diagrams of PyDia
  with   'dia2code -t python ../dia2code/PyDiaObjects.dia' 
  
  Note: Experimental, will be obsolete if we found a way to use libdia /pydia libraries
  Author: SoSie@sos-productions.com
  License: LGPL
"""


import _once
_once.imported['Image']=None

class Image:
    """Class Image
dia.Image gets passed into DiaRenderer.draw_image    """
    
    # Attributes:
    
    filename = None  # () string: utf-8 encoded filename of the image 
    height = None  # () int: pixel height of the image 
    mask_data = None  # () string: array of alpha pixel values 
    rgb_data = None  # () string: array of packed rgb pixel values 
    uri = None  # () string: Uniform Resource Identifier of the image 
    width = None  # () int: pixel width of the image 
    
    # Operations
    
    def __init__(self) :
        self.filename = None # 
        self.height = None # 
        self.mask_data = None # 
        self.rgb_data = None # 
        self.uri = None # 
        self.width = None # 
        pass


_once.imported['Image']= Image
for name, object in _once.imported.items():
    globals()[name]=object
