'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_SGIX_fog_scale'
_p.unpack_constants( """GL_FOG_SCALE_SGIX 0x81FC
GL_FOG_SCALE_VALUE_SGIX 0x81FD""", globals())


def glInitFogScaleSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
