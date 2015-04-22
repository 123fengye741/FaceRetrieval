#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import sys
import random
import numpy as np
import Image


def read_csv_file(csv_file):
    path_and_labels = []
    f = open(csv_file, 'rb')
    for line in f:
        line = line.strip('\r\n')
        path, label = line.split(',')
        label = int(label)
        path_and_labels.append((path, label))
    f.close()
    random.shuffle(path_and_labels)
    return path_and_labels

def vectorize_imgs(path_and_labels):
    arrs   = []
    labels = [] 
    i = 0
    for path_and_label in path_and_labels:
        path, label = path_and_label
        labels.append(label)
        im = Image.open(path)
        size_x, size_y = im.size
        assert size_x == size_y
        gray_im = im.convert('L')
        arr_img = np.asarray(gray_im, dtype='float64')
        vec_img = arr_img.reshape((size_x * size_y, ))
        arrs.append(vec_img)
        i += 1
        if i % 100 == 0:
            sys.stdout.write('\rdone: ' + str(i))
            sys.stdout.flush()
    print ''
    arrs = np.asarray(arrs, dtype='float64')
    labels = np.asarray(labels, dtype='int32')
    return (arrs, labels)

def cPickle_output(vars, file_name):
    import cPickle
    f = open(file_name, 'wb')
    cPickle.dump(vars, f, protocol=cPickle.HIGHEST_PROTOCOL)
    f.close()

def output_data(vector_vars, vector_folder, batch_size=1000):
    if not vector_folder.endswith('/'):
        vector_folder += '/'
    if not os.path.exists(vector_folder):
        os.mkdir(vector_folder)
    x, y = vector_vars
    n_batch = len(x) / batch_size
    for i in range(n_batch):
        file_name = vector_folder + str(i) + '.pkl'
        batch_x = x[ i*batch_size: (i+1)*batch_size]
        batch_y = y[ i*batch_size: (i+1)*batch_size]
        cPickle_output((batch_x, batch_y), file_name)
    if n_batch * batch_size < len(x):
        batch_x = x[n_batch*batch_size: ]
        batch_y = y[n_batch*batch_size: ]
        file_name = vector_folder + str(n_batch) + '.pkl'
        cPickle_output((batch_x, batch_y), file_name)


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print 'Usage: python %s query_set_file searched_set_file query_vector_folder searched_vector_folder' % (sys.argv[0])
        sys.exit()
    query_set_file    = sys.argv[1]
    searched_set_file = sys.argv[2]
    query_vector_folder    = sys.argv[3]
    searched_vector_folder = sys.argv[4]
    
    query_path_and_labels    = read_csv_file(query_set_file)
    searched_path_and_labels = read_csv_file(searched_set_file)

    print 'query img num   : %d' % (len(query_path_and_labels))
    print 'searched img num: %d' % (len(searched_path_and_labels))

    query_vec    = vectorize_imgs(query_path_and_labels)
    searched_vec = vectorize_imgs(searched_path_and_labels)

    output_data(query_vec, query_vector_folder)
    output_data(searched_vec, searched_vector_folder)




    
    
