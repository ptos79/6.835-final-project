'''OpenGL extension NV.texture_barrier

This module customises the behaviour of the 
OpenGL.raw.GL.NV.texture_barrier to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension relaxes the restrictions on rendering to a currently
	bound texture and provides a mechanism to avoid read-after-write
	hazards.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/texture_barrier.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.NV.texture_barrier import *
### END AUTOGENERATED SECTION