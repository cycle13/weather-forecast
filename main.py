#!/usr/bin/env python
import timeit

import pandas as pd
import numpy as np

# format time
import datetime

# operators
import operator
from math import sqrt

# graphical
import matplotlib.pyplot as plt

# linear statistical model
import statsmodels.api as sm

# sklearn suite
from sklearn import linear_model
from sklearn.feature_selection import RFE
from sklearn.metrics import mean_squared_error, median_absolute_error, r2_score, explained_variance_score
from sklearn.datasets import make_classification
# from sklearn.linear_model import LassoCV, LassoLarsCV, LassoLarsIC
# from sklearn.cross_validation import StratifiedKFold
# from sklearn.feature_selection import RFECV
# from sklearn.svm import LinearSVC, SVC
# from sklearn.svm import SVR

import core

fileinput = 'dataset_norway.csv'
# read file
df = core.Formatting(fileinput).to_dataframe()

# get each station index
index = core.Cleaning(df).reference_index()
# stations
stations = core.Cleaning(df).station_processing(index)
# dates
year, month, day = zip(*core.Cleaning(df).date_processing(index))
year = list(year)
month = list(month)
day = list(day)
# hour
hour = core.Cleaning(df).hour_processing(index)
# formatting
hour, day, month, year = [core.Formatting(hour).to_series(name="HOUR"),
                          core.Formatting(day).to_series(name="DAY"),
                          core.Formatting(month).to_series(name="MONTH"),
                          core.Formatting(year).to_series(name="YEAR")]

#processed = core.Formatting(stations).to_concat_dataframe(year, month, day, hour)
print(pd.concat([year, month, day, hour, stations], axis=1))
