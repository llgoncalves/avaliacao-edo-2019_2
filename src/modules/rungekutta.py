#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import mpmath as mp
from modules.edo import EDO


class RungeKutta(EDO):
    """Implementa o método númerico RungeKutta de Quarta ordem para solução
aproximada de equações diferenciais.
    """

    def __init__(self, passo, *kwargs):
        EDO.__init__(self, *kwargs)
        self.passo = passo

    #: Executa o algoritmo Runge-Kutta
    def run(self):

        #: Para intervalo de H(t) definido
        for H in EDO.H:
            t = H['ti']

            #: Percorre intervalo
            while(t <= H['tf']):
                id = len(EDO.xt) - 1
                xt = EDO.xt[id]

                valor_h = H['H']

                #: Usar o método EDO.h para obter o valor de H(t)
                if H['H'] is None:
                    valor_h = EDO.h(self, t)

                #: Calcula o valor das constantes ki (1 <= i <= 4)
                k1 = mp.fmul(self.passo, EDO.edo(self, xt, t, valor_h))

                valorA = mp.fadd(xt, mp.fmul(0.5, valor_h))
                valorB = mp.fadd(t,  mp.fmul(0.5, k1))
                k2 = mp.fmul(self.passo, EDO.edo(
                    self, valorA, valorB, valor_h))

                valorA = mp.fadd(xt, mp.fmul(0.5, valor_h))
                valorB = mp.fadd(t,  mp.fmul(0.5, k2))
                k3 = mp.fmul(self.passo, EDO.edo(
                    self, valorA, valorB, valor_h))

                valorA = mp.fadd(xt, valor_h)
                valorB = mp.fadd(t,  k3)
                k4 = mp.fmul(self.passo, EDO.edo(
                    self, valorA, valorB, valor_h))

                #: (k1 + 2 * k2 + 2 * k3 + k4)
                constantes = mp.fadd(mp.fmul(2, k2), mp.fmul(2, k3))
                constantes = mp.fadd(constantes, k1)
                constantes = mp.fadd(constantes, k4)

                #: prox_xt = xt + (1/6) * constantes
                prox_xt = mp.fmul(mp.fdiv(1.0, 6), constantes)
                prox_xt = mp.fadd(xt, prox_xt)

                #: incrementando t
                t = mp.fadd(t, self.passo)

                #: salvando resultados
                EDO.xt.append(prox_xt)
                EDO.t.append(t)

        return EDO.xt, EDO.t
