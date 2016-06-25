#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" Up for the output.json results """


import re
import json


SOURCE_FILE = 'output.json'


def main():
    """ Doing actions """
    final_styles = []
    with open(SOURCE_FILE, 'r') as source_file:
        data = source_file.read()
    items = json.loads(data)
    for item in items:
        try:
            styles = re.search(r'\((.*?)\)', item['title']).groups()[0]
            if '/' in styles:
                out_style = [style.lower().stip() for style in styles.split('/')]
                final_styles += out_style
            elif ',' in styles and '/' not in styles:
                out_style = [style.lower().strip() for style in  styles.split(',')]
                final_styles += out_style
        except AttributeError:
            pass
    print ", ".join(set(final_styles))


if __name__ == '__main__':
    main()
