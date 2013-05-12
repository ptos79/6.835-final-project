'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_APPLE_vertex_array_object'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_APPLE_vertex_array_object',False)
_p.unpack_constants( """GL_VERTEX_ARRAY_BINDING_APPLE 0x85B5""", globals())
glget.addGLGetConstant( GL_VERTEX_ARRAY_BINDING_APPLE, (1,) )
@_f
@_p.types(None,_cs.GLuint)
def glBindVertexArrayAPPLE( array ):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteVertexArraysAPPLE( n,arrays ):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenVertexArraysAPPLE( n,arrays ):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsVertexArrayAPPLE( array ):pass


def glInitVertexArrayObjectAPPLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
