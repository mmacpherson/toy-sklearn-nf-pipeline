#!/usr/bin/env python

import sys

import pandas as pd

from sklearn.preprocessing import StandardScaler, RobustScaler, FunctionTransformer
from sklearn.linear_model import LinearRegression, ElasticNetCV, BayesianRidge
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib

SMAP = dict(
    unscaled=FunctionTransformer,
    scaled=StandardScaler,
    robust=RobustScaler, )

MMAP = dict(
    ols=LinearRegression,
    elasticnet=ElasticNetCV,
    bayesianridge=BayesianRidge, 
    svm=LinearSVC, )


def main(args):
    dataset, scale_id, engine_id, outfile = args

    df = pd.read_pickle(dataset)

    y = df.classif.values.ravel()
    X = df[
        'thickness size_u shape_u marg_adh sng_ep bare_nuc bland_chr normal_nuc mitoses'.
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
