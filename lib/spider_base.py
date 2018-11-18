#!/bin/python3

from .owef_urlmanage import URLMAN
from .owef_urlload import URLLOAD
from .owef_urlparse import RESPARSE
from .owef_dataoutput import OUTPUT


class SPIDER_BASE:

    def __init__(self, path=None, mode="w"):
        self.urlmanage = URLMAN()
        self.urlload = URLLOAD()
        self.urlparse = RESPARSE()
        self.output = OUTPUT(path=path, mode="w")

    def run(self, url):
        pass
