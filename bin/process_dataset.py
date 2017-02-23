#!/usr/bin/env python

import sys

import pandas as pd

'''
   1. Sample code number            id number
   2. Clump Thickness               1 - 10
   3. Uniformity of Cell Size       1 - 10
   4. Uniformity of Cell Shape      1 - 10
   5. Marginal Adhesion             1 - 10
   6. Single Epithelial Cell Size   1 - 10
   7. Bare Nuclei                   1 - 10
   8. Bland Chromatin               1 - 10
   9. Normal Nucleoli               1 - 10
  10. Mitoses                       1 - 10
  11. Class:                        (2 for benign, 4 for malignant)
'''


def main(args):

    fname, fout = args

    # if dlm == 'tsv':
    #     dlm = '\s*[,\t\\\\]'

    df = pd.read_csv(fname, sep=',', na_values='?')

    df.columns = 'id thickness size_u shape_u marg_adh sng_ep bare_nuc bland_chr normal_nuc mitoses classif'.split()
    df = df.dropna()

    df.to_pickle(fout)


if __name__ == '__main__':
    main(sys.argv[1:])
