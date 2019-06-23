#!/usr/bin/env python3

from datetime import date

m, d, y = map(int, input().strip().split())
print(date(y, m, d).strftime('%A').upper())
