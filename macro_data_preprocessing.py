#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
df = pd.read_csv('2020-12.csv')
df.loc[1:,df.iloc[0]==2] = df.loc[1:,df.iloc[0]==2].diff()
df.loc[1:,df.iloc[0]==3] = df.loc[1:,df.iloc[0]==3].diff().diff()
df.loc[1:,df.iloc[0]==4] = np.log(df.loc[1:,df.iloc[0]==4])
df.loc[1:,df.iloc[0]==5] = np.log(df.loc[1:,df.iloc[0]==5]).diff()
df.loc[1:,df.iloc[0]==6] = np.log(df.loc[1:,df.iloc[0]==6]).diff().diff()
df.loc[1:,df.iloc[0]==7] = (df.loc[1:,df.iloc[0]==7].pct_change()-1).diff()
df = df.drop(0)
df = df.rename({'sasdate':'Date'}, axis=1)
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'] + pd.offsets.MonthEnd(0) 