# -*- coding: utf-8 -*-
# --------------------------------------------------
# Test file for rmrf module
# Quentin Dufournet, 2023
# --------------------------------------------------
# Built-in
import unittest.mock
import os
import shutil
import subprocess as sp
import time
import sys

# 3rd party
import pytest
sys.path.insert(0, 'src')
import rmrf

# --------------------------------------------------

TEST_FOLDER = 'pytest/'
TEMP_FOLDER = 'rmrftmp/'

# So freaking complicated to test with multiprocessing, even ChatGPT can't find a proper way ffs