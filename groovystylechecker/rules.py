#!/usr/bin/env python3

'''
Rules for Groovy code style checking.
'''

import re


class GroovyStyleRule:
    '''
    Groovy code style rule class.
    '''
    def __init__(self, name, check_function):
        '''
        Method to initialize Groovy code style rule object.

        :param name: name of the rule
        :param check_function: function which returns result of check
        '''
        self.name = name
        self.check_function = check_function

    def check(self, groovy_text):
        '''
        Method to check is rule is violated or met.

        :param groovy_text: text that we want to check for code style
        :returns: 0 if rule is met, 1 if rule is violated
        '''
        print("Checking rule '{}'...".format(self.name))
        result = self.check_function(groovy_text)
        if result > 0:
            print("Rule '{}' is violated!".format(self.name))
        else:
            print("Rule '{}' is met.".format(self.name))
        return result


def findLineNumberBySymbolNumber(text, symbol_number):
    '''
    Function to find line number by symbol number.

    :param text: multiline text where we need to find a line
    :param symbol_number: number of needed symbol in text
    :returns: number of line, where symbol resides
    '''
    line_number = 0
    for i in range(symbol_number):
        if text[i] == '\n':
            line_number += 1
    return line_number


# Rule #1.
def noTrailingSemicolons(groovy_text):
    '''
    Function that checks trailing semicolons.

    :param groovy_text: text that we want to check for code style
    :returns: 0 if rule is met, 1 if rule is violated
    '''
    lines = groovy_text.splitlines()
    errors = False
    for line_number in range(len(lines)):
        line = lines[line_number]
        if len(line) > 0 and line[-1] == ';':
            print('ERROR: trailing semicolon at {} line.'.format(
                line_number + 1))
            errors = True
    return int(errors)


# Rule #2.
def optionalReturn(groovy_text):
    '''
    Function that checks unneeded returns.

    :param groovy_text: text that we want to check for code style
    :returns: 0 if rule is met, 1 if rule is violated
    '''
    lines = groovy_text.splitlines()
    for line_number in range(len(lines)):
        if 'return ' in lines[line_number]:
            print('WARN: return keyword is used at {} line.'.format(
                line_number + 1))
    return 0


# Rule #3.
def defOrType(groovy_text):
    '''
    Function that checks if both def and type are used.

    :param groovy_text: text that we want to check for code style
    :returns: 0 if rule is met, 1 if rule is violated
    '''
    lines = groovy_text.splitlines()
    errors = False
    for line_number in range(len(lines)):
        line = lines[line_number]
        if re.search(r'def\s+.+\s+.+\s*=', line):
            print('ERROR: both def and type are used at'
                  ' {} line.'.format(line_number + 1))
            errors = True
    return int(errors)


# Rule #4.
def defInParams(groovy_text):
    '''
    Function that checks if def is used in function parameters.

    :param groovy_text: text that we want to check for code style
    :returns: 0 if rule is met, 1 if rule is violated
    '''
    errors = False
    function_params = []
    for param in re.finditer(r'def\s+[^\(]+\s*\(([^\)]+)\)', groovy_text):
        function_params.append(param)
    if function_params:
        for param in function_params:
            if 'def ' in param.group(1):
                symbol_number = param.start(1) + param.group(1).find('def ')
                print('ERROR: def is used in function parameters at {} '
                      'line.'.format(findLineNumberBySymbolNumber(
                        groovy_text, symbol_number) + 1))
                errors = True
                break
    return int(errors)


# Rule #5.
def defConstructor(groovy_text):
    '''
    Function that checks if def is used to define a constructor.

    :param groovy_text: text that we want to check for code style
    :returns: 0 if rule is met, 1 if rule is violated
    '''
    errors = False
    groovy_classes = []
    for line in groovy_text.splitlines():
        class_name = re.search(r'class\s+(\S+)\s*{', line)
        if class_name:
            groovy_classes.append(class_name.groups()[0])
    for class_name in groovy_classes:
        found = re.search('def\s+' + class_name + '\s*\(.*\)\s*\{',
                          groovy_text)
        if found:
            symbol_number = found.start(0) + found.group(0).find('def')
            print('ERROR: def is used to define a constructor at'
                  ' {} line.'.format(findLineNumberBySymbolNumber(
                    groovy_text, symbol_number) + 1))
            errors = True
    return int(errors)


# List of actual rules.
ACTUAL_RULES = [
    GroovyStyleRule('no trailing semicolons', noTrailingSemicolons),
    GroovyStyleRule('optional returns', optionalReturn),
    GroovyStyleRule('only def or type used', defOrType),
    GroovyStyleRule('def is not used in function parameters', defInParams),
    GroovyStyleRule('def is not used to define a constructor', defConstructor)
]
