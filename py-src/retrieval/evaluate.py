#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import sys
import pickle

def evaluate_AP(search_results_file):
    '''count num of right prediction of top-N'''
    num_samples  = len(results)
    top_1_right  = 0
    top_5_right  = 0
    top_10_right = 0
    for line in results:
        test_label, result = line
        for i in range(10):
            predict_label = result[i][0]
            if predict_label != test_label:
                continue
            if i < 1:
                top_1_right += 1
            if i < 5:
                top_5_right += 1
            if i < 10:
                top_10_right += 1
    top_1_precision  =  top_1_right * 1.0 / (num_samples * 1)
    top_5_precision  =  top_5_right * 1.0 / (num_samples * 5)
    top_10_precision = top_10_right * 1.0 / (num_samples * 10)
    print 'top-1  AP: %f = %d / %d' % (top_1_precision,  top_1_right,  num_samples)
    print 'top-5  AP: %f = %d / %d' % (top_5_precision,  top_5_right,  num_samples * 5)
    print 'top-10 AP: %f = %d / %d' % (top_10_precision, top_10_right, num_samples * 10)


def evaluate_precision(results):
    '''retrieval is right when right prediction appears in top-N'''
    num_samples  = len(results)
    top_1_right  = 0
    top_5_right  = 0
    top_10_right = 0
    for line in results:
        test_label, result = line
        for i in range(10):
            predict_label = result[i][0]
            if predict_label != test_label:
                continue
            if i < 1:
                top_1_right += 1
            if i < 5:
                top_5_right += 1
            if i < 10:
                top_10_right += 1
            break
    top_1_precision  =  top_1_right * 1.0 / (num_samples)
    top_5_precision  =  top_5_right * 1.0 / (num_samples)
    top_10_precision = top_10_right * 1.0 / (num_samples)
    print 'top-1  precision: %f = %d / %d' % (top_1_precision,  top_1_right,  num_samples)
    print 'top-5  precision: %f = %d / %d' % (top_5_precision,  top_5_right,  num_samples)
    print 'top-10 precision: %f = %d / %d' % (top_10_precision, top_10_right, num_samples)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python %s search_results_file' % (sys.argv[0])
        sys.exit()

    search_results_file = sys.argv[1]
    f = open(search_results_file, 'rb')
    results = pickle.load(f)
    f.close()

    evaluate_AP(results)
    evaluate_precision(results)
    
