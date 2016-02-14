# -*- coding:UTF-8 -*-
#!/usr/bin/python

'''
Script Name     : deleteSmallImage.py
Author          : svoid
Created         : 2015-03-14
Last Modified   : 
Version         : 1.0
Modifications   : 
Description     : 文件相关操作
'''

import os
import sys
import stat 
import time

def get_dir_file(dirname):
    filelist = []
    for file in os.listdir(dirname):
        targetFile = os.path.join(dirname,  file) 
        filelist.append(targetFile)
    return filelist

def get_file_size(filename):
    return os.stat(filename)[stat.ST_SIZE]

if __name__ == '__main__':
    WORKDIR = '/home/git/temp/'
    filelist = get_dir_file(WORKDIR)
    for file in filelist:
        if (get_file_size(file) <= 1024*50 and os.path.exists(file)) :
            os.remove(file)
            print("delete file %s"%(file))
        else:
            print("file not exists or file is well")
