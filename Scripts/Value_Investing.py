######### Value Investing Script ###############

## Note that the script takes approx 80 mins to run.

######### IMPORTS ###############
import numpy as np
import pandas as pd
import xlsxwriter

import yfinance as yf
# for the fundamental ratios it is easier to use yahoo_fin
import yahoo_fin.stock_info as si

import scipy.stats as stats 
import math

# this notebook contains future warnings which i wanted to be ignored
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

## used for progress on the loop
from tqdm import tqdm


####### TICKERS ############
tickers = si.tickers_sp500()


###### CREATE DATAFRAME ########
my_columns = [
    "Ticker",
    "Price",
    "P/E Ratio",
    "P/E Percentile",
    "P/B Ratio",
    "P/B Percentile",
    "P/Sales Ratio",
    "P/Sales Percentile",
    "EV/EBITDA Ratio",
    "EV/EBITDA Percentile",
    "EV/Gross Ratio",
    "EV/Gross Percentile",
    "NumberSharesToBuy"
]

value_df = pd.DataFrame(columns=my_columns)



######## GETTING MARKET DATA ##############
## THIS BLOCK TAKES APPROX 80 MINS TO RUN
## Data can be loaded above
for tick in tqdm(tickers):
    try:
        stock = si.get_stats_valuation(tick).iloc[:,0:2]
        price = si.get_quote_table(tick)["Quote Price"]
        pe_ratio = float(stock.iloc[2,1])
        pb_ratio = float(stock.iloc[6,1])
        ps_ratio = float(stock.iloc[5,1])
        ev_ebitda = float(stock.iloc[8,1])
        ev_gross = float(stock.iloc[7,1])

        row = pd.Series([tick, price, pe_ratio, 'N/A', 
                        pb_ratio, "N/A", ps_ratio, "N/A",
                        ev_ebitda, "N/A", ev_gross, "N/A", "N/A"], index = my_columns)
        value_df = pd.concat([value_df, row.to_frame().T], ignore_index=True)
    except:
        print("Error with: ", tick)


## Dealing with missing data
for column in ["P/E Ratio","P/B Ratio", "P/Sales Ratio","EV/EBITDA Ratio","EV/Gross Ratio"]:
    value_df[column].fillna(value_df[column].mean(), inplace=True)


## Calculate the percentiles
metrics = {
    "P/E Ratio" : "P/E Percentile",
    "P/B Ratio" : "P/B Percentile",
    "P/Sales Ratio" : "P/Sales Percentile",
    "EV/EBITDA Ratio" : "EV/EBITDA Percentile",
    "EV/Gross Ratio" : "EV/Gross Percentile"
}

for metric in metrics.keys():
    for row in value_df.index:
        value_df.loc[row, metrics[metric]] = stats.percentileofscore(value_df[metric], value_df.loc[row, metric])


## Calculate the robust value score
from statistics import mean

rv_score = []
for row in value_df.index:
    percentiles = []
    for metric in metrics.keys():
        percentiles.append(value_df.loc[row, metrics[metric]])
    
    ## now add the mean to the rv_score list
    rv_score.append(mean(percentiles))

value_df["RV Score"] = rv_score


## Select the top 50
value_df.sort_values("RV Score", ascending=True, inplace=True)
value_df_50 = value_df[:50]
value_df_50.reset_index(inplace=True, drop=True)


# save to file
value_df_50.to_csv("Value_Top_50.csv")