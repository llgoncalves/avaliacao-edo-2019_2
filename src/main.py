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
    RK = RungeKutta(args['passo'], args['x0'], args['t0'], args['T'],
                    args['H'], args['precisao'])

    xt, t = RK.run()

    if args['precisao'] is None:
        args['precisao'] = 53
    fig, ax = plt.subplots()

    ax.plot(t, xt)

    ax.set(xlabel='t', ylabel='x(t)', title='Diagrama x(t) vs t')
    ax.grid()
    matplotlib.use('tkagg')
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", type=float, default=1,
                        help="Valor de x0 (default = 0.0)")
    parser.add_argument("-t", type=float, default=0,
                        help="Valor de t0 (default = 0.0)")
    parser.add_argument("-T", type=float, default=7,
                        help="Valor de T (default = 6.5)")
    parser.add_argument("-H", type=str, default=[],
                        help="Valor da função H(t) em intervalores de t (Valores fixos) \
                        (default = \"{'H': 0, 'ti': 0, 'tf': 300}\")", action='append')
    parser.add_argument("--func_h", action="store_true", default=False,
                        help="Usar a funcao H(t) definida na classe EDO")

    parser.add_argument("-i", type=float, default=0.1,
                        help="Valor incrementado ao tempo t (passo) em cada interação (default = 0.1)")
    parser.add_argument("-p", type=int, default=None,
                        help="Precisao em número de cadas decimais (Mpmath default = 53)")
    parser.add_argument("-f", type=str, default=None,
                        help="Nome do arquivo de saida")

    args = parser.parse_args()

    func_H = None
    if not args.func_h:
        func_H = []

        for H in args.H:
            func_H.append(literal_eval(H))
        if len(func_H) == 0:
            func_H.append({'H': 0, 'ti': 0, 'tf': 300})
    else:
        func_H = [{'H': None, 'ti': 0, 'tf': 300}]

    argumentos = {'x0': args.x,
                  't0': args.t,
                  'T': args.T,
                  'H': func_H,
                  'passo': args.i,
                  'precisao': args.p,
                  'arquivo': args.f}

    print("Configuração:", argumentos)

    main(argumentos)
