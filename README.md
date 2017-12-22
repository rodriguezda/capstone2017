# Diego's Capstone
Week 12: 9:00 a.m., Friday, December 22

## Problem Statement
The goal of this project is to uncover home availability in Washington DC. I am doing that by analysing data that I scraped [how much data?] from the DC Office of Tax and Revenue website.

The reason I scraped the OTR Property Tax Database is because home sales data is hard to find. Home listing services and aggregators like Zillow do host the estimated price of homes, but they don't provide access to a convenient export of home sales data. They also do not allow scraping. I couldn't find anything at Fannie Mae or Freddie Mac

Articulate “Specific aim”

### Goals and Sucess Criteria
After articulating your problem statement, outline your goals and success criteria.

Has a measurable impact


## Define risks & assumptions

### A Potential Use Case or Audience
Key stakeholders: investors, realtors and homebuyers. Anyone interested in the supply-side of homes. Knowing where and when properties may pan up, take some of the guesswork out of real estate investing. knowing that there will be properties to bid on allows you to focus efforts in that area or during that period of time.

Taking this one step further: I could try to find the neighborhoods with the highest amount of predicted home avails and the lowest mean or median home price. Low home prices are usually driving by economic indicators, like (pre)foreclosure, debt or delinquency, divorce or death. Layering these economic indicators into my model could account for some of the variance. Taht's for round 2 and not part of this assignment!

### About the Data Source
The OTR Property Tax Database

he Office of Tax and Revenue's (OTR) real property tax database provides online access to real property information that was formerly available only through manual searches and at various DC public libraries. You can obtain property value, assessment roll, and other information for more than 180,000 parcels using the links below. 

The Office of Tax and Revenue provides download access to real property files for major customers (not noobs like me). This service is restricted to mortgage companies that pay tax bills for ten (10) or more properties.

Which is why I had to scrape.

### About the Data Set
How many records?

