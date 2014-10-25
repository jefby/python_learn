#!/usr/bin/env python
# -*- coding: utf-8 -*-

#first string will be as module document comment
' a handle image module '
#module author
__author__ = 'jefby'

import Image
im=Image.open('yuri.jpg')
print im.format,im.size,im.mode
im.thumbnail((200,100))
im.save('thumb.jpg','JPEG')
