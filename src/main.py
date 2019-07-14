#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import sys
import tkinter as tk
from ast import literal_eval

import matplotlib
import matplotlib.pyplot as plt

import mpmath as mp
from modules.rungekutta import RungeKutta

matplotlib.use('tkagg')


def main(args):
    #: Instância da  RungeKutta() com a configuração informada por parâmetro
    RK = RungeKutta(args['passo'], args['x0'], args['t0'], args['T'],
                    args['H'], args['precisao'])

    #: Calcula o resultado
    xt, t = RK.run()

    #: Plota o gráfico x(t) vs t
    fig, ax = plt.subplots()
    ax.plot(t, xt)

    ax.set(xlabel='t', ylabel='x(t)', title='Diagrama x(t) vs t')
    ax.grid()
    matplotlib.use('tkagg')
    plt.show()


if __name__ == "__main__":
    #: Definindo argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", type=float, default=1,
                        help="Valor de x0 (default = 0.0)")
    parser.add_argument("-t", type=float, default=0,
                        help="Valor de t0 (default = 0.0)")
    parser.add_argument("-T", type=float, default=7,
                        help="Valor de T (default = 7.0)")
    parser.add_argument("-H", type=str, default=[],
                        help="Valor da função H(t) em intervalores de t (Valores fixos) \
                        (default = \"{'H': 0, 'ti': 0, 'tf': 300}\")", action='append')
    parser.add_argument("--func_h", action="store_true", default=False,
                        help="Usar a funcao H(t) definida na classe EDO")

    parser.add_argument("-i", type=float, default=0.05,
                        help="Valor incrementado ao tempo t (passo) em cada interação (default = 0.1)")
    parser.add_argument("-p", type=int, default=None,
                        help="Precisao em número de cadas decimais (Mpmath default = 53)")

    args = parser.parse_args()

    funcH = None

    #: Guarda em funcH o valor de H(t)
    if not args.func_h:
        funcH = []

        for H in args.H:
            funcH.append(literal_eval(H))
        if len(funcH) == 0:
            funcH.append({'H': 0, 'ti': 0, 'tf': 300})
    #: Usar o método h da class EDO para obter o valor de H(t)
    else:
        funcH = [{'H': None, 'ti': 0, 'tf': 300}]

    argumentos = {'x0': args.x,
                  't0': args.t,
                  'T': args.T,
                  'H': funcH,
                  'passo': args.i,
                  'precisao': args.p}

    print("Configuração:", argumentos)

    main(argumentos)
