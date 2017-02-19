import sys

import pandas as pd

from sklearn.preprocessing import StandardScaler, RobustScaler, FunctionTransformer
from sklearn.linear_model import LinearRegression, ElasticNetCV
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib

SMAP = dict(
    unscaled=FunctionTransformer,
    scaled=StandardScaler,
    robust=RobustScaler, )

MMAP = dict(
    ols=LinearRegression,
    elasticnet=ElasticNetCV, )


def main(args):
    dataset, scale_id, engine_id, outfile = args

    df = pd.read_pickle(dataset)

    y = df.thickness.values.ravel()
    X = df[
        'size_u shape_u marg_adh sng_ep bare_nuc bland_chr normal_nuc mitoses class'.
        split()].values

    fitter = Pipeline([
        ('scale', SMAP[scale_id]()),
        ('engine', MMAP[engine_id]()),
    ])

    fitter.fit(X, y)

    result = dict(scale=scale_id, engine=engine_id, fitted=fitter)

    joblib.dump(result, outfile)


if __name__ == '__main__':
    main(sys.argv[1:])
