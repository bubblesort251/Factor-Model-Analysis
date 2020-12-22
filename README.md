# Factor-Model-Analysis
Place to put Factor Modeling Code for future use

## FactorModelLib

This file contains relevant functions which calculate linear factor models

## FactorMomentumLib

The function "compute_returns" constructs factor momentum from a pandas dataframe of factor returns.  It can calculate both time-series and cross sectional factor momentum

## TrendFilteringLib

The two most useful functions in this library are "filter_time_series" and "plot_returns_regime_multiple"

* filter_time_series: runs the LASSO trend filtering algorithm and returns a numpy series of labels given a lambda value
* plot_return_regime_multiple: creates a graph where the "crash" regime is shaded in grey

## FinancialMetricsLib

This library contains various functions to calculate financial metrics

## FullLib.yml

Library which should have all dependencies installed. Creates a conda environment to run the code
