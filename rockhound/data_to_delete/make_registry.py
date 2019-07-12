#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 20:36:23 2019

@author: chet
"""

#%%

import rockhound as rh
import pooch
import os

#%%

pooch.make_registry("dat", "dat/dat.txt")
