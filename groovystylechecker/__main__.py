#!/usr/bin/env python3

'''
Main script for command-line Groovy style checking.
'''

import argparse

from .checker import GroovyStyleChecker
from .rules import ACTUAL_RULES


def main():
    '''
    Parse arguments and process Groovy file.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('groovyFile', type=str,
                        help='a Groovy file to analyze code style')
    args = parser.parse_args()
    try:
        groovy_text = open(args.groovyFile).read()
        checker_instance = GroovyStyleChecker(groovy_text, ACTUAL_RULES)
        if checker_instance.checkRules() > 0:
            exit(2)
    except IOError:
        print("Could not open file '{}'.".format(args.groovyFile))
        exit(1)


if __name__ == '__main__':
    main()
