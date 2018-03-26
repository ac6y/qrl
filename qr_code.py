#!/usr/bin/env python
# just for fun 
# ac6y 2018-03-25

import qrcode
from base64 import b64encode

from cStringIO import StringIO
import webbrowser

def str_to_qrl(s):
    """
    converts a string s to a qrcode png image, which is
    encoded as a data url and returned
    as a string
    """
    buff = StringIO()
    im = qrcode.make(data=s)
    im.save(buff, format='png')
    b64 = b64encode(buff.getvalue())
    url = 'data:image/png;base64,{}'.format(b64)
    return url

webbrowser.open(str_to_qrl('ac6y'))
