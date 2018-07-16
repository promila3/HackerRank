#!/bin/python

import math
import os
import random
import re
import sys

# all letters, a, ab, abc, ..
def edge_ngram(contact):
    return [contact[0:idx] for idx in range(1, len(contact) + 1)]

contact_indices = {}
def add(contact):
    for token in edge_ngram(contact):
        contact_indices[token] =contact_indices.get(token, 0) + 1

def find(name):
    return contact_indices.get(name, 0)

if __name__ == '__main__':
    n = int(raw_input())

    for n_itr in xrange(n):
        opContact = raw_input().split()

        op = opContact[0]

        contact = opContact[1]
        if op == 'add':
            add(contact)
        elif op == 'find':
            print find(contact)
        
