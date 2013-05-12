'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_EXT_framebuffer_sRGB'
_p.unpack_constants( """GL_FRAMEBUFFER_SRGB_EXT 0x8DB9
GL_FRAMEBUFFER_SRGB_CAPABLE_EXT 0x8DBA""", globals())


def glInitFramebufferSrgbEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
