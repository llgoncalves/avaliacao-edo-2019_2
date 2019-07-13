#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import sys
from ast import literal_eval

from modules.rungekutta import RungeKutta


def main(args):
    RK = RungeKutta(args['passo'], args['x0'], args['t0'], args['T'],
                    args['H'], args['precisao'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", type=float, default=0,
                        help="Valor de x0 (default = 0.0)")
    parser.add_argument("-t", type=float, default=0,
                        help="Valor de t0 (default = 0.0)")
    parser.add_argument("-T", type=float, default=7,
                        help="Valor de T (default = 7.0)")
    parser.add_argument("-H", type=str, default=[],
                        help="Valor da função H(t) em cada instante t \
                        (default = \"{'H': 0, 'ti': 0, 'tf': 300}\")", action='append')
    parser.add_argument("-i", type=float, default=0.1,
                        help="Valor incrementado ao tempo t (passo) em cada interação (default = 0.1)")
    parser.add_argument("-p", type=int, default=None,
                        help="Precisao em número de cadas decimais (Mpmath default = 53)")

    args = parser.parse_args()

    H_list = []

    for H in args.H:
        H_list.append(literal_eval(H))

    if len(H_list) == 0:
        H_list = [{'H': 0, 'ti': 0, 'tf': 300}]

    argumentos = {'x0': args.x,
                  't0': args.t,
                  'T': args.T,
                  'H': H_list,
                  'passo': args.i,
                  'precisao': args.p}

    main(argumentos)
