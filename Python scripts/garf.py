#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import random
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic/garf')
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
    logging.info("garf")

    epd = epd7in5_V2.EPD()
    logging.info("init and Clear")
    epd.init()

    a = 1

    while a == 1:
    # for filename in picdir:
        logging.info("Loading Img")
        Himage = Image.open(os.path.join(picdir, random.choice(os.listdir(picdir))))
        epd.display(epd.getbuffer(Himage))
        time.sleep(600)



except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd7in5.epdconfig.module_exit()
    exit()
