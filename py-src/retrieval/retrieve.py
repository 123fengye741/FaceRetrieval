#!/usr/bin/env python
# -*- coding:utf8 -*-

from retrieval.load_data import *
from retrieval.pre_process import *
from data_prepare.vectorize_img import cPickle_output
import numpy as np
import sys
import os

def load_train_and_test(test_data_folder, train_data_folder):
    test_file_names  = get_files(test_data_folder)
    train_file_names = get_files(train_data_folder)
    test_x, test_y   = load_data_xy(test_file_names)
    train_x, train_y = load_data_xy(train_file_names)
    print 'test_x:  ', test_x.shape
    print 'test_y:  ', test_y.shape
    print 'train_x: ', train_x.shape
    print 'train_y: ', train_y.shape
    return test_x, test_y, train_x, train_y

def search(test_x, test_y, train_x, train_y, pre_process_method, sim_metric_method):
    if pre_process_method != None:
        test_x, train_x = pre_process_method(test_x, train_x)
    assert test_x.shape[1] == train_x.shape[1]
    query_sample_num = len(test_x)
    
    search_results = []
    for i in range(query_sample_num):
        sample = test_x[i]
        sim_result = sim_metric_method(sample, train_x)
        sort_index = np.argsort(sim_result)
        test_label = test_y[i]

        search_result = []
        for index in sort_index[0:10]:
            search_result.append((train_y[index], sim_result[index]))
        search_results.append((test_label, search_result))
        if i % 100 == 0:
            sys.stdout.write('\rdone: ' + str(i))
            sys.stdout.flush()
    print ''
    return search_results

def sim_metric_cos(sample, train_x):
    return 1 - np.inner(train_x, sample)

def sim_metric_euc(sample, train_x):
    return np.sum( (train_x - sample) ** 2, axis=1)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: python %s test_data_folder train_data_folder search_results_file' % (sys.argv[0])
        sys.exit()

    test_data_folder  = sys.argv[1]
    train_data_folder = sys.argv[2]
    search_results_file = sys.argv[3]
    test_x, test_y, train_x, train_y = load_train_and_test(test_data_folder, train_data_folder)
    # search_results = search(test_x, test_y, train_x, train_y, None, sim_metric_euc)
    # search_results = search(test_x, test_y, train_x, train_y, norm_data, sim_metric_cos)
    # search_results = search(test_x, test_y, train_x, train_y, pca_data, sim_metric_euc)
    search_results = search(test_x, test_y, train_x, train_y, pca_norm_data, sim_metric_cos)
    cPickle_output(search_results, search_results_file)

