#!/usr/bin/env python

import nltk
from cloud import NLTK_DATA_LOC

def main():
    '''Update the NLTKDATA directory in this folder'''
    nltk.download('stopwords', download_dir=NLTK_DATA_LOC)
    nltk.download('punkt', download_dir=NLTK_DATA_LOC)

if __name__ == '__main__':
    main()
