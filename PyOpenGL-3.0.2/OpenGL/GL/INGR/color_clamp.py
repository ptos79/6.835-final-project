'''OpenGL extension INGR.color_clamp

This module customises the behaviour of the 
OpenGL.raw.GL.INGR.color_clamp to provide a more 
Python-friendly API

Overview (from the spec)
	
	Various RGBA color space conversions require clamping to values
	in a more constrained range than [0, 1].  This extension allows
	the definition of independent color clamp values for each of the
	four color components as part of the Final Conversion in the pixel
	transfer path for draws, reads, and copies.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/INGR/color_clamp.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.INGR.color_clamp import *
### END AUTOGENERATED SECTION