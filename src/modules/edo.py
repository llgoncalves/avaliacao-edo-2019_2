#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import sys

import mpmath as mp


class EDO(object):
    H = []
    xt = []
    t = []
    T = None

    def __init__(self, x0, t0, T, H, precisao):
        if precisao is not None:
            mp.prec = precisao

        self.xt.append(mp.mpf(x0))
        self.t.append(mp.mpf(t0))
        self.T = mp.mpf(T)

        for valor in H:
            if valor['H'] is None:
                self.H.append({'H':  None,
                               'ti': mp.mpf(valor['ti']),
                               'tf': mp.mpf(valor['tf'])})
                return

            self.H.append({'H':  mp.mpf(valor['H']),
                           'ti': mp.mpf(valor['ti']),
                           'tf': mp.mpf(valor['tf'])})

    def h(self, t):
        if t < 100:
            return 0

        if t <= 200:
            return mp.mpf(0.3) * mp.sin(t)

        if t <= 300:

            return mp.mpf(0.3) * (mp.power(mp.euler, mp.mpf(-0.05) * t)) * mp.sin(t)

    def edo(self, x, t, H):
        valor = (6 * x + H) / self.T
        return (mp.mpf(-1) * x) + ((mp.tanh(valor) + (mp.tanh(valor)**2)) / (1 + (mp.tan(valor)**3)))
