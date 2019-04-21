#!/usr/bin/env python3

import os, sys
import PIL
from PIL import Image

size = 360, 247

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            parent = os.path.join(os.pardir,'thumbs')
            im.save(os.path.join(parent,outfile), "JPEG")
            print ("Saved in: " + parent)
        except IOError:
            print ("cannot create thumbnail for '%s'" % infile)
            
