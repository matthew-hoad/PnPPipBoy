from glob import glob 
from os.path import dirname, join, basename
from kivy.core.text import Label
from kivy.core.text import LabelBase


from kivy.core.text import LabelBase
KIVY_FONTS = [
    {
        "name": "unispace",
        "fn_regular": "data/fonts/unispace-rg.ttf",
        "fn_bold": "data/fonts/unispace-bd.ttf",
        "fn_italic": "data/fonts/unispace-it.ttf",
        "fn_bolditalic": "data/fonts/unispace-bd-it.ttf"
    }
]
    
for font in KIVY_FONTS:
    LabelBase.register(**font)

KIVY_DEFAULT_FONT='unispace'