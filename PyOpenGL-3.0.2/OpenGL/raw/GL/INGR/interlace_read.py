'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_INGR_interlace_read'
_p.unpack_constants( """GL_INTERLACE_READ_INGR 0x8568""", globals())
glget.addGLGetConstant( GL_INTERLACE_READ_INGR, (1,) )


def glInitInterlaceReadINGR():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
