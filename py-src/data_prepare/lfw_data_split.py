#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import sys
import random

def walk_through_folder_for_split(src_folder):
    query_set    = []
    searched_set = []
    
    label = 0
    for people_folder in os.listdir(src_folder):
        people_path = src_folder + people_folder + '/'
        img_names   = os.listdir(people_path)

        tmp_train = []
        tmp_test = []
        if len(img_names) < 5:
            tmp_train = img_names
            tmp_test = []
        else:
            tmp_train = img_names[0 : len(img_names) * 2 / 3]
            tmp_test  = img_names[len(img_names) * 2 / 3 : ]

        for img_name in tmp_train:
            img_path = people_path + img_name
            searched_set.append((img_path, label))

        for img_name in tmp_test:
            img_path = people_path + img_name
            query_set.append((img_path, label))
            
        sys.stdout.write('\rdone: ' + str(label))
        sys.stdout.flush()
        label += 1
    print '\nquery    set num: %d' % (len(query_set))
    print 'searched set num: %d' % (len(searched_set))
    return query_set, searched_set

def set_to_csv_file(data_set, file_name):
    f = open(file_name, 'wb')
    for item in data_set:
        line = item[0] + ',' + str(item[1]) + '\n'
        f.write(line)
    f.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: python %s src_folder query_set_file searched_set_file' % (sys.argv[0])
        sys.exit()
    src_folder        = sys.argv[1]
    query_set_file    = sys.argv[2]
    searched_set_file = sys.argv[3]
    if not src_folder.endswith('/'):
        src_folder += '/'
    
    query_set, searched_set = walk_through_folder_for_split(src_folder)
    set_to_csv_file(query_set, query_set_file)
    set_to_csv_file(searched_set, searched_set_file)


    



