'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_geometry_shader4'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_geometry_shader4',False)
_p.unpack_constants( """GL_GEOMETRY_SHADER_EXT 0x8DD9
GL_MAX_GEOMETRY_VARYING_COMPONENTS_EXT 0x8DDD
GL_MAX_VERTEX_VARYING_COMPONENTS_EXT 0x8DDE
GL_MAX_VARYING_COMPONENTS_EXT 0x8B4B
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT 0x8DDF
GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT 0x8DE0
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT 0x8DE1""", globals())
glget.addGLGetConstant( GL_MAX_GEOMETRY_VARYING_COMPONENTS_EXT, (1,) )
glget.addGLGetConstant( GL_MAX_VERTEX_VARYING_COMPONENTS_EXT, (1,) )
glget.addGLGetConstant( GL_MAX_VARYING_COMPONENTS_EXT, (1,) )
glget.addGLGetConstant( GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT, (1,) )
glget.addGLGetConstant( GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT, (1,) )
glget.addGLGetConstant( GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT, (1,) )
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint)
def glProgramParameteriEXT( program,pname,value ):pass


def glInitGeometryShader4EXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
