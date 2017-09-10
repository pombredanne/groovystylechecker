#!/usr/bin/env python3

'''
Groovy style checker class script.
'''


class GroovyStyleChecker:
    '''
    Main class for checking Groovy code style.
    '''

    def __init__(self, groovy_text, actual_rules):
        '''
        Method to initialize Groovy style checker object.

        :param groovy_text: text that we want to check for code style
        :param actual_rules: list of rules to use for checking
        '''
        self.groovy_text = groovy_text
        self.actual_rules = actual_rules

    def checkRules(self):
        '''
        Method to check Groovy code style rules.

        :returns: number of violated rules
        '''
        errors = 0
        for rule in self.actual_rules:
            errors += rule.check(self.groovy_text)
        return errors
