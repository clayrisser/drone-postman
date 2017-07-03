#!/usr/bin/env python

import os
import sys

if 'PLUGIN_COLLECTION' not in os.environ or not len(os.environ['PLUGIN_COLLECTION']) > 0:
    sys.stdout.write('Missing PLUGIN_COLLECTION\n')
    sys.stdout.flush()
    exit(1)
os.system('newman run ' + os.environ['PLUGIN_COLLECTION'])
