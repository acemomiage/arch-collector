#!/usr/bin/env python3

import sys
import os
import subprocess
import time

search_path = "/home/share/books"
#search_path = "/tmp/pdftest/"
root_path = "/home/share/arch_collection"
pdf2ppm = ['pdftoppm', '-singlefile', '-png', '', '/tmp/arch-collector-tmp']
convert_cmd = ['convert', '-thumbnail', '150x150', '/tmp/arch-collector-tmp.png', '']

def isPDF(name):
    if os.path.splitext(name)[1] == '.pdf':
        return True
    else:
        return False

def analyze_file(name):
    if isPDF(name):
        print(name)
        pdf2ppm[3] = name
        cmd_ret = subprocess.run(pdf2ppm)
        if cmd_ret != 0:
            out_file_name = os.path.join(root_path,os.path.splitext(os.path.basename(name))[0]) + '.png'
            convert_cmd[4] = out_file_name
            cmd_ret = subprocess.run(convert_cmd)
        os.remove('/tmp/arch-collector-tmp.png')
        time.sleep(1)

def search_file(p):
    for l in os.listdir(p):
        t = os.path.join(p,l)
        if os.path.isdir(t):
            search_file(t)
        else:
            analyze_file(t)

def main():
    if not os.path.exists(search_path):
        print("search path is not exist!")
        exit()
    else:
        search_file(search_path)

if __name__ == "__main__":
    main()
