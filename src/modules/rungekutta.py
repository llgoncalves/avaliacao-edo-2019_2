#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from modules.edo import EDO


class RungeKutta(EDO):
    def __init__(self, passo, *kwargs):
        EDO.__init__(self, *kwargs)
        self.passo = passo
