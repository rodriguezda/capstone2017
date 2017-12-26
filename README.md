# Diego's Capstone
Due: Week 12: 9:00 a.m., Friday, December 22

## Problem Statement
The goal of this project is to forecast home availability in Washington DC. I am doing that by analysing data that I scraped from the DC Office of Tax and Revenue website, which consists of over 50,000 unique property listings over a 17 year timespan (2000-2017).

The reason I scraped the OTR Property Tax Database is because home sales data is hard to find. Home listing services and aggregators like Zillow do host the estimated price of homes, but they don't provide access to a convenient export of home sales data. They also do not allow scraping. I couldn't find any pubic resources or repositories from the Federal Reserve, Fannie Mae or Freddie Mac.

My original hypothesis was that the housing market would not have been hurt as bad in DC, and that we'd see a steady incline of home sales and home prices over time. The market is fairly stable here  in DC compared to other markets due to the presence of government and military employees and jobs.

## Current Success Criteria
I define a successful project by the following criteria:
- Able to pinpoint neighborhood(s) that have or are projected to have homes for sale
- Able to produce a model that forecasts
- Able to visually show trends in home availability (through EDA)

## Future Success Criteria (for the Spotlight)
- Provide specific availability and pricing metrics for different DC neighborhoods
- Present metrics in a visual and interactive format (such as a website built with Flask or a Tableau Dataset) that provide forecasts for home availability and pricing per neighborhood).

## A Potential Use Case or Audience
Key stakeholders: investors, realtors and homebuyers. Anyone interested in the supply-side of homes. Knowing where and when properties may pan up, take some of the guesswork out of real estate investing. knowing that there will be properties to bid on allows you to focus efforts in that area or during that period of time.

Taking this one step further, for the Spotlight: I could try to find the neighborhoods with the highest amount of predicted home avails and the lowest mean or median home price. Low home prices are usually driving by economic indicators, like (pre)foreclosure, debt or delinquency, divorce or death. Layering these economic indicators into my model could account for some of the variance. That's for round 2 and not part of this assignment!

## About the Data Source, The OTR Property Tax Database
The Office of Tax and Revenue's (OTR) real property tax database provides online access to real property information that was formerly available only through manual searches and at various DC public libraries. You can obtain property value, assessment roll, and other information for more than 180,000 parcels using the links below. 

The Office of Tax and Revenue provides download access to real property files for major customers (not noobs like me). This service is restricted to mortgage companies that pay tax bills for ten (10) or more properties. Which is why I had to scrape.

### Preprocessing
Home sales: I confirmed home sales by confirming whether there was a dollar amount in the sales column. homes that did not contain dollar amounts were considered non-transactions and droped from the dataset. since I only care about date, I converted date to index and created a count column to aggregrate sold homes.

Property type: I limited the datset to residential property, properties that you and I are most likely to purchase or be interested in: single family homes, condos, etc. there are at least 10 types of residential properties, and there are over 30 different codes for different property types, some residential, some commercial, so I had to filter out a lot of listings.

Timeframe: I tried to scrape 180,000 records from as far back as 1990. Unfortunately, OTRs records weren't so great back then, so I adjusted the scrape to 2000. The reason I wanted to go back is to get an account of seasonality before the housing crisis. In case home prices and sales declined during the timeframe of the US housing market, my original goal was to get at least a decades worth of additional data just to be safe.

### Why Care about Home Availability?
I'm curious about seasonality, home turnover, and the strength of the real estate market in the Washington, DC area. Knowing about seasonal availability in DC will let me be a more effective homebuyer/investor down the road.

### Who sets the price of a home?
Asked another way, why am I not looking at home price data? Who cares about availability? 

In short, the market sets the price. The baseline home value is what your county says it is. County appraisals send you estimates for the land. Realtors give you prices based on comparables (also known as comps). Homeprice aggregators base prices from local, federal and realtor updates. As consumers, the best thing we can do is know means and medians. If we're buying homes, we should run comparables and be educated on the cost of real estate. And while I scraped appraisal and sales data, and I'll cover it briefly, it's not the main focus of my presentation. Home prices are affected by several factors. While home prices affect home transactions, there are bigger market forces that affect home prices. Inflation. Taxation. Recession. Unemployment. Natural Disasters. Also not the topic of this presentation, but still itneresting stuff neverheless.

### The Model Process
Home sales are just like product sales, we can aggregate the number of homes sold per given region and look for trends over time. Originally, I wanted to do a linear regression on the full dataset, which I did, but I also wanted to do prediction via ARIMA. the benefit of arima is that is accounts for variability over time. I'm sure there are many more advantages, but these are the ones that I could think of right now. 

To build my model, I started with a dataset that I cleaned. Next, I stationarized the data by taking a first difference of the data, taking a seasonal difference to remove the seasonality of the data, and then taking the first difference of the seasonal difference. This gave me a Test Statistic that was greater than the Critical Value. I then selected the appropriate AR, MA, SAR, and MAR terms for the model using ACF and PACF charts that accounted for those three seasonal differences noted previously. I used a function that fitted SARIMAX models using all possible combinations of parameters, and then selected the model with the smallest sum of squared errors.

### Outocome
I was able to produce a model that closely follows the trends of the housing market from 2000-2017, and provides forecasts for future timeframes. 

### Tools Used

Pandas: for analysis
Geocoder: a python package, used for geocoding ( retreiving lats and longs, confirming addresses)
SKLearn and Statsmodels: for linear regression and ARIMA/SARIMAX
Seaborn and Tableau: for data visualizations

## Notes, Files and Folders

The repo contains the following folders and content:

00. Preprocessing - This is where I'm storing my csvs and data cleaning.
01. EDA - this is where I am working out of right now. just did initial digging, just to have some info on the page for you guys to see.
02. Models
03. Extra (scratch work)

### The Presentation
Included in the folder "presentation".

### Blog Post
I am creating at least one blog post about my findings. TBD

### Next Steps
TBD. But there are many things I'd like to tackle next. I'll build this section out soon.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