What are the 'predictors?' List them here
neighborhood: clean
subneighborhood: clean
use_code: clean (create a data dictionary for this column)
exception: clean
tax_type: clean (create a data dictionary for this column)
tax_class2: clean (create a data dictionary for this column)
homestead: dummified and column cleaned
assessor: cleaned (titlecase)
building_area: empty (for now. check again once you get the full dataset)
ward: float status. cleaning not needed
land_area: clean (dropped commas)
triennial_group: no cleaning necessary (float)
owner_name: cleaned (converted to title case)
address: cleaned (spend an hour on this!
sale_price: cleaned (dropped commas and dollar signs)
current_value: drop it
new_value: drop it
land_2017: cleaned (dropped commas and dollar signs)
land_2018: cleaned (dropped commas and dollar signs)
improvements_2017: cleaned (dropped commas and dollar signs)
improvements_2018: cleaned (dropped commas and dollar signs)
value_2017: cleaned (dropped commas and dollar signs)
value_2018: cleaned (dropped commas and dollar signs)
assessment_2017: cleaned (dropped commas and dollar signs)
assessment_2018: cleaned (dropped commas and dollar signs)


### Preprocessing
As part of pre-processing, What did I filter for?
Home sales: I confirmed home sales by confirming whether there was a dollar amount in the sales column. homes that did not contain dollar amounts were considered non-transactions and droped from the dataset. since I only care about date, I converted date to index and created a count column to aggregrate sold homes.

Property type: OTR has a codebook for property type. the datset is limited to residential property, things that you and I are most likely to purchase: single family homes, condos, etc. there are at least [X type] of residential properties, and there are over 30 different codes for different property types, some residential, some commercial

Date: I tried to scrape [x amount of records] from as far back as 1990. Unfortunately, OTRs records weren't so great back then, so I adjusted the scrape to 2000. The reason I wanted to go back is to get an account of seasonality before the housing crisis. We saw home price and sales decline started aroudn 2006, so I wanted to get at least a decade behind that just to be safe.

My original hypothesis was that the housing market would not have been hurt as bad in DC. The market is fairly stable here compared to other markets due to the presence of government and military employees. stable jobs, stable pay. for the most part. [talk about the trends that you did notice]

Neighborhoods: According to DC and Google, there are 126 DC neighborhoods. http://dcsmokefreehousing.org/washington-dc-neighborhoods/ The dataset included listings for about 68. OTR had a few massive clusters, called City I and City II, probalby half of the dataset. OTRs classification of neighborhoods was not the same as Googles, so what i had to do was take property addresses, parse them, and send them through a Geocoder to confirm address + neighborhoods. Addresses taht could not be matched were dropped. Listings that could not be categorized by neighborhood were dropped. I should come back to this to make sure that is in fact what I did.


### Why Care about Home Availability?
Mostly for selfish reasons. I am curious about turnover. I want to know where I can expect homes to go on market and when. 

The price of homes is documented and readily available online. They're all estimates?

Additionally, while they model home sales and prices, they gather home sales data from the city. you recently sold your home and your agent has a free Zillow profile, they can log in and manually add the sale information to their Zillow account. This data will then appear on your home property page.

I'm curious about seasonality. If homes were a product, and real estate was one business, I'd be predicting the sales of that business.

### Who sets the price of a home?
Asked another way, why am I not looking at home price data? Who cares about availability? 

In short, the market sets the price. The baseline home value is what your county says it is. County appraisals send you estimates for the land. Realtors give you prices based on comparables (also known as comps). Homeprice aggregators base prices from local, federal and realtor updates.

As consumers, the best thing we can do is know means and medians. If we're buying homes, we should run comparables and be educated on the cost of real estate. And while I scraped appraisal and sales data, and I'll cover it briefly, it's not the main focus of my presentation.

Home prices are affected by several factors. While home prices affect home transactions, there are bigger market forces that affect home prices. Inflation. Taxation. Recession. Unemployment. Natural Disasters. Also not the topic of this presentation, but still itneresting stuff neverheless.

### The modeling Process
Home sales are just like product sales, we can aggregate the number of homes sold per given region and look for trends over time. Originally, I wanted to do a linear regression on the full dataset, which I did, but I also wanted to do prediction via ARIMA. the benefit of arima is that is accounts for variability over time. I'm sure there are many more advantages, but these are the ones that I could think of right now. 

To do Arima, i started with a clean dataset. Next, I 

### Tools Used

Pandas: for analysis
Geocoder: a python package, used for geocoding ( retreiving lats and longs, confirming addresses)
SKLearn and Statsmodels: for linear regression and ARIMA
Seaborn and Tableau: for data visualizations

## Notes, Files and Folders

The repo contains the following folders and content:

00. Preprocessing - This is where I'm storing my csvs and data cleaning.

01. EDA - this is where I am working out of right now. just did initial digging, just to have some info on the page for you guys to see.

02. Models

## My Biggest Obstacles
Time: I put this together yesterday
Data: I started scraping on Saturday. That shit takes forever. I got through about 75% of what I wanted to get through. 
Data: I grabbed the wrong address column. I grabed the mailing address instead of the premise address. which mean some of the addresses are out of state. i had to drop those, they accounted for X. The ones that were instate matched the ones that were 

### The Presentation
Create a 12-15 minute presentation slide deck. This slide deck should be accessible to a wide audience - especially since you'll likely be the only subject-matter expert in the room. However, you'll also want to include details so that we understand your thought process and how well you were able to solve your problem.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Answers to Some Potential Questions
Be prepared to discuss and defend your work... from your choice of dataset to your model-building decisions to your conclusions. They're all fair game!


### Blog Post
Create at least one blog post about your findings.

### Miscellaneous
- might be a good idea to look at how many class 3 properties are increasing over time. Class three is vacant real property, whatever that means
- why are neighborhoods numbered the way they are in the datset?
- https://dcgis.maps.arcgis.com/apps/webappviewer/index.html?id=9a5c11c11dd347cc9c05d64499cc98ee visualizer


## Checklist:
Data collection
Data munging
EDA
Feature engineering
Modeling / machine learning
Model evaluation
Interpretation
Visualizing and communicating results
Be prepared to discuss why the models you chose make sense, and how the data work with it given the goal.

## Presenting
Err on the side of simple over complex
For timing: complex slides will need ~2-3 minutes. Simple slides need 1.
Title your plots with succinct conclusions.
Highlight your inference when presenting multiple outputs
i.e. point out what’s interesting in your graphs
Be sure to visualize, but make sure your visualizations make sense!
PRACTICE! Time yourself. You can get through two runs in about 45 minutes and will help immensely.
SUMMARIZE, SUMMARIZE, SUMMARIZE! Always wrap up your presentation with your problem, your method, and your solution.
Capstone Milestones


Submission Link: https://goo.gl/forms/o05Na7O43SuBP49J3

## Final Presentation
Executive Summary
Identification of outliers
Description of how you defined your variables
Discussion of model selection and implementation
Description of any data pipeline(s)
Visualizations & statistical analysis
Interpretation of findings & relation to goals/success metrics
Description of any source code used to conduct analysis
Stakeholder recommendations & next steps for model/peers
Bonus
Describe how you could continue to validate your model's performance over time
Explain how you would deploy your model in a production environment
Create a blog post of at least 500 words explaining your overall approach, model implementation, specific analysis, findings, and lessons learned. Link to it in your Technical notebook.


## Final product:
- A cleaned Jupyter notebook, ready for posting to your portfolio, that includes:
- a one-paragraph executive summary in a Markdown cell (basically this)
- and all of your final code including any visualizations, models, evaluation, and testing you do.
- The data used to generate your project. (If you are required to mask data for confidentiality reasons, speak with Matt Brems immediately.)
- A .pdf version of your final presentation slides.
- LATER: At least one capstone-related blog post is due by Tuesday, January 2 at 10:00 a.m.

Your slides, notebook, data, and blog post should all be included as part of your final portfolio, due at the time set by Outcomes.