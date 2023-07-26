#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 18:18:21 2023

@author: tim
"""
import pandas as pd

files = ["location.csv"]

for file in files:
    df = pd.read_csv(file)
    cols = df.columns #capture col names now to later filter out two unnamed cols appearing after apply operation
    df['time']=df['time'].apply(lambda x: x-df.loc[0,"time"])
    df.to_csv(file, index=False, columns=cols)
     
    