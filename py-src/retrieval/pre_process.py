#!/usr/bin/env python
# -*- coding:utf8 -*-

import numpy as np
from sklearn.decomposition import RandomizedPCA

def sqrt_norm(x):
    sqrt_x = np.sqrt(np.sum(x**2, axis=1))
    sqrt_x = sqrt_x.reshape((sqrt_x.shape[0], 1))
    norm_x = x / sqrt_x
    return norm_x

def norm_data(test_x, train_x):
    print 'sqrt normalizing data ...'
    norm_test  = sqrt_norm(test_x)
    norm_train = sqrt_norm(train_x)
    return norm_test, norm_train

def pca_data(test_x, train_x, params):
    print 'pcaing data ...'
    components = int(params['components'])
    pca = RandomizedPCA(components, whiten=True).fit(train_x)
    pca_train_x = pca.transform(train_x)
    pca_test_x  = pca.transform(test_x)
    return pca_test_x, pca_train_x

def sim_metric_cos(sample, train_x):
    return 1 - np.inner(train_x, sample)

def sim_metric_euc(sample, train_x):
    return np.sum( (train_x - sample) ** 2, axis=1)

pre_process_methods_set = {'pca': pca_data, 'None':None}
sim_metric_methods_set  = {'euc': sim_metric_euc, 'cos': sim_metric_cos}

