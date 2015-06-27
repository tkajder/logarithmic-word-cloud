#!/usr/bin/env python

import argparse
import collections
import math
import nltk
import os
import sys

def cli():
    '''Define the command line structure and parse the arguments'''
    parser = argparse.ArgumentParser(description='Create an html word cloud from text file', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('inputfile',
                        help='The file to generate the word cloud of')
    parser.add_argument('outputfile',
                        help='The output file to write the html word cloud to')
    parser.add_argument('--minFontSize',
                        required=False,
                        default=12,
                        type=int,
                        help='The minimum font size to use in the word cloud')
    parser.add_argument('--maxFontSize',
                        required=False,
                        default=48,
                        type=int,
                        help='The maximum font size to use in the word cloud')
    parser.add_argument('--numWords',
                        required=False,
                        default=25,
                        type=int,
                        help='The number of words to use in the word cloud')

    args = parser.parse_args()
    return args

def read_file(filename):
    '''Read a file and return it's contents'''
    with open(filename, 'r') as file:
        contents = file.read()
    return contents

def parse_word_counts(contents):
    '''Parse the file contents into word counts'''
    stopwords = set(nltk.corpus.stopwords.words())

    # Parse out stopwords and punctuation/numbers and create word counts
    words = nltk.word_tokenize(contents)
    word_counts = collections.Counter()
    for lower_word in (word.lower() for word in words):
        if lower_word not in stopwords and lower_word.isalpha():
            word_counts[lower_word] += 1

    return word_counts

def generate_font_sizes(word_counts, min_font_size, max_font_size, num_words):
    '''Generate a word cloud from word counts'''
    # Grab the least and most common's word count
    min_count = word_counts.most_common(num_words)[-1][1]
    max_count = word_counts.most_common(num_words)[0][1]

    font_sizes = {}

    for word, count in word_counts.most_common(num_words):
        font_size = calculate_font_size(count,
                                        min_count,
                                        max_count,
                                        min_font_size,
                                        max_font_size)
        font_sizes[word] = font_size

    return font_sizes

def calculate_font_size(count, min_count, max_count, min_font_size, max_font_size):
    '''Calculate the font size from word count with logarithmic scaling;
    source http://lofjard.se/post/the-logarithmic-tag-cloud'''
    weight = (math.log(count) - math.log(min_count)) / (math.log(max_count) - math.log(min_count))
    size = min_font_size + round(weight * (max_count - min_count))
    return size

def generate_word_cloud(font_sizes):
    '''Generate an html word cloud from the word:font_size dictionary'''
    html = '<html><body><p>'
    for word, font_size in font_sizes.items():
        html += html_word(word, font_size)
    html += '</p></body></html>'
    return html

def html_word(word, font_size):
    '''Generate the html word element from word and fontsize'''
    return '<span style="font-size: {font_size}pt">{word} </span>'.format(font_size=font_size, word=word)

def export_word_cloud(word_cloud, output_file):
    '''Write the html word cloud to file'''
    with open(output_file, 'w') as file:
        file.write(word_cloud)

def main():
    # Parse the command line
    args = cli()

    # Read the contents of file
    contents = read_file(args.inputfile)

    # Parse the contents into word counts
    word_counts = parse_word_counts(contents)

    # Generate font_sizes from word counts
    font_sizes = generate_font_sizes(word_counts,
                                     args.minFontSize,
                                     args.maxFontSize,
                                     args.numWords)

    # Generate word cloud from font sizes
    word_cloud = generate_word_cloud(font_sizes)

    # Output the word cloud
    export_word_cloud(word_cloud, args.outputfile)

if __name__ == '__main__':
    main()
