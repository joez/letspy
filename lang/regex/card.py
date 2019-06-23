#!/usr/bin/env python3

import re

'''A valid credit card has the following characteristics:

* It must start with a 4, 5 or 6
* It must contain exactly 16 digits
* It must only consist of digits (0-9)
* It may have digits in groups of 4, separated by one hyphen "-"
* It must NOT use any other separator like ' ', '_', etc
* It must NOT have 4 or more consecutive repeated digits
'''
def valid(card):
    if '-' in card:
        if any(len(g) != 4 for g in card.split('-')):
            return False
        card = card.replace('-', '')
    if not re.match(r'[456]\d{15}$', card):
        return False
    if re.search(r'(\d)\1{3,}', card):
        return False
    return True

for _ in range(int(input())):
    print('Valid' if valid(input()) else 'Invalid')
