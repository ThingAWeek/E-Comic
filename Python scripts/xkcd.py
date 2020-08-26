#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import random
import glob
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic/time')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("xkcd-time")

    epd = epd7in5_V2.EPD()
    logging.info("init and Clear")
    epd.init()

    a = 1

    index = 1;

    while a == 1:
        logging.info("Loading Img")
        timename = 'time/time' + str(index) + '.jpg'
        filename = os.path.join(os.path.dirname(picdir), timename)
        logging.info(filename);
        index = index + 1
        if index > 3099:
            index = 1
        Himage = Image.open(filename)
        epd.display(epd.getbuffer(Himage))
        time.sleep(590)

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd7in5.epdconfig.module_exit()
    exit()
