#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""HTML2eBook a tiny function that converts HTML5 to eBook,Mobile Friendly."""


import os
import zipfile
import codecs
from getpass import getuser
from datetime import datetime
from uuid import uuid4
import base64
import binascii
import zlib


def stealth_to_string(stringy: str, rot13: bool=False) -> str:
    """Stealth to string,stealth is a hidden string,both str type and utf-8."""
    def __i2b(integ):  # int to bytes, do not touch.
        """Helper for string_to_stealth and stealth_to_string, dont touch!."""
        __num = len("%x" % integ)
        return binascii.unhexlify(str("%x" % integ).zfill(__num + (__num & 1)))
    _n = int(str(stringy).replace(u"\u200B", "0").replace(u"\uFEFF", "1"), 2)
    stringy = zlib.decompress(base64.b64decode(__i2b(_n))).decode('utf-8')
    stringy = codecs.decode(stringy, "rot-13") if rot13 and codecs else stringy
    return str(stringy).strip()


##############################################################################


CONTAINER = stealth_to_string("​﻿﻿​​﻿​﻿​﻿​​﻿﻿﻿​​﻿﻿﻿​​​​​﻿﻿​​﻿​​​﻿﻿​﻿​﻿​​﻿﻿﻿​​﻿​​﻿​​​﻿﻿​​﻿​﻿​​﻿﻿​﻿﻿﻿﻿​​​​﻿​​​﻿​​​﻿​​​​​﻿​﻿​​﻿﻿​﻿​﻿​﻿​​﻿​​﻿​﻿​​​​​﻿﻿﻿​﻿​​​​﻿﻿﻿​​​​﻿﻿​﻿​​​​﻿​﻿﻿​​​​﻿​​​﻿​﻿​﻿​​﻿﻿​​​﻿﻿​﻿​﻿​​﻿﻿﻿​​​﻿​﻿​​​﻿﻿​​﻿﻿​﻿​﻿​​﻿​﻿​​​​​﻿​​​﻿​﻿​﻿﻿​﻿﻿​﻿​﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​​﻿​​﻿​﻿﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿​​​​﻿​​﻿﻿﻿﻿​​​​﻿﻿​​​﻿​​﻿​​﻿﻿﻿﻿​﻿​﻿​﻿﻿​​﻿﻿​﻿​​﻿​﻿﻿​​​﻿﻿​﻿​​​​﻿﻿​﻿​﻿​​﻿﻿​﻿​﻿​​​​​﻿﻿﻿​​﻿​​﻿​﻿​​​﻿​﻿​​​﻿​​​​﻿﻿​﻿​﻿​﻿﻿​​﻿​﻿​​﻿﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿​​﻿﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿​﻿​﻿﻿﻿​​﻿﻿​​​​​﻿﻿​﻿﻿​​​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿​​​​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​﻿​​​​﻿﻿​​​﻿​﻿﻿﻿﻿​​​​﻿​​﻿﻿​​​﻿​​​﻿﻿​​﻿​​​​﻿​​​﻿​﻿​﻿﻿​﻿​﻿​​​﻿​﻿​﻿​​﻿﻿​﻿​​​​﻿﻿​﻿​​﻿​​​​﻿﻿﻿​﻿﻿​​​﻿﻿​﻿​﻿​​﻿﻿​​​﻿​﻿​​​﻿​​​​﻿﻿​﻿​﻿​﻿​​﻿​﻿﻿​﻿​​​​​﻿​﻿﻿​​﻿​﻿​﻿﻿​﻿​﻿​​﻿​​﻿​​﻿​﻿​​​​﻿​​​﻿﻿​﻿﻿﻿​﻿﻿﻿﻿​﻿​​​﻿﻿​​﻿​​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿​​﻿​​﻿​﻿​​﻿​﻿​​​​​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿​​​﻿​﻿​​﻿​​​﻿﻿​​﻿​​﻿​​﻿​﻿﻿​﻿​​﻿​﻿﻿​​﻿﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​﻿​​﻿​​​​﻿​​​﻿﻿​﻿﻿​​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿​​​﻿﻿﻿​﻿​﻿​​﻿​​﻿﻿﻿​​​​​​﻿﻿​﻿﻿​​﻿​​﻿​​​​﻿﻿﻿​​​​​﻿​​﻿​​​​﻿​​​​﻿﻿​﻿​​﻿​​​​﻿﻿​​​﻿​​﻿﻿​​﻿﻿﻿​﻿​​﻿​﻿​​﻿​​​﻿​​​​﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿​​​﻿​﻿​﻿​﻿​﻿​​﻿﻿﻿﻿​﻿​﻿​​﻿﻿​﻿﻿﻿﻿​​﻿​﻿​﻿​﻿​﻿​﻿﻿﻿﻿​﻿​​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿​​﻿​​﻿​​﻿​﻿﻿​﻿﻿​​​﻿​​​﻿﻿​​﻿​​﻿​​﻿​﻿​​﻿﻿﻿​​​﻿﻿​​﻿​​﻿﻿​​﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿​​﻿﻿​​​﻿​﻿﻿​​﻿​﻿​​​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​​​﻿​﻿​​​​​﻿​﻿﻿​﻿﻿﻿​​﻿﻿﻿​﻿​​​﻿﻿﻿﻿​​﻿​​﻿﻿​﻿﻿​​﻿​​​​​﻿​﻿​​﻿﻿​​​﻿​​﻿​​﻿​​﻿﻿​﻿​﻿​​﻿﻿​​﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿​​﻿﻿﻿​​﻿​﻿​​﻿​​﻿​​​​​﻿​​﻿﻿​﻿​﻿​﻿​​﻿﻿﻿​​﻿​​﻿​​﻿​​﻿​﻿​﻿﻿​﻿﻿﻿​​​​​​﻿﻿​​​​​﻿﻿​﻿﻿​﻿​﻿​﻿﻿​​﻿​﻿﻿​﻿​​﻿​﻿﻿​﻿﻿﻿​​﻿​​​﻿​﻿​﻿​​﻿​﻿﻿​﻿​​​﻿​﻿​﻿​​﻿﻿​﻿​﻿﻿​﻿​​​​​﻿​﻿﻿﻿﻿​​﻿﻿​﻿﻿​​﻿﻿﻿﻿​﻿​​﻿​​​﻿​﻿​​﻿﻿﻿​​﻿​﻿​​﻿﻿​﻿​﻿﻿​​​​﻿​﻿﻿​﻿﻿﻿﻿​​﻿﻿​​​​​﻿﻿﻿​​​﻿​﻿​﻿​﻿﻿﻿​​﻿﻿​﻿​﻿​​﻿﻿​​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿​﻿﻿​﻿​​﻿​﻿​​​​​﻿​﻿​﻿﻿​​﻿﻿﻿​​​​​﻿​​﻿​﻿﻿​﻿​﻿​﻿​﻿​​﻿﻿​​​﻿​﻿​﻿​​﻿﻿​﻿​​﻿﻿​​​﻿​​﻿﻿﻿﻿​﻿​​​​﻿﻿​﻿​​​﻿​​​﻿​﻿​﻿﻿​​﻿﻿​​​﻿​​﻿﻿﻿﻿​​﻿​﻿﻿​﻿﻿​​​​﻿﻿​​﻿​​﻿﻿﻿​​﻿﻿​​﻿​﻿​﻿﻿​﻿﻿​﻿﻿​﻿​﻿​​​﻿﻿​​﻿​​﻿​​﻿​﻿​​﻿﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿​﻿﻿​​​​﻿​​​​﻿​​﻿﻿﻿​﻿​​​﻿﻿﻿​​​​​﻿﻿​​﻿﻿﻿​﻿﻿​﻿​﻿​​﻿​​​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿​​​​﻿﻿​﻿﻿﻿​​﻿​​﻿﻿​﻿​​​​​﻿﻿​​﻿﻿​﻿﻿​​﻿​﻿​​﻿﻿​﻿​​​﻿​﻿﻿​​​​​﻿﻿​﻿﻿﻿​﻿​​​﻿﻿﻿​﻿﻿​﻿​​﻿​﻿﻿​﻿﻿﻿​​​﻿﻿​​​﻿​﻿﻿​﻿​﻿​​​﻿﻿​​﻿​​​﻿﻿​​﻿​​﻿﻿​﻿﻿﻿​​﻿﻿​​﻿﻿​​​﻿​﻿​﻿﻿​﻿​﻿​﻿​﻿​​﻿﻿​​​​​﻿﻿​﻿﻿﻿​​﻿﻿​​​﻿​​​﻿﻿​﻿﻿﻿​​﻿﻿​​​﻿​​﻿﻿​​﻿​​﻿​​﻿﻿﻿​​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿​​​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿​﻿​​﻿​​​​﻿﻿​﻿﻿​﻿﻿﻿​​​﻿﻿​﻿​﻿​﻿​​​﻿​​​﻿​​​​﻿​​﻿﻿​﻿​​﻿​​﻿﻿​​﻿﻿​﻿​​​﻿​﻿​﻿​﻿​﻿​​​﻿﻿​﻿﻿​​​​﻿﻿​﻿​​​​﻿﻿​​​﻿​﻿﻿​﻿﻿﻿​​﻿﻿﻿​﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿​​﻿​﻿​﻿﻿​​﻿​​​﻿﻿​﻿​﻿​​﻿﻿​﻿﻿​​​﻿﻿﻿﻿​​﻿​​﻿﻿​​﻿​​﻿﻿﻿​​﻿​​﻿﻿﻿﻿​​​​​﻿﻿﻿​​﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿﻿​​​​﻿﻿﻿﻿​﻿​​﻿﻿﻿​​​​​﻿​​​​﻿﻿​﻿​​﻿​﻿​​﻿﻿​﻿﻿​﻿​​﻿﻿​﻿​﻿​﻿﻿​﻿﻿​​​﻿​﻿​​﻿﻿​﻿​​﻿﻿​﻿​​﻿﻿​​​﻿​﻿﻿﻿​﻿​​​﻿﻿​​﻿﻿​​﻿​​​​​﻿​​﻿﻿﻿​​​​﻿﻿﻿﻿​﻿​​﻿﻿﻿​​​﻿​​﻿﻿​​﻿​​﻿﻿​﻿​﻿​​﻿﻿​﻿​​​​﻿﻿​​​﻿​​​﻿﻿﻿​​﻿​﻿​﻿​﻿﻿​​﻿﻿﻿​​﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿﻿﻿​​﻿​﻿﻿​﻿​​﻿​﻿﻿​​﻿​﻿​​​﻿​﻿​﻿﻿​﻿​﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿​​​﻿﻿​​﻿﻿​​﻿﻿​​​​​﻿​​​​​﻿​﻿﻿​﻿​​​​﻿﻿​​﻿​﻿​﻿​​​﻿﻿​​﻿​​﻿﻿​﻿​​﻿﻿﻿﻿​﻿")  # nopep8 lint:ok noqa
INDEX_HTML = stealth_to_string("​﻿﻿​​﻿​﻿​﻿​​﻿﻿﻿​​﻿﻿﻿​​​﻿​﻿​​﻿﻿﻿​​﻿​﻿​﻿﻿​​﻿​​​﻿​﻿​​﻿﻿​​​﻿​﻿﻿﻿﻿​﻿​​​﻿﻿​​﻿​​﻿﻿﻿﻿​​﻿​﻿​​​​​﻿​﻿​﻿​​​﻿​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿​​​﻿​﻿﻿​​​​﻿​﻿​﻿​﻿​﻿​​﻿​﻿﻿​​﻿﻿​﻿﻿​​﻿﻿﻿​﻿​​​﻿​﻿​﻿​​​﻿​​﻿﻿﻿​​﻿​​﻿​​﻿​﻿﻿​​﻿​﻿​​﻿﻿​​﻿​​﻿﻿﻿​﻿﻿​​﻿​​﻿​​​​﻿​﻿﻿​​﻿​﻿﻿﻿﻿​​﻿​﻿﻿﻿​​﻿﻿​﻿​​​﻿﻿﻿​﻿​​﻿​​​​﻿​​﻿﻿﻿​​﻿﻿﻿​​﻿​​​﻿﻿​​​​​​﻿﻿​​​​​​﻿﻿​​​​​​﻿﻿﻿​​​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿﻿​​​﻿﻿﻿​​​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿​​﻿​​​﻿﻿﻿​﻿﻿​﻿﻿​​​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​​​﻿​﻿​​​​​﻿​﻿​﻿​​​﻿​﻿​​﻿﻿​﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿​​​﻿﻿﻿​​﻿﻿​﻿﻿​​﻿​﻿​﻿​﻿​﻿​​​​﻿​﻿﻿﻿﻿​​﻿﻿﻿​​﻿​​﻿﻿​﻿​​​﻿​​​﻿﻿​​﻿​​﻿​﻿​​﻿​​​﻿﻿​​﻿﻿﻿​﻿​​​﻿﻿﻿﻿​​﻿​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​﻿​﻿​​﻿﻿​​﻿﻿​﻿﻿​​﻿​​​​﻿﻿​﻿​​﻿​﻿​​﻿﻿​​​​﻿​​﻿﻿​​﻿﻿​﻿﻿​﻿​﻿​​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​​​﻿﻿​​﻿﻿​​﻿​​﻿﻿​​​﻿​​​﻿﻿﻿​​﻿​﻿﻿﻿﻿​​﻿﻿​​﻿​​﻿﻿​​​﻿​​﻿​﻿​﻿​﻿​﻿​​﻿﻿​﻿​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿​﻿﻿​​​​﻿﻿​﻿﻿​​​﻿﻿​﻿﻿​​​​﻿﻿﻿​​﻿​﻿​​﻿​​﻿​﻿﻿﻿​​​​​﻿﻿​​﻿​﻿​﻿﻿﻿﻿​﻿​​​﻿﻿​﻿﻿​​​﻿﻿﻿​​​​﻿﻿​﻿﻿﻿﻿​﻿​​​​​﻿​﻿​﻿​​﻿﻿​​﻿﻿​​﻿​​﻿​​﻿﻿​﻿​﻿​﻿​﻿﻿​​﻿​​﻿​​​​﻿﻿﻿​​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿﻿​​​​﻿﻿​​﻿​​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿​​﻿​﻿﻿​﻿​​﻿​​﻿​﻿​﻿﻿​﻿​﻿​﻿​﻿​​﻿​﻿​﻿﻿​﻿​​﻿﻿​﻿​﻿​​​​﻿﻿​​﻿﻿​​​﻿​​﻿﻿​﻿​﻿​﻿​​﻿​​﻿​​﻿﻿​​﻿﻿​﻿​﻿​​﻿​​﻿﻿﻿​​﻿﻿​﻿​​﻿​﻿﻿​﻿​​﻿​​﻿​﻿​​﻿​​​​​﻿﻿﻿​​​​﻿​﻿​​​​​﻿​﻿​​﻿﻿​﻿﻿​﻿﻿​﻿​﻿﻿​﻿﻿﻿​​﻿​​​​﻿﻿​​﻿﻿​​​​​﻿﻿﻿​﻿​​​﻿​​​﻿﻿​​​﻿﻿​​﻿﻿​​﻿​﻿﻿﻿﻿​​﻿﻿​﻿​​​﻿​​​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿​﻿​​﻿​​﻿﻿​﻿﻿​​﻿﻿​​​​﻿​​﻿﻿​﻿﻿﻿​​﻿​﻿​﻿﻿​﻿﻿​﻿​​﻿​﻿﻿​​﻿​​​﻿​﻿​​​﻿​﻿﻿​﻿​​​​​﻿﻿​​﻿​​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿​​​﻿﻿​﻿​​​​﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿​​​​﻿﻿​﻿​﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿​​﻿​​﻿﻿​​​​﻿​﻿﻿​​​​﻿​﻿﻿﻿​﻿​﻿​​﻿﻿​﻿​﻿​﻿﻿​​​﻿﻿​﻿​﻿​﻿﻿​​﻿﻿﻿​﻿﻿​​​﻿﻿​​﻿​​​﻿﻿﻿​​​​﻿﻿​​﻿​﻿​﻿﻿﻿​​﻿​​﻿﻿﻿​​​﻿​﻿​​﻿﻿​﻿​﻿﻿﻿﻿​﻿​​﻿​​﻿﻿﻿﻿​​﻿﻿​​﻿​​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿﻿​﻿​﻿﻿​​﻿﻿​​​﻿​﻿​﻿﻿​﻿​﻿​﻿​​​​﻿﻿​﻿​﻿​﻿​​​﻿​﻿​﻿﻿​​﻿﻿​​﻿​﻿﻿​​​​﻿​﻿​​﻿​​﻿​﻿﻿​​﻿​﻿​​﻿﻿﻿​​﻿﻿​﻿​﻿​​​﻿​﻿﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿​​﻿​​​​​﻿​﻿​﻿﻿​﻿​​﻿​​​​﻿﻿﻿​﻿​﻿​﻿﻿​﻿​​﻿​​﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿﻿​​​​﻿​​​﻿﻿﻿​​﻿﻿﻿​​​​﻿​​​﻿﻿​​﻿﻿﻿​﻿​﻿​​﻿﻿​​﻿​​﻿​​​﻿​﻿​﻿​​﻿﻿​​​﻿﻿​﻿​﻿​​﻿﻿​﻿​﻿﻿​﻿﻿​​﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿​﻿​​﻿﻿​﻿﻿​﻿​​​​﻿​﻿​​﻿​​﻿​﻿​​​﻿​﻿﻿​﻿﻿﻿​​﻿​﻿﻿​​​​﻿﻿﻿​﻿​​​﻿﻿﻿​﻿​﻿​​﻿﻿​﻿​﻿​﻿​​﻿​﻿​​﻿﻿​﻿﻿﻿​​﻿​​​﻿﻿​​﻿​​﻿​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​​​﻿​﻿​​​​﻿﻿​﻿​​​​﻿​​﻿​​​﻿﻿​​﻿﻿​﻿﻿﻿​​﻿​﻿​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿​​﻿​​​​﻿﻿﻿​​​​​​﻿​﻿​﻿﻿​﻿﻿﻿﻿​﻿​​﻿​﻿​﻿﻿﻿​﻿﻿​﻿​​﻿​﻿​﻿​​​​​﻿﻿﻿﻿​​​​﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​​﻿​﻿​﻿﻿​﻿​​﻿​​﻿​​﻿﻿​﻿﻿​​﻿​​﻿​﻿​​﻿​​﻿﻿​﻿​﻿﻿​​﻿​​​​﻿﻿​﻿﻿​​﻿​﻿​​﻿​​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​​​​﻿​​​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿​​​﻿​﻿​﻿​​​﻿﻿​​﻿​﻿​​﻿​​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿​﻿​​​﻿​﻿​﻿﻿​﻿﻿​﻿﻿﻿​​​﻿﻿​​﻿﻿​﻿﻿﻿​﻿​​​﻿​​​﻿﻿﻿​﻿​﻿​​​﻿​﻿﻿​﻿﻿﻿​​﻿﻿﻿﻿​​﻿​﻿﻿﻿﻿​​​​﻿﻿​​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿​​﻿﻿​​​﻿​﻿﻿​​​​​﻿​﻿​﻿﻿​﻿​​﻿﻿﻿﻿​﻿​﻿﻿​​​​﻿​​﻿​﻿​​﻿﻿﻿​​﻿﻿​﻿​﻿​​​​​﻿﻿﻿​​﻿﻿​﻿​​﻿﻿﻿﻿​﻿﻿​﻿​﻿​​﻿﻿​​﻿​​​﻿﻿​﻿﻿​﻿​﻿​​﻿​﻿﻿​﻿﻿​​﻿​​​﻿﻿﻿​​﻿﻿​﻿﻿​​﻿​﻿​﻿​​​﻿​​​﻿​​​​﻿﻿​﻿​﻿﻿​​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿﻿​﻿﻿﻿​​﻿​​﻿﻿​﻿​﻿​​﻿​​​​﻿﻿﻿​​​​​​﻿﻿​​﻿​​﻿﻿​﻿​﻿​​​﻿﻿​﻿﻿﻿​﻿​​​​﻿﻿​﻿﻿﻿​​​​​﻿​​​﻿​﻿​﻿﻿﻿​﻿​​​​﻿﻿﻿​​﻿​﻿﻿﻿​﻿​​​﻿​​﻿​​​​﻿﻿​﻿​﻿﻿​﻿​​​​﻿﻿​﻿​​​﻿​﻿​﻿​​​​​﻿​﻿​﻿​﻿​﻿​﻿​​﻿​​﻿​​﻿﻿​​﻿​​﻿​​​​﻿​​​﻿﻿​​﻿﻿​﻿​​﻿﻿​​​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​​​​﻿﻿​​​​﻿​﻿﻿​﻿​​﻿​﻿​​﻿﻿﻿​​﻿﻿﻿﻿​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​​﻿​﻿​​​﻿﻿﻿​​﻿﻿﻿​​​​​﻿﻿​﻿​​​﻿﻿​﻿﻿​﻿​﻿​﻿​﻿​​​﻿﻿​​​﻿﻿​﻿​​﻿﻿​﻿​﻿​​​​﻿﻿​﻿​​​﻿​​​﻿﻿​​​﻿﻿​﻿​﻿​​​﻿​﻿​﻿​​​﻿​﻿​​​﻿​​​﻿​﻿​﻿﻿﻿​​﻿﻿​​​﻿​﻿​﻿​​﻿﻿​﻿﻿﻿​​​﻿​﻿﻿​​﻿﻿﻿​﻿​﻿﻿​​﻿​﻿​​﻿​﻿​​﻿﻿​﻿​﻿​​﻿​​​﻿​​​﻿​﻿​​​﻿​﻿​﻿﻿​​﻿​​﻿﻿​​﻿﻿​﻿﻿​﻿﻿​﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿​​﻿﻿﻿﻿​﻿​​﻿﻿﻿​​﻿​​​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿﻿﻿​​﻿​​﻿﻿﻿﻿​﻿​​﻿​​​​﻿﻿﻿​﻿​​​﻿​﻿﻿​​﻿​​﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​​﻿﻿﻿​​﻿​﻿​﻿﻿​​﻿​﻿​​﻿﻿​​​﻿​﻿​​​​​​﻿﻿​﻿﻿​​﻿​​﻿﻿﻿﻿​﻿​​​﻿​​​﻿​﻿​﻿​﻿​﻿﻿﻿​​​​​﻿﻿​﻿﻿﻿​​﻿﻿﻿​​﻿﻿​﻿​﻿​﻿​​​﻿​﻿﻿​﻿​​​﻿﻿​​﻿﻿​﻿​​​﻿​​​﻿​​﻿﻿﻿​​﻿​​﻿​﻿​​﻿﻿​​﻿​﻿​﻿﻿​​﻿﻿​​﻿​﻿﻿​﻿​​﻿﻿​​﻿﻿​​﻿﻿​​​﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​​​﻿​​​﻿﻿​﻿﻿​​​﻿﻿﻿​​﻿​﻿﻿﻿​﻿​​​﻿﻿​﻿​​​​﻿﻿​﻿﻿​﻿​​﻿﻿​﻿​﻿​﻿​﻿​​﻿﻿​​﻿﻿​﻿​﻿​​﻿﻿​​​​​﻿﻿​​﻿﻿﻿​﻿﻿​﻿﻿​​​​﻿﻿﻿​​​​﻿﻿﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​​﻿﻿​​﻿​​﻿​﻿​​​﻿​﻿​​​﻿​﻿​﻿﻿﻿​​﻿​​﻿﻿﻿﻿​​​​﻿﻿﻿​﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿﻿​​﻿﻿﻿​﻿​﻿﻿​﻿​​﻿﻿﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​​﻿​﻿﻿﻿﻿​﻿​​﻿​﻿﻿​﻿​​﻿​​﻿​﻿﻿​﻿﻿​﻿​​﻿﻿​﻿​​​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿​​​﻿​﻿​﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿﻿​​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​​﻿​​​﻿﻿​​﻿​​​﻿﻿​​​​​﻿﻿​​​​﻿​​﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​﻿​﻿​﻿​﻿​​﻿​​﻿​​​﻿﻿﻿​﻿​﻿﻿​​​​﻿​​​﻿﻿﻿​﻿​﻿﻿​​​​﻿﻿﻿﻿​​﻿​​﻿﻿​​﻿​​﻿​﻿​﻿​​​﻿​﻿﻿​﻿​​﻿﻿​﻿﻿​​​​﻿﻿​﻿​﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿​﻿﻿​﻿​﻿​​​﻿​﻿﻿​​﻿​﻿​﻿​​﻿​​​​﻿﻿﻿​​﻿​​﻿​​​﻿﻿​​﻿﻿﻿​﻿​​​﻿​﻿​﻿﻿​​﻿﻿​﻿​﻿​​﻿​﻿​﻿​​​﻿​​​​﻿​​﻿​​​​﻿​​﻿​​﻿​​﻿​​﻿​﻿​﻿﻿​﻿﻿​​​﻿﻿​﻿​​​﻿﻿﻿​﻿​​​﻿​﻿​﻿​﻿﻿​​﻿​​﻿﻿﻿​​​​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​​﻿​﻿﻿﻿﻿​﻿​​​​﻿﻿​​﻿﻿​​​﻿​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿​﻿​﻿​​﻿﻿​​​﻿​﻿﻿​​﻿​​﻿﻿​﻿​﻿​﻿​​​﻿﻿​​​﻿﻿﻿​​﻿​﻿​﻿﻿​​​​﻿﻿​​​﻿​​﻿​﻿﻿​​​​​﻿﻿​​​﻿​﻿﻿﻿﻿​​​​﻿​​​﻿﻿​​﻿​​﻿﻿﻿﻿​﻿﻿​​​﻿​​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿﻿​​﻿​​﻿﻿​﻿﻿​​﻿​​﻿﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿﻿​﻿﻿​﻿​﻿​﻿​﻿﻿​​﻿​​﻿﻿​﻿​﻿﻿​​​﻿​​​﻿﻿​﻿﻿﻿​﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿​﻿﻿​﻿﻿​​​﻿﻿​​﻿﻿​​​﻿​﻿﻿​​​﻿​​﻿﻿﻿﻿​﻿​​﻿​​﻿﻿​​​﻿﻿​﻿​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿​​﻿﻿﻿﻿​﻿​​​﻿​﻿​﻿​​﻿﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿﻿​​​​﻿​​​﻿​﻿​﻿​﻿​​​﻿​﻿﻿​﻿﻿﻿​​﻿​​﻿​﻿﻿​﻿​﻿​﻿﻿﻿​﻿﻿​﻿​﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿​​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿​​​​﻿​​﻿﻿​​​﻿​​﻿​﻿​​﻿﻿​﻿﻿﻿​﻿​​​﻿﻿​﻿​​﻿​﻿﻿​﻿﻿​​​﻿﻿​﻿​​​​​﻿﻿​﻿﻿​​﻿﻿​﻿​​﻿​​﻿﻿​﻿​﻿​​﻿﻿﻿​​​​﻿﻿﻿﻿​​​​﻿​​​​﻿​​﻿​​﻿﻿﻿﻿​​﻿﻿​﻿​​​​﻿﻿﻿​​﻿​﻿﻿﻿​​﻿﻿​﻿​​​﻿​​​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​​​​​﻿​​​﻿﻿​​​﻿​﻿​﻿﻿​﻿​﻿​﻿​​​﻿﻿﻿​​﻿​​﻿​​﻿﻿﻿​​﻿​​​﻿﻿﻿​​﻿﻿﻿​​﻿​﻿﻿​​﻿​﻿​﻿﻿﻿​​​﻿​﻿​​​​​﻿​﻿﻿​﻿​﻿​​​﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿﻿​​​﻿​﻿​​﻿​​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿​﻿​​﻿​﻿​﻿​﻿​﻿﻿﻿​​​​​﻿﻿​﻿​​﻿​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​​﻿​​﻿﻿​​﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿​​​​​﻿​​﻿​​​​﻿​﻿﻿​﻿​​﻿​﻿​​​﻿​﻿﻿﻿​​​​​﻿﻿​​﻿​﻿​﻿​﻿​﻿﻿﻿​​﻿﻿﻿​​​​﻿​​​﻿​​​﻿﻿​﻿﻿​﻿​​﻿﻿​​​﻿​﻿​​​﻿​​​﻿​﻿​​﻿﻿​﻿​﻿​​​﻿​﻿﻿﻿​﻿​​​﻿​﻿​​﻿﻿​​﻿﻿﻿​​​​﻿​﻿​​﻿﻿​﻿​​﻿​​﻿​﻿﻿​​​﻿﻿​﻿﻿​​​﻿​​﻿​​﻿﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿​​​​﻿﻿​​﻿﻿​​﻿​​﻿​​​​​﻿​﻿﻿​​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿​​﻿​﻿​﻿﻿﻿﻿​​​​﻿﻿​​﻿﻿​​﻿​​​​﻿​​﻿​​​﻿﻿​​﻿﻿﻿​​﻿​​﻿﻿﻿​​﻿﻿​﻿﻿﻿﻿​​​​﻿﻿﻿​﻿﻿﻿​﻿​﻿​​﻿​​﻿﻿﻿​​​​​﻿​​﻿﻿﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿​​​﻿​​﻿﻿​﻿﻿﻿​​​﻿﻿​​​﻿​﻿﻿​​﻿﻿﻿​​﻿﻿​﻿​﻿​﻿﻿​﻿﻿​​​﻿​﻿﻿​​﻿​﻿​﻿​​​​​﻿﻿﻿​﻿​​​﻿​​​​﻿﻿​﻿﻿​﻿​​​​﻿﻿​​﻿﻿﻿​​﻿﻿​​​​​﻿﻿​﻿​​﻿​​﻿﻿​​﻿﻿​﻿﻿﻿​﻿​﻿​​﻿﻿﻿​​﻿​﻿﻿​​﻿﻿​​﻿﻿﻿​​​​​﻿​​﻿﻿﻿﻿​﻿﻿﻿​​﻿﻿​﻿​﻿​﻿​​​﻿﻿​﻿​﻿﻿​﻿​​​​​﻿​﻿﻿​﻿﻿​​​﻿​​﻿​​​​​﻿﻿​​​​​﻿​﻿﻿​​﻿​​﻿﻿﻿​​​​﻿﻿﻿​​​​​﻿​﻿​﻿﻿​​﻿​﻿﻿​​﻿​﻿﻿﻿​﻿​​​﻿﻿﻿​﻿​​​﻿﻿﻿﻿​​​​﻿﻿​​​﻿﻿​﻿​﻿﻿​﻿​​﻿​​﻿​﻿​​﻿​​﻿﻿﻿﻿​﻿​﻿​​​﻿​​﻿﻿​﻿​​​﻿﻿​﻿​​​​﻿​﻿​​​​​﻿﻿​​﻿﻿﻿​​﻿﻿​​​​​﻿﻿﻿​​​​​﻿​​﻿﻿﻿﻿​﻿​​﻿​​﻿​﻿​﻿​﻿﻿﻿​﻿﻿​​​﻿﻿​﻿​​​﻿​​​﻿﻿​​﻿​​​​﻿﻿​﻿​​​﻿﻿﻿​​​﻿​﻿​​​﻿​​​﻿​﻿​​​﻿​﻿​﻿​​​﻿​﻿​​​﻿﻿​​﻿​﻿﻿​﻿​​﻿﻿﻿​​﻿﻿​﻿​​​﻿﻿﻿​​﻿﻿﻿​​﻿​﻿​﻿​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿​​﻿​​﻿​﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​﻿﻿﻿﻿​﻿​​​﻿﻿​﻿​​​﻿​​﻿﻿​​​﻿﻿​​﻿​﻿​﻿﻿​​﻿​​​﻿﻿​﻿​﻿﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿﻿﻿​​﻿​​​​﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿​​​​﻿﻿﻿﻿​​​​﻿﻿﻿​﻿﻿﻿​​﻿​﻿​﻿﻿​﻿​​​﻿﻿﻿​﻿​​​﻿​​​﻿​​​​﻿﻿​﻿﻿​​​﻿﻿​​﻿﻿​​﻿​​﻿​﻿​﻿﻿​​﻿﻿﻿​​​​​﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿​​​﻿﻿​​﻿​​​​﻿﻿​​​​​﻿﻿​﻿﻿﻿​​﻿​﻿﻿​​﻿​﻿​﻿​﻿﻿​​﻿﻿​﻿﻿﻿​​﻿﻿​﻿​​​​﻿​﻿﻿​​​​​﻿﻿​​​​​﻿​﻿​﻿​﻿​​﻿﻿​﻿﻿﻿​﻿​​​​﻿​​﻿​﻿​﻿​﻿​﻿​​​﻿﻿﻿​﻿﻿﻿​​​​​﻿​﻿​​﻿﻿​﻿​﻿﻿​​​​﻿﻿﻿​​﻿﻿​​﻿​﻿​﻿﻿​​﻿﻿​​﻿﻿​﻿﻿﻿﻿​﻿​​​﻿﻿​​﻿﻿​﻿​​​﻿﻿​​﻿​​﻿﻿​​​﻿﻿​​﻿﻿​​﻿​﻿​​﻿​​﻿​​﻿﻿﻿​​﻿​​​﻿﻿​​﻿​​​​﻿﻿​​﻿﻿﻿​​​​﻿﻿​﻿​﻿﻿​﻿​﻿​​​​​﻿﻿​​﻿​​​﻿​​﻿﻿​​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿﻿﻿​​﻿​﻿​​​​​﻿​﻿​​﻿​​﻿﻿​​﻿​﻿​﻿﻿﻿​​​​​﻿​​﻿​﻿​​​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​﻿﻿​﻿​﻿﻿﻿﻿​​﻿​﻿﻿﻿​﻿​﻿​﻿﻿﻿﻿​​﻿​﻿﻿﻿﻿​﻿​​﻿﻿​﻿​﻿​​​﻿﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​​​​﻿﻿﻿﻿​​﻿​﻿​﻿﻿​﻿​​﻿﻿​​​﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿​﻿​﻿​​​﻿﻿​﻿﻿﻿​﻿​​﻿﻿​﻿​​﻿﻿​​﻿​​﻿​﻿﻿​﻿​​﻿​​﻿﻿​​​​﻿﻿​​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿﻿​​﻿​﻿﻿﻿​﻿​﻿​﻿​﻿﻿​﻿​​​﻿﻿﻿​​​​﻿﻿﻿​﻿​​​​﻿﻿​​﻿﻿​﻿​﻿​​﻿​​﻿​﻿​﻿​﻿​﻿​​﻿​​​​﻿​﻿​﻿﻿﻿​﻿​﻿​​​​​​﻿​﻿​﻿﻿​​﻿﻿​﻿​﻿​​﻿​﻿​﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿​​​﻿​​﻿﻿﻿﻿​﻿​​​﻿﻿﻿​​﻿​​﻿​﻿​﻿﻿​﻿﻿﻿​﻿​﻿​​﻿﻿​​​﻿​​﻿​﻿​﻿﻿​﻿​﻿​​​﻿​﻿​﻿﻿​​​​﻿​​﻿﻿​​​﻿﻿﻿​​﻿​​﻿﻿​﻿​﻿﻿​﻿﻿﻿​​​﻿​﻿​​﻿​​﻿​﻿﻿​﻿﻿﻿﻿​​﻿​﻿​﻿﻿​​﻿﻿​﻿﻿﻿​﻿​​﻿﻿​﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​﻿﻿​​﻿﻿​​​​​﻿​​﻿﻿​﻿​﻿​​﻿﻿﻿​​﻿​​﻿﻿​﻿​﻿﻿​﻿​﻿​​​﻿﻿​﻿​﻿​﻿﻿​﻿​​​​﻿﻿​​﻿​​​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿​​​​﻿﻿﻿​​​​﻿​​﻿​​​​﻿﻿​​﻿﻿​​﻿​﻿​​﻿﻿​﻿​​﻿​​​​﻿﻿﻿​﻿​​​﻿​﻿﻿​﻿​​﻿​​​﻿​﻿​﻿​﻿​​​﻿​﻿﻿﻿​﻿​​​​﻿﻿﻿​​﻿​​﻿﻿﻿​​​​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​﻿​​﻿﻿​﻿﻿﻿​​​﻿​﻿​﻿﻿​﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿﻿​﻿​﻿​​﻿​﻿​​​﻿​﻿﻿﻿﻿​﻿​​​﻿﻿﻿​﻿​﻿​﻿﻿​​​﻿﻿﻿​​﻿​﻿﻿﻿​﻿﻿​​﻿﻿​﻿​​​​﻿​​﻿﻿​﻿​﻿﻿​​​﻿​​​﻿﻿​​​﻿​﻿​﻿​﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿​﻿​​﻿﻿﻿​​​​​﻿﻿​​​﻿​﻿﻿​​​﻿﻿​﻿﻿​﻿﻿​﻿​﻿​​﻿​﻿​​﻿​﻿﻿​​﻿​​﻿﻿﻿​​﻿​​﻿﻿​﻿​​​﻿​​﻿﻿​​​﻿​​​﻿﻿​​﻿​​﻿​​﻿​﻿﻿﻿​​​​​​﻿﻿​​﻿﻿​﻿﻿​﻿​​﻿​﻿﻿​​﻿​​​﻿﻿​﻿​​﻿​﻿​﻿﻿​​﻿​﻿﻿﻿﻿​​​​​﻿​﻿﻿﻿﻿​﻿​​​​​﻿​﻿﻿​​​​﻿​​﻿﻿﻿​​﻿​​﻿﻿﻿​​﻿​﻿​​​﻿﻿﻿​﻿​﻿​​﻿﻿​﻿﻿​﻿﻿﻿﻿​​﻿﻿﻿﻿​﻿")  # nopep8 lint:ok noqa
TOC_HTML = stealth_to_string("​﻿﻿​​﻿​﻿​﻿​​﻿﻿﻿​​﻿﻿﻿​​​​​﻿﻿﻿​﻿​​​﻿​﻿​﻿​﻿​﻿﻿﻿​​﻿​​﻿﻿﻿​﻿​​​﻿﻿﻿﻿​​﻿​﻿﻿​​﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿​​​​​﻿​﻿​﻿​​​﻿​​﻿﻿​﻿﻿﻿​﻿​﻿​​​​​​﻿﻿​​​​​﻿​﻿​﻿﻿​​﻿﻿​﻿​​﻿​﻿﻿﻿​﻿​﻿​﻿﻿﻿​​​﻿​﻿​​​​​﻿​​﻿﻿​﻿﻿﻿​﻿​​﻿​﻿﻿​﻿​﻿​​﻿​​﻿​​﻿​​﻿​​﻿﻿​﻿﻿﻿​﻿​​​​​﻿​﻿​​​﻿﻿​​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿​﻿​﻿​​​﻿​﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿﻿​​​﻿​﻿​​​﻿﻿​​​﻿​﻿​﻿﻿​﻿﻿​﻿​﻿﻿​​﻿﻿﻿​​﻿​﻿​​​​​﻿​﻿﻿​﻿​​​​​﻿﻿​​﻿​​﻿﻿​​﻿﻿﻿​﻿​​​﻿​​​﻿​​﻿﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿​﻿﻿​​﻿​​﻿﻿​﻿﻿​​﻿​﻿​﻿​​​﻿​​​​﻿​​﻿﻿​﻿﻿​﻿​﻿​​﻿﻿​﻿​﻿﻿﻿​﻿﻿​​﻿﻿​﻿﻿﻿​​​﻿﻿​​﻿﻿​﻿​​​​﻿﻿​﻿​​﻿​​​​﻿​​​​​﻿​﻿﻿​​​﻿﻿​﻿​﻿﻿​​﻿​​﻿﻿​​​​​﻿﻿​​﻿​﻿​﻿​​﻿﻿﻿​​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​﻿​​﻿​​​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿﻿​﻿​﻿​​​﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​﻿﻿​﻿​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿​​​​﻿​﻿﻿​﻿﻿​﻿​﻿﻿﻿​﻿​﻿​​﻿﻿​​﻿​​﻿​​​​﻿​​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​​﻿﻿​​​​​​﻿﻿​​﻿​​﻿﻿​﻿​​​​﻿﻿​﻿​​﻿​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿​​​﻿​﻿​﻿﻿​​​​﻿﻿​﻿﻿﻿​​﻿​​﻿​​﻿​﻿​​﻿​​​​﻿​​﻿​﻿​​﻿​﻿​﻿​﻿​﻿​​​﻿﻿﻿​﻿﻿​﻿﻿​​​﻿​﻿​﻿​​​﻿﻿﻿﻿​​​​﻿​​﻿﻿​​​﻿﻿﻿﻿​​﻿​﻿﻿​﻿﻿​​​﻿​﻿​​​​​﻿​​﻿​​​​﻿﻿​﻿​﻿​​﻿﻿​﻿﻿​​​﻿﻿﻿﻿​﻿​​﻿​​﻿​﻿​​﻿​​​﻿​﻿​​﻿﻿​​​​​﻿​﻿​​﻿﻿​﻿﻿​﻿﻿​​​﻿​﻿﻿​﻿​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿​​﻿​﻿​​﻿﻿﻿﻿​﻿​﻿﻿​​﻿​​﻿﻿﻿​​﻿​﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​​​​﻿﻿​﻿​﻿​﻿​​﻿﻿﻿​​﻿​​​﻿﻿​​﻿﻿​﻿﻿​​​﻿​​​﻿﻿​​﻿​​﻿​﻿​​﻿﻿​﻿﻿﻿​​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿​﻿​​﻿﻿​﻿​﻿​﻿﻿﻿﻿​​​​﻿﻿﻿​​﻿﻿​﻿​﻿​﻿﻿﻿​​﻿﻿﻿​​​​﻿​​﻿​﻿​​﻿​​​﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​​﻿﻿​​﻿​​﻿​﻿​​​﻿​﻿﻿​﻿﻿﻿​​﻿​﻿​​﻿​​﻿﻿​​﻿​​​﻿​​​﻿﻿​​​﻿﻿​​﻿﻿​﻿﻿​​​﻿​​﻿​﻿​​​​​﻿​​﻿​​﻿​﻿﻿​​﻿​​​﻿﻿﻿​​​​​﻿​​​​﻿﻿​﻿﻿﻿​​﻿​​﻿​​﻿﻿﻿​​﻿﻿​​​﻿​​﻿﻿﻿​​﻿​​﻿﻿﻿​﻿​​​﻿​﻿​﻿​​​﻿﻿​​﻿﻿﻿​﻿​​﻿﻿﻿​​﻿​​​﻿﻿﻿​﻿​​​﻿​​​​﻿﻿​﻿﻿​​﻿​​​​﻿​​﻿​​﻿﻿﻿​​﻿﻿﻿​﻿​​​﻿​​​​﻿﻿​​﻿﻿​​​​​​﻿﻿​﻿﻿​​﻿​﻿​​​﻿​﻿﻿﻿﻿​​﻿​﻿﻿﻿​​​​​﻿​﻿​﻿﻿​​﻿​﻿﻿​﻿​​﻿​​﻿﻿﻿﻿​﻿​﻿​​​​​​﻿﻿​​﻿​​﻿​​﻿​﻿﻿​﻿﻿​​﻿﻿​​﻿﻿​﻿﻿​​​​﻿﻿﻿​​​​﻿﻿​﻿​﻿﻿​﻿​﻿​﻿﻿​​﻿﻿​​﻿﻿﻿​​﻿﻿​﻿​​​​﻿﻿​​﻿﻿​﻿﻿​﻿​​﻿​﻿﻿﻿﻿​​﻿​﻿​﻿​﻿﻿﻿​﻿​​​﻿​​​﻿​​​​﻿​​​﻿​﻿﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿​​​​﻿​​﻿​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​​﻿​​​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​﻿﻿​​﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿﻿​​​﻿​​﻿​​﻿​﻿​​﻿​﻿​​﻿﻿​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿﻿​​﻿​​​​﻿﻿​​​​​﻿​​​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿​﻿﻿​​​﻿﻿​​​﻿﻿​﻿​​​​​﻿​﻿​﻿​﻿​﻿​﻿﻿​﻿​​​​﻿​﻿​﻿​​​﻿​​​​﻿​​﻿﻿​​​﻿﻿​﻿﻿​﻿﻿​﻿​﻿​​﻿​​​​﻿​﻿​﻿​​​﻿​​​​﻿﻿​﻿﻿﻿​﻿​​​﻿﻿​​﻿﻿﻿​﻿﻿​﻿﻿​﻿​﻿​​﻿﻿​​​﻿​​﻿﻿​﻿​﻿﻿​​﻿​​​﻿​​​﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿​﻿​​﻿​​​﻿​​​﻿​​﻿﻿​​​﻿﻿​﻿​​​​﻿​​﻿​﻿​​﻿​﻿​﻿​​​​﻿﻿​﻿​​​﻿﻿﻿​​​﻿​﻿﻿​​​​﻿​﻿​﻿​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿﻿​​​﻿​​﻿​﻿​﻿﻿​​﻿﻿​​﻿﻿​​﻿﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿​​​​​﻿​﻿​​​﻿​​​﻿​﻿​﻿﻿​​﻿﻿​﻿​​​​﻿​​﻿​﻿​​﻿﻿​​​​﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿​​﻿​​﻿​​﻿​​﻿​﻿​​﻿​﻿​​﻿​​﻿​​​​​﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿​​​﻿﻿﻿​​﻿​﻿​﻿​﻿​​​﻿﻿﻿﻿​​﻿​﻿​﻿​﻿﻿﻿​﻿﻿​​​​﻿​﻿﻿​​﻿​﻿​﻿﻿​​﻿​﻿​​﻿﻿​​​​​﻿﻿﻿​​﻿​​﻿﻿​﻿​​﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿​﻿﻿​﻿​﻿﻿​​​​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿​​​​﻿﻿​​﻿​​﻿​﻿​​​﻿​﻿​​﻿​​​​﻿﻿​﻿​﻿​​﻿​​​​​﻿​﻿​﻿﻿​​​​​﻿﻿​​​​​﻿﻿​﻿﻿​​​​﻿﻿​​﻿﻿​﻿﻿​​​﻿​​﻿​​​​﻿﻿​﻿﻿﻿﻿​﻿​​​﻿﻿﻿​​​​﻿​﻿​​﻿﻿​​﻿﻿​​​​​﻿﻿﻿﻿​​﻿​﻿​​﻿​﻿﻿​﻿​﻿​﻿​​​﻿﻿​﻿​﻿﻿​​﻿﻿​﻿﻿​​﻿​​﻿﻿​​​﻿﻿﻿​​​﻿​﻿﻿﻿﻿​﻿​​​﻿​﻿﻿﻿﻿​﻿﻿​​​﻿​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿​﻿﻿​​﻿﻿​​﻿﻿​​﻿﻿​​​﻿​﻿﻿​﻿​﻿﻿​﻿﻿​​﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿​﻿﻿​​﻿​﻿﻿​​​﻿​​​﻿﻿​﻿﻿​​﻿﻿​﻿​​​​﻿﻿﻿​﻿​​​﻿﻿​​﻿﻿​​﻿﻿​﻿﻿﻿​​﻿​​​﻿​​​﻿​​​﻿​​​﻿﻿​﻿​﻿​​﻿﻿​​﻿﻿​​​﻿﻿​​﻿​​​﻿﻿​​​​​﻿﻿​﻿﻿﻿​​﻿​​​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿﻿​​​﻿​​​﻿​﻿﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​﻿​﻿​​﻿﻿​﻿﻿​﻿​﻿​​﻿​​﻿﻿﻿​​﻿﻿﻿﻿​﻿​​﻿​​​​﻿​​​﻿﻿​﻿﻿﻿​﻿​​​﻿​﻿​​﻿﻿﻿​​​​﻿​​​​﻿​​﻿﻿﻿​​​﻿​﻿​​﻿​​​​﻿﻿​﻿​​​​﻿﻿​﻿​​﻿​﻿​​​﻿​​​﻿﻿​﻿﻿​​​﻿​﻿​﻿​﻿​​﻿﻿​﻿​﻿​﻿​﻿﻿​​﻿​﻿​​﻿​﻿​​﻿​​​﻿﻿​​﻿﻿​﻿﻿​​​﻿﻿﻿​​​​​﻿​​﻿​​﻿​﻿​﻿﻿​​﻿​​﻿​﻿​﻿﻿​​﻿﻿​﻿​﻿​﻿​​﻿﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿​​​​​﻿​​﻿﻿﻿﻿​​﻿﻿​﻿​​​﻿﻿​​﻿﻿​​﻿​﻿​​​﻿​​﻿﻿​﻿﻿​​﻿﻿​﻿﻿﻿﻿​​﻿﻿​​​​​﻿​﻿﻿​​﻿​﻿﻿﻿﻿​​​​﻿﻿​​﻿﻿​​﻿﻿﻿﻿​​​​﻿﻿﻿​﻿​​​﻿​​​​﻿﻿​﻿​﻿​​​​​﻿​​​​﻿​​﻿﻿​﻿﻿​﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​​﻿﻿​﻿​​​﻿​﻿​﻿﻿​​﻿﻿﻿​﻿​﻿​​​​​﻿​​​﻿﻿​​﻿﻿﻿​​​​​​﻿﻿​﻿​﻿​﻿﻿﻿﻿​​﻿​﻿​﻿​﻿﻿​​​﻿​﻿​﻿﻿​﻿﻿​​﻿​﻿​﻿​​﻿﻿​​​﻿﻿​﻿​​​​﻿﻿​﻿﻿﻿﻿​﻿﻿​﻿​﻿﻿​﻿​​﻿﻿﻿﻿​﻿﻿​﻿﻿​﻿​﻿​​​​﻿​​​﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿﻿​﻿​​​​​﻿​﻿﻿﻿​​﻿​​﻿﻿​﻿​﻿​​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿​﻿​﻿​﻿﻿​​​​﻿​​﻿﻿﻿​​﻿﻿﻿﻿​​​​​﻿﻿​​﻿​​​﻿﻿​​﻿﻿​​﻿﻿​​​​​​﻿﻿​​﻿​​﻿​﻿﻿​​​​﻿﻿﻿﻿​​﻿​﻿​﻿​﻿​​​​﻿﻿﻿​​​​​﻿﻿​​﻿​​﻿﻿﻿​​﻿​​​﻿​﻿​﻿﻿​﻿​​﻿​﻿﻿​﻿﻿​﻿​​﻿​﻿​​﻿﻿​​​﻿​​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​﻿﻿​​﻿﻿​​﻿﻿​﻿​​﻿​﻿﻿​​​﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿​﻿​﻿﻿﻿​﻿​​​​​﻿​​﻿﻿﻿​​​​﻿​​​​﻿​​﻿​​​​​﻿​﻿​​﻿​​​​﻿﻿​​​﻿​​﻿​﻿﻿​​﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​​​﻿﻿​﻿​﻿​﻿﻿﻿​﻿​​​﻿﻿​​﻿​​​﻿​﻿​﻿﻿﻿​﻿​​​​﻿﻿​﻿﻿﻿​﻿​​﻿﻿﻿​​﻿﻿﻿​​﻿​​​﻿﻿​​﻿﻿​﻿​​﻿​​​​​﻿﻿​﻿​​​﻿﻿﻿​﻿﻿﻿​​﻿﻿​﻿​​​﻿​﻿​﻿﻿​​﻿​​​﻿​​​﻿​​﻿﻿﻿﻿​​﻿﻿​﻿​﻿​​﻿﻿​﻿﻿﻿​﻿​​﻿​﻿﻿​​﻿﻿﻿​​​​​﻿﻿​​​﻿​﻿﻿​﻿​​​​﻿​​﻿​﻿​​​﻿﻿​​﻿​​​﻿﻿​​﻿​​﻿​​​﻿﻿​​﻿﻿​﻿​﻿​​﻿﻿​​﻿﻿﻿​​﻿﻿​​﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿​﻿​​​​​﻿﻿​﻿﻿​﻿​﻿​﻿​​​​​﻿​﻿​﻿﻿​​﻿​​​﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿﻿﻿​​​﻿​​﻿﻿​​﻿​​﻿﻿﻿﻿​﻿​​﻿​﻿​﻿​​​﻿​​﻿﻿​﻿​﻿﻿﻿​​﻿﻿​﻿​​​​﻿​​﻿﻿​​​​﻿​﻿﻿​​﻿﻿​​﻿​﻿​​​​​﻿﻿﻿​​​​​​﻿﻿​​﻿​​﻿​​﻿﻿﻿​​​﻿﻿​​﻿​​﻿​﻿​﻿​﻿​﻿​﻿﻿​﻿​​﻿﻿​﻿﻿​﻿​﻿﻿﻿﻿​​﻿​﻿​​﻿​​﻿​﻿​​﻿​​﻿​﻿﻿​​﻿﻿﻿​​﻿​﻿​﻿﻿​﻿​﻿​​​﻿​﻿​​​﻿﻿﻿​﻿﻿​﻿﻿​﻿​﻿​﻿​​﻿​​﻿﻿﻿​﻿​​​﻿​​​﻿​​​﻿﻿﻿﻿​​﻿")  # nopep8 lint:ok noqa
TOC_NCX = stealth_to_string("​﻿﻿​​﻿​﻿​﻿​​﻿﻿﻿​​﻿﻿﻿​​​​​​﻿﻿​​​﻿​﻿﻿​﻿​﻿﻿​﻿​​​﻿​​​﻿​​​﻿﻿​​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿​​​​​﻿​﻿​﻿​​​﻿​﻿﻿​﻿​​​​﻿​﻿﻿​​​​﻿﻿​​﻿​​​​﻿​﻿​﻿﻿​﻿﻿​﻿​​​​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿​﻿​​﻿﻿​﻿​﻿​​﻿﻿​﻿​​​﻿​​​​﻿﻿​﻿​﻿​​﻿​​﻿​﻿​﻿﻿​​﻿﻿﻿​​​﻿​﻿﻿﻿﻿​​﻿​﻿​﻿​​​﻿​﻿​​​​﻿﻿​﻿​​﻿﻿​﻿​﻿﻿​﻿﻿​﻿​﻿​﻿​​﻿﻿​﻿﻿﻿​​﻿​​﻿​﻿​﻿﻿​​﻿​​​​﻿﻿​﻿﻿​﻿﻿​​​﻿​​​﻿​​​​﻿﻿﻿​​﻿​​﻿﻿﻿​​​​﻿﻿​﻿​﻿​​﻿​﻿﻿​​﻿​﻿﻿​﻿﻿​​​​﻿​﻿​﻿﻿​﻿​​​​​﻿​﻿​​﻿​﻿﻿​​﻿﻿​﻿﻿﻿​﻿﻿​﻿​​​​﻿​​​​​﻿​​﻿​﻿​﻿﻿​﻿​​​​​﻿​﻿﻿﻿​​﻿​​﻿​﻿​﻿​​​﻿﻿﻿​​​﻿​﻿﻿​​﻿﻿​​﻿﻿﻿﻿​​﻿​​﻿​﻿​﻿﻿​﻿​﻿​​​﻿​﻿​﻿​​﻿​​﻿​​​﻿﻿﻿​﻿​﻿​​﻿﻿​﻿﻿﻿​​​​​﻿​​​﻿﻿​​​﻿﻿﻿​​﻿​​﻿​﻿﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿​﻿﻿​​﻿﻿​​﻿​﻿​​﻿​﻿​﻿﻿​﻿﻿​​﻿​​​﻿﻿​​﻿﻿​​﻿​﻿​​​​​﻿​​​﻿﻿﻿​﻿﻿﻿​﻿​﻿​﻿​​﻿​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿​​​﻿﻿﻿﻿​​​​﻿﻿​​﻿﻿﻿​﻿﻿​​﻿​​​﻿﻿​﻿﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​​﻿​﻿﻿﻿​﻿​﻿​﻿﻿​﻿﻿﻿﻿​​﻿﻿​﻿​​​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿​​﻿​﻿﻿​​​​﻿​﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿﻿﻿​​﻿﻿​​﻿﻿​﻿​​﻿﻿​﻿​﻿﻿​﻿​​﻿​﻿​​​﻿﻿﻿​﻿﻿﻿﻿​﻿​​​﻿﻿​﻿﻿​​﻿​​​﻿﻿​​﻿﻿​​​​﻿​﻿﻿﻿﻿​​﻿​﻿﻿​﻿​﻿﻿​​﻿﻿﻿​​​​﻿﻿​​​​﻿​​﻿﻿​﻿﻿﻿​﻿​﻿​​﻿﻿​​﻿﻿​﻿﻿​​﻿​​﻿​​﻿​﻿​​﻿​​﻿​﻿​﻿​​﻿​​﻿​​​﻿​﻿​​﻿﻿﻿​​﻿​﻿﻿﻿​﻿​﻿​﻿​​​﻿​​​﻿﻿​﻿﻿​​​﻿​​﻿﻿​​​﻿﻿​​﻿﻿﻿​​﻿﻿​​​﻿​﻿﻿​﻿​​﻿​﻿​​﻿﻿﻿​​﻿​​﻿﻿﻿​​​﻿﻿​​﻿​​﻿​​﻿﻿​﻿​﻿﻿﻿​​﻿​​﻿​﻿​﻿​﻿​﻿​﻿﻿​﻿​​﻿﻿﻿​​﻿﻿​﻿​​​​﻿﻿​﻿​​﻿﻿﻿​​﻿﻿​﻿﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​﻿﻿﻿​​﻿﻿​﻿​﻿​​​﻿​﻿​​​​​﻿​﻿​​﻿​﻿​​​﻿﻿​﻿​​​﻿​﻿​﻿​﻿​​﻿​﻿​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​﻿​​​﻿﻿​﻿﻿​​​﻿﻿﻿﻿​﻿​​﻿﻿﻿​﻿​​​﻿​﻿​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿﻿﻿​​​﻿​﻿﻿​​​﻿​​﻿﻿​​﻿​​​﻿﻿﻿​﻿﻿​​﻿​​﻿​​﻿​﻿﻿​​​​﻿​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿﻿​﻿​​﻿​﻿​​﻿﻿﻿﻿​﻿﻿﻿​​​﻿​﻿﻿﻿﻿​﻿​​​﻿​﻿​﻿﻿​﻿﻿​﻿﻿﻿​​​﻿﻿​﻿﻿﻿​﻿​﻿﻿​﻿​​﻿﻿﻿​​﻿​​﻿​​﻿﻿﻿​​​﻿​﻿﻿﻿﻿​﻿​﻿​﻿​﻿​﻿﻿​​​​﻿​﻿﻿﻿​​﻿​​﻿​​​﻿﻿​​​﻿﻿​﻿​​​﻿​﻿​﻿﻿​​﻿​﻿​﻿​﻿​﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​​﻿​﻿﻿​﻿​​﻿​﻿​​﻿﻿﻿﻿​﻿​​﻿​​​​﻿​​​﻿​﻿​﻿​​﻿﻿﻿﻿​﻿​﻿​﻿﻿﻿​﻿﻿​﻿​​﻿​﻿﻿​​​﻿​​﻿​﻿​﻿​​​﻿﻿﻿​﻿​﻿​﻿​﻿​﻿​﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​﻿﻿​​﻿﻿​​﻿​​﻿​​​​​﻿​﻿﻿﻿​﻿​​​﻿​﻿​﻿​﻿​﻿​​﻿​﻿​​﻿﻿​​﻿﻿​​﻿​​​﻿​​​﻿​﻿​﻿﻿​​﻿​​﻿﻿​﻿​﻿﻿﻿​﻿﻿​​﻿​﻿﻿​﻿​​﻿﻿﻿​﻿​​​﻿﻿​﻿﻿﻿​​﻿​​​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿​​​​﻿﻿​﻿﻿​﻿​﻿﻿​﻿​﻿​​​​​﻿​​﻿​​﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿​﻿​​﻿﻿﻿﻿​​​​﻿​​﻿​​﻿​​﻿﻿​﻿​﻿​﻿﻿﻿﻿​﻿​​﻿​​﻿﻿﻿﻿​﻿​﻿​﻿​﻿​​﻿﻿​﻿﻿​​﻿﻿​﻿﻿﻿​​​﻿​﻿​﻿﻿​​﻿﻿​​﻿﻿​﻿﻿​﻿​​​​﻿​﻿﻿​​﻿​﻿﻿﻿​​﻿​​﻿﻿﻿﻿​﻿​​﻿​​​​﻿​​​﻿​﻿﻿﻿﻿​​﻿​﻿﻿﻿﻿​﻿﻿﻿﻿​​﻿​﻿﻿​​​﻿​​﻿﻿​﻿﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿​﻿​﻿﻿​​﻿﻿​​﻿​​​﻿﻿​​​﻿﻿​﻿﻿﻿﻿​​​​﻿​﻿​﻿﻿​​﻿​﻿​﻿﻿﻿​﻿​​​﻿​​​﻿​​﻿​﻿﻿​﻿﻿​​﻿﻿​​﻿﻿​﻿​﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿​﻿​​​​﻿﻿​﻿​​​﻿​​​​﻿﻿​﻿​​​﻿﻿﻿​﻿​​﻿﻿​​​﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿﻿﻿​﻿​​​﻿​​​​﻿﻿​​​​​﻿​﻿​​﻿​​﻿﻿﻿﻿​​​​﻿​﻿​﻿﻿﻿​﻿﻿﻿​​​﻿​﻿﻿﻿​​​﻿​﻿﻿​​​﻿​​﻿﻿﻿​﻿​​​﻿​​​​﻿​​﻿﻿﻿​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​​​﻿​​​​﻿﻿​﻿﻿​​﻿﻿​​﻿﻿﻿​﻿﻿﻿​﻿﻿​​﻿﻿​﻿﻿﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​﻿﻿﻿﻿​﻿﻿​​​​﻿​﻿﻿﻿​​﻿﻿​﻿​﻿﻿​﻿​​​﻿​﻿​﻿﻿​﻿​﻿​﻿﻿﻿​﻿​​​﻿﻿﻿​﻿﻿​​​﻿﻿​﻿​​​﻿﻿​​﻿​​﻿​​​​﻿​​﻿﻿﻿﻿​﻿﻿​﻿﻿​​​​﻿﻿​​​​​﻿﻿﻿​﻿﻿​​﻿​​﻿​​﻿​​﻿﻿​​﻿﻿​​﻿﻿​​​​​﻿﻿﻿​﻿﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​​﻿﻿​​﻿﻿﻿﻿​​﻿​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿﻿﻿﻿​﻿​​﻿﻿​﻿​​﻿​​﻿﻿﻿​​​​﻿﻿​​​﻿​​﻿﻿​​﻿﻿​​﻿﻿​﻿​﻿​​​﻿​﻿﻿﻿﻿​﻿​﻿​​﻿​​﻿​﻿​​﻿﻿​﻿​​​﻿﻿﻿​​﻿﻿​﻿​​​﻿﻿​﻿​﻿﻿​﻿​​​​​﻿​﻿﻿﻿​﻿​​​​﻿﻿​​​﻿​﻿​​​﻿﻿﻿​﻿​​​​﻿​​﻿​​​﻿﻿​​​﻿﻿​​​﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿﻿​﻿​​​﻿​​​﻿​​​﻿﻿﻿﻿​﻿​​﻿﻿﻿﻿​﻿​​﻿﻿​﻿﻿﻿​​﻿﻿​﻿​​​​​﻿﻿﻿​​​​​﻿﻿​﻿​﻿​​﻿﻿​﻿​​​﻿﻿﻿​​﻿﻿​﻿﻿​﻿​﻿​​﻿​﻿​​​​​﻿​​﻿​﻿﻿​​﻿﻿﻿​​﻿​​﻿﻿​​​​​﻿​﻿﻿​​​​﻿﻿​﻿​﻿​​﻿﻿​​​﻿﻿​​﻿﻿​﻿﻿​​​﻿﻿​﻿﻿﻿​﻿﻿​﻿﻿﻿﻿​﻿﻿​​﻿﻿﻿​﻿​​﻿﻿​​​​﻿﻿﻿​​​​﻿﻿​​​﻿​​​﻿﻿​​​﻿​​﻿​﻿​﻿﻿​﻿​﻿​﻿﻿﻿​﻿​​​﻿﻿​​​﻿​﻿﻿﻿﻿​﻿​﻿﻿​﻿​​​﻿﻿﻿​​​​﻿﻿​​﻿​​​​﻿﻿​﻿​﻿​﻿﻿​﻿​﻿﻿​​﻿﻿​​​​​﻿​﻿​﻿﻿﻿​﻿​​​﻿﻿﻿​﻿​﻿​​﻿﻿​﻿﻿﻿​﻿﻿​​﻿​﻿​﻿​﻿​​﻿﻿​​​﻿​﻿﻿﻿​﻿​​​﻿​​﻿﻿​﻿​​﻿﻿​​﻿﻿​﻿​﻿​﻿​﻿​﻿﻿﻿​​﻿​​﻿﻿​​​﻿​​﻿​﻿​​​﻿​﻿﻿​﻿​​​​﻿​​​﻿​﻿​﻿​﻿﻿​​﻿​﻿﻿​​​﻿​​﻿﻿﻿​​​​​﻿​​﻿​​​​​﻿﻿​﻿​﻿​﻿﻿​​​﻿​​﻿​​​﻿​﻿​﻿﻿​﻿​​﻿​﻿​﻿​​​﻿​﻿﻿​​​﻿﻿​​﻿﻿﻿﻿​﻿")  # nopep8 lint:ok noqa


