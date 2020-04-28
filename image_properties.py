# Recuperar os dados de uma imagem (PNG, JPG etc)
# Trevisolli, 28/04/2020
import os
import sys
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS

imagem = "C:\\Temp\\IMG_20200427_141417.jpg"
print("Nome Imagem: ", imagem)
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

exif = get_exif(imagem)
#print(exif)

def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled

# Retorna como um dicionário para melhor interpretação
# Retorna inclusive GPSInfo
labeled = get_labeled_exif(exif)
print(labeled)



#exif = {
#    PIL.ExifTags.TAGS[k]: v
#    for k, v in img._getexif().items()
#    if k in PIL.ExifTags.TAGS
#}

#for (tag,value) in Image.open(image)._getexif().iteritems():
#    print('%s = %s' % (TAGS.get(tag), value))