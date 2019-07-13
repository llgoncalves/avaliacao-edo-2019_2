#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import mpmath as mp
from modules.edo import EDO


class RungeKutta(EDO):
    def __init__(self, passo, *kwargs):
        EDO.__init__(self, *kwargs)
        self.passo = passo

    def run(self):

        for H in EDO.H:
            t = H['ti']

            while(t <= H['tf']):
                id = len(EDO.xt) - 1
                xt = EDO.xt[id]

                valor_h = H['H']

                if H['H'] is None:
                    valor_h = EDO.h(self, t)

                k1 = self.passo * EDO.edo(self, xt, t, valor_h)
                k2 = self.passo * \
                    EDO.edo(self, xt + (0.5) * valor_h,
                            t + (0.5) * k1, valor_h)
                k3 = self.passo * \
                    EDO.edo(self, xt + (0.5) * valor_h,
                            t + (0.5) * k2, valor_h)
                k4 = self.passo * EDO.edo(self, xt + valor_h, t + k3, valor_h)

                prox_xt = xt + (mp.mpf(1) / mp.mpf(6)) * \
                    (k1 + 2 * k2 + 2 * k3 + k4)

                t = t + self.passo

                EDO.xt.append(prox_xt)
                EDO.t.append(t)

        return EDO.xt, EDO.t
