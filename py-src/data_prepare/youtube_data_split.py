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
        video_folders = os.listdir(people_path)
        random.shuffle(video_folders)
        if len(video_folders) == 1:
            query_video_folders    = []
            searched_video_folders = video_folders
        else:
            query_video_folders    = video_folders[0:1]
            searched_video_folders = video_folders[1:]

        for video_folder in query_video_folders:
            video_path = people_path + video_folder + '/'
            img_files  = os.listdir(video_path)
            random.shuffle(img_files)
            for img_file in img_files[0:5]:
                img_path = video_path + img_file
                query_set.append((img_path, label))

        for video_folder in searched_video_folders:
            video_path = people_path + video_folder + '/'
            img_files  = os.listdir(video_path)
            random.shuffle(img_files)
            for img_file in img_files[0:10]:
                img_path = video_path + img_file
                searched_set.append((img_path, label))
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


    



