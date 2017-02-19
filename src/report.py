import sys

import pandas as pd
from sklearn.externals import joblib


def main(args):

    df = pd.read_pickle(args[0])
    y = df.thickness.values.ravel()
    X = df[
        'size_u shape_u marg_adh sng_ep bare_nuc bland_chr normal_nuc mitoses class'.
        split()].values

    results = []
    for fn in args[1:]:
        z = joblib.load(fn)
        results.append([z['scale'], z['engine'], z['fitted'].score(X, y)])

    for row in sorted(results, key=lambda x: -x[-1]):
        s, e, v = row
        print('{:12s} {:12s} {:.2f}%'.format(s, e, v * 100))


if __name__ == '__main__':
    main(sys.argv[1:])
