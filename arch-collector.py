#!/usr/bin/env python3

import sys
import os
from PyPDF2 import PdfReader
from PIL import IMAGE

search_path = "/home/share/books"
root_path = "/home/share/arch_collection"

#def analyze_file(name):
#    reader = PdfReader(name)

def search_file(p):
    for l in os.listdir(p):
        t = os.path.join(p,l)
        if os.path.isdir(t):
            search_file(t)
        else:
            print(t, end='')
            print("  Size:{}".format(os.path.getsize(t)))
#            analyze_file((t))

def main():
    if not os.path.exists(search_path):
        print("search path is not exist!")
        exit()
    else:
        search_file(search_path)

if __name__ == "__main__":
    main()