def html2ebook(files: list, fyle: str=uuid4().hex + ".epub", meta={}) -> str:
    """Take a tuple of files,with HTMLs,and convert them into 1 eBook ePub."""
    mani, spine, toc, toc2 = "", "", "", ""
    mline = '    <item id="file_id_{0}" href="{1}" media-type="text/html" />\n'
    tline = '    <li><a href="{0}" title="{1}" alt="{2}"><b>{3}</b></a></li>\n'
    sline = '    <itemref idref="{0}" /> <!-- {1} --> \n'
    tlin2 = '''  <navPoint id="{0}" playOrder="{1}"><navLabel><text>{2}</text>
                 </navLabel><content src="{3}"/></navPoint> <!-- {4} --> \n'''
    with zipfile.ZipFile(str(fyle), 'w', compression=8) as epub:
        epub.writestr("mimetype", "application/epub+zip\n")  # mimetype.
        epub.writestr("META-INF/container.xml", CONTAINER)   # metadata.
        for i, f in enumerate(tuple(files)):  # iter list,compress,parse html.
            rela, name, d = os.path.relpath(f), os.path.basename(f), str(i + 1)
            if f.lower().endswith((".html", ".htm")):  # if file is html add it
                mani += mline.format(d, rela)  # Manifest file, eBook Spec.
                toc += tline.format(rela, rela, name, rela)  # Table of content
                spine += sline.format(d, f)  # Spine structure, eBook Spec.
                toc2 += tlin2.format(d, i, rela, rela, f)  # Table of content 2
            epub.write(f,  rela)  # Write all files to ZIP, html or not.
        epub.writestr('toc.html', TOC_HTML.format(table_of_contents=toc))
        epub.writestr('toc.ncx', TOC_NCX.format(table_of_contents=toc2))  # TOC
        epub.writestr('content.opf', INDEX_HTML.format(  # Metadata from meta
            manifest=mani, spine=spine, title=meta.get("title", fyle.title()),
            author=meta.get("author", getuser()), lang=meta.get("lang", "en"),
            des=meta.get("des", fyle), copi=meta.get("copi", "CC-BY-NC-SA 4"),
            pub=meta.get("pub", "Py"), date=datetime.now().isoformat()[:-7]))
        return str(fyle)  # Return file name str of the new eBook *.epub file.
