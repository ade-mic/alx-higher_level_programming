#!/usr/bin/python3
import sys
n_write = sys.stdout.write('and that piece of art is useful \
- Dora Korpar, 2015-10-19\n')
if n_write != len('and that piece of art is useful - \
Dora Korpar, 2015-10-19'):
    sys.stderr.write('incomplete sentence')
sys.exit(1)
