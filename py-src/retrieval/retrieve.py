#!/usr/bin/env python
# -*- coding:utf8 -*-

from retrieval.load_data import *
from retrieval.pre_process import *
from retrieval.parse import *
from retrieval.evaluate import evaluate_precision, evaluate_AP
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

def search(test_x, test_y, train_x, train_y, str_pre_process, str_sim_metric, params):
    pre_process_method = pre_process_methods_set[str_pre_process]
    if pre_process_method != None:
        test_x, train_x = pre_process_method(test_x, train_x, params)

    sim_metric_method = sim_metric_methods_set[str_sim_metric]
    if str_sim_metric == 'cos':
        test_x, train_x = norm_data(test_x, train_x)

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

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python %s exp_param' % (sys.argv[0])
        sys.exit()

    exp_params_file = sys.argv[1]
    params_results, test_data_folder, train_data_folder = parse_params(exp_params_file)
    test_x, test_y, train_x, train_y = load_train_and_test(test_data_folder, train_data_folder)

    print ''
    print '%d experiments' % (len(params_results))

    for params in params_results:
        description = params['description']
        exp_id = params['id']
        print ''
        print '*************************************************'
        print exp_id, '--', description
        str_pre_process = params['pre_process_method']
        str_sim_metric  = params['sim_metric_method']
        search_results = search(test_x, test_y, train_x, train_y, 
                str_pre_process, str_sim_metric, params)
        evaluate_precision(search_results)
        evaluate_AP(search_results)

    # cPickle_output(search_results, search_results_file)

