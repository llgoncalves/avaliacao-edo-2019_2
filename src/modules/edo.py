#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import sys

import mpmath as mp


class EDO(object):
    """Define um equação diferencia."""
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
                self.H.append({'H': None,
                               'ti': mp.mpf(valor['ti']),
                               'tf': mp.mpf(valor['tf'])})
                return

            self.H.append({'H': mp.mpf(valor['H']),
                           'ti': mp.mpf(valor['ti']),
                           'tf': mp.mpf(valor['tf'])})

    #: Define a função H(t)
    def h(self, t):
        if t < 100:
            return 0

        if t <= 200:
            return mp.fmul(0.3, mp.sin(t))

        if t <= 300:
            result = mp.fmul(mp.fneg(0.05), t)
            exponencial = mp.exp(result)
            result = mp.fmul(0.3, exponencial)

            return mp.fmul(result, mp.sin(t))

    #: Obtem o valor de dx/dt
    def edo(self, x, t, H):
        valor = mp.fmul(6.0, x)
        valor = mp.fadd(valor, H)
        valor = mp.fdiv(valor, self.T)

        result = mp.fadd(mp.tanh(valor),
                         mp.power(mp.tanh(valor), 2.0))
        result = mp.fdiv(result,
                         mp.fadd(1, mp.power(mp.tan(valor), 3.0)))

        return mp.fadd(mp.fneg(x), result)
