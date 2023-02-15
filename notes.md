# Algorithmic Trading # 

The following is a collection of personal notes taken when I was learning of algorithmic trading. 

## What is Algorithmic Trading? ## 

Algorithmic trading is trading with the use of computer software, rather than financial analysts. 

We will use Python as it is the most popular language for algorithmic trading. However, Python is slow and is often used as a gluing language, where Python calls code from other faster languages. 

The process of running a quant investing strategy can be summarised as follows: 

1. Collect Data. 
2. Develop a hypothesis for a strategy. 
3. Backtest that strategy. 
4. Implement the strategy in production.

Some caveats: 

1. Data collected here will be random, unless I pay for an API token to get real market data. 
2. I won't be executing trades unless I learn how to use the API for my custodian.
3. We will be generating order sheets instead. 

***
## API Basics ## 

An API is an application programming interface. APIs allow you to interact with someone else's software using your own code. We will mostly use the IEX Cloud API.  

An overview of API functionality: 

1. **GET**: gets data from the API database. 
2. **POST**: adds data to the database exposed by the API. 
2. **PUT**: Adds and _overwrites_ data in the database exposed by the API. 
3. **Delete**: deletes the data from the API's database. 

To learn about API's, one can use the following link to interact with API's using HTTP requests: 

https://github.com/public-apis/public-apis


*** 

## Momentum Investing ## 

Momentum Investing is the strategy of investing in companies that have increased the most. For instance, suppose AAPL stock increased 35% and MSFT 20%. Then Momentum investing would suggest investing in AAPL because of its higher recent price return. 

There are some nuances to this strategy which we will explore. Like high quality momentum and quantifying what that is. 


## Value Investing ## 

Value Investing is the strategy of investing in stocks which are trading below their perceived intrincic value. This has been popularized by Warren Buffett. 

To create algorithmic value investing strategies relies on a concept called _multiples_. Multiples are calculated by dividing a companies stock price by some other meaningful metric, like assets or earnings. Such examples are: 

1. P/E ratio.
2. Price-to-Book.
3. Price-to-FCF. 

Each of the individual multiples used in value investing has its pros and cons. One way to minimize is by using a _composite_. We'll use a composite of 5 different valuation metrics in our strategy.  


***

## Calling an API ## 

In this example we call from IEX Cloud. We can find the documentation at https://iexcloud.io/docs/api. 

We find the base url by clicking `ctrl+f` and searching for `sandbox`. We then navigate to the `Quote` section which provides market cap and stock price, and we copy the `GET` url. Finally, we must add `?token=IEX_CLOUD_API_TOKEN` to the end of the url to ensure we are given access. 


***








