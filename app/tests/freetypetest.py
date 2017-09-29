import freetype

face = freetype.Face('Roboto/Roboto-Regular.ttf')
face.set_char_size(48*64)
face.load_char('e')
bitmap = face.glyph.bitmap
print(bitmap.width)
print(bitmap.rows)