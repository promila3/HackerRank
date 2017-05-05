#!/bin/python

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))
maxHeight = max(height)
numCandles = height.count(maxHeight)
print numCandles
