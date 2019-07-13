#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import sys

import mpmath as mp


class EDO(object):
    def __init__(self, x0, t0, T, H, precisao):
        if precisao is not None:
            mp.prec = precisao

        self.xt = [].append(mp.mpf(x0))
        self.t = [].append(mp.mpf(t0))
        self.T = mp.mpf(T)

        self.H = []
        for valor in H:
            self.H.append({'H':  mp.mpf(valor['H']),
                           'ti': mp.mpf(valor['ti']),
                           'tf': mp.mpf(valor['tf'])})

    def edo(self, x, t, H):
        valor = (6 * x + H) / self.T
        return (-1 * x) + ((mp.tanh(valor) + (mp.tanh(valor)**2)) / (1 + (mp.tan(valor)**3)))
