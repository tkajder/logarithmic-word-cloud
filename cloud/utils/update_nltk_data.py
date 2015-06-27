#!/usr/bin/env python

import nltk

def main():
    '''Update the nltk resources'''
    nltk.download('stopwords')
    nltk.download('punkt')

if __name__ == '__main__':
    main()
