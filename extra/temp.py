# import our necessary first packages

from selenium import webdriver
from bs4 import BeautifulSoup
import urllib
import re
import time

import pandas as pd
df = pd.DataFrame(columns=[
'neighborhood',
'sub_neighborhood',
'use_code',
'exception',
'tax_type',
'tax_class',
'homestead',
'assessor',
'building_area', #Blank 
'ward',
'land_area',
'triennial_group',
'owner_name',
'address',
'sale_price', #maybe blank
'date',
'instrument_no',
'sales_code',
'sales_type',
'current_value',
'new_value',
'land_2017',
'land_2018',
'improvements_2017',
'improvements_2018',
'value_2017',
'value_2018',
'assessment_2017',
'assessment_2018'])


#elem = driver.find_element_by_xpath("//SELECT[@name='selectNbhdCode']/option[text()={}]".format('"Barry Farms"')).click()
#american university
driver = webdriver.Chrome(executable_path="/Users/admin/Downloads/chromedriver")
driver.get("https://www.taxpayerservicecenter.com/RP_Search.jsp?search_type=Assessment")
#time.sleep(5)
#for i in range(2):#,73):
#driver.find_element_by_xpath("//*[@id='SearchForm']/table/tbody/tr/td/table[2]/tbody/tr[5]/td[2]/table/tbody/tr/td[1]/select/option[{}]".format('"i"')).click()
driver.find_element_by_xpath("//*[@id='SearchForm']/table/tbody/tr/td/table[2]/tbody/tr[5]/td[2]/table/tbody/tr/td[1]/select/option[2]").click()
#this will pick the first neighborhood from the dropdown, which is American
start_date = driver.find_element_by_name("dtFrom") #calling start date
end_date = driver.find_element_by_name("dtTo") #calling end date
start_date.send_keys("01/01/1980") #creating start date
end_date.send_keys("12/13/2017") #creating end date
driver.find_element_by_name("imgSearch").click() 
#clicks to first page



#assert "District of Columbia: Search Results" in driver.title
#makes sure we're on a search page
html = driver.page_source #scrapes page
soup = BeautifulSoup(html, "lxml") #do not add prettify here
table = soup.find('table', {'cellspacing' : "2"})
length =len(table.find_all('tr')) #confirms length of table 
length


   
#for i in range(2, length): #let's start iterating through the table, click into page
listings = driver.find_element_by_xpath("//*[@id='TABLE1']/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/a").click()
#listings = driver.find_element_by_xpath("//*[@id='TABLE1']/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[{}]/td[1]/a".format('"i"')).click()

#first listing 
time.sleep(1)
scrape = driver.page_source #scrape 

soup = BeautifulSoup(scrape, 'lxml')
#table = soup.find_all('div', class_="contentPadding")

home_data = soup.find_all('td', class_= 'RPRowData')
for item in home_data:
    try:
        neighborhood = home_data[0].text
    except:
        neighborhood = np.NaN
    try:
        sub_neighborhood = home_data[1].text
    except:
        sub_neighborhood = np.NaN
    try:
        use_code  = home_data[2].text.replace('\n', '').replace('\t', '')
    except:
        use_code = np.NaN
    try:
        exception  = home_data[3].text
    except:
        exception = np.NaN
    try:
        tax_type  = home_data[4].text.replace('\n', '').replace('\t', '')
    except:
        tax_type = np.NaN
    try:
        tax_class  = home_data[5].text.replace('\n', '').replace('\t', '')
    except:
        tax_class = np.NaN
    try:
        homestead  = home_data[6].text
    except:
        homestead = np.NaN
    try:
        assessor  = home_data[7].text
    except:
        assessor = np.NaN
    try:
        building_area  = home_data[8].text
    except:
        building_area = np.NaN
    try:
        ward  = home_data[9].text
    except:
        ward = np.NaN
    try:
        land_area  = home_data[10].text
    except:
        land_area = np.NaN
    try:
        triennial_group  = home_data[11].text
    except:
        triennial_group = np.NaN
    try:
        owner_name  = home_data[12].text
    except:
        owner_name = np.NaN
    try:
        address  = home_data[13].text
    except:
        address = np.NaN
    try:
        sale_price  = home_data[14].text
    except:
        sale_price = np.NaN
    try:
        date  = home_data[15].text
    except:
        date = np.NaN
    try:
        instrument_no  = home_data[16].text
    except:
        instrument_no = np.NaN
    try:
        sales_code  = home_data[17].text
    except:
        sales_code = np.NaN
    try:
        sales_type  = home_data[18].text
    except:
        sales_type = np.NaN
        
price = soup.find_all('td', class_= 'RPRightData')
for item in price:
    try:
        current_value = price[0].text
    except:
        current_value = np.NaN
    try:
        new_value = price[1].text
    except:
        new_value = np.NaN
    try:
        land_2017 = price[2].text
    except:
        land_2017 = np.NaN
    try:
        land_2018 = price[3].text
    except:
        land_2018 = np.NaN
    try:
        improvements_2017 = price[4].text
    except:
        improvements_2017 = np.NaN
    try:
        improvements_2018 = price[5].text
    except:
        improvements_2018 = np.NaN
    try:
        value_2017 = price[6].text
    except:
        value_2017 = np.NaN
    try:
        value_2018 = price[7].text
    except:
        value_2018 = np.NaN
    try:
        assessment_2017 = price[8].text
    except:
        assessment_2017 = np.NaN
    try:
        assessment_2018 = price[9].text
    except:
        assessment_2018 = np.NaN
df.loc[len(df)]=[neighborhood, sub_neighborhood, use_code, exception, tax_type, tax_class, homestead, assessor, building_area,
                 ward, land_area, triennial_group, owner_name, address, sale_price, date, instrument_no, sales_code, 
                 sales_type, current_value, new_value, land_2017, land_2018, improvements_2017, improvements_2018, 
                 value_2017, value_2018, assessment_2017, assessment_2018]
df
      



        driver.find_element_by_name("imgPrev_Arrow").click() #go back to listing page
#         i=1
#         for j in listings:
#             i=i+1
#             try:
                # this is the next button to navigate to next listing page
                #//*[@id="TABLE1"]/tbody/tr/td[2]/div/table/tbody/tr[3]/td/font/a[2].format('"j"'))
        driver.find_element_by_xpath("//*[@id='TABLE1']/tbody/tr/td[2]/div/table/tbody/tr[3]/td/font/a[2]").click()


For 
def scrape(self):
    self.load_page()

    for state in states():
        print state

        for district in districts():
            print 2*' ', district

            for project in projects():
                print 4*' ', project



html = driver.page_source #scrapes page
soup = BeautifulSoup(html, "lxml").prettify
#soup.find('table', {'cellspacing' : "2"})


     
#except:
#if next doesn't work, you've reached the last page. Go back to homepage
#driver.get("https://www.taxpayerservicecenter.com/RP_Search.jsp?search_type=Assessment")

        
        
    try:
        elem = driver.find_element_by_xpath("//*[@id='TABLE1']/tbody/tr/td[2]/div/table/tbody/tr[3]/td/font/a[{}]".format('"i"')).click()
                                  
    #this is the NEXT button to go to page 2
    #page 2
    elem = driver.find_element_by_xpath("//*[@id='TABLE1']/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/a").click()
    #page 2! this is the same! so the process continues. a lot of repeatable code
    #final page
    elem = driver.find_element_by_xpath("//*[@id='TABLE1']/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/a").click()
    
    #if next doesn't work:
    except:
    driver.get("https://www.taxpayerservicecenter.com/RP_Search.jsp?search_type=Assessment")
    
    driver.close()

    # Ah, pull all the code onto your machine
    driver.page_source
    # This is where you get that sweet, sweet data
    # Sort it with some BeautifulSoup tools and store it away!



html = driver.get(#scrapes 
soup = BeautifulSoup(html, "lxml").prettify
table = soup.find('table', {'cellspacing' : "2"})
length = len(table.find_all('tr')) #confirms length of table 


for content in html.find_all('div', {'class':'result content-section-list-row cf with-times'}):
    print(content.find('div', {'class':'booking'}))


import selenium.webdriver.support.ui as UI

def test_text_saver(self):
    driver = self.driver
    wait = UI.WebDriverWait(driver, 5000)
    with open("textsave.txt","w") as textsave:
        list_of_links = driver.find_elements_by_xpath("//*[@id=\"learn-sub\"]/div[4]/div/div/div/div[1]/div[2]/div/div/ul/li/a")
        for link in list_of_links:  # 2
            link.click()   # 1
            text = wait.until(
                lambda driver: driver.find_element_by_xpath("//*[@id=\"learn-sub\"]/div[4]/div/div/div/div[1]/div[1]/div[1]/h1").text)
            textsave.write(text+"\n\n")
            driver.back()


click into the page. 
identify length of table
    for the length of the table:
        click in to each link
        scrape each link
        click backward
    try: click next page
    identify length of table
    for the length of the table:
        click in to each link
        scrape each link
        click backward
    try: click next page


pages_remaining = True
 
while pages_remaining:
    #DO YOUR THINGS WITHIN THE PAGE
 
    try:
        #Checks if there are more pages with links
        next_link = driver.find_element_by_xpath('//a[img/@title="next"]')
        next_link.click()
        time.sleep(30)
    except NoSuchElementException:
        rows_remaining = False


#gets to the next page!
#then we have to click into the first record 
#then we scrape everything in the first record subpage
#then we back out of subpage, and we scrape the next record...
#...
#finally, when we are done with the last record, we click on the "next" link, and the process repeats
#...
#when we get to the last page and the last entry, we're not going to be able to click on next, so set up next as a try and accept statement and throw the except to go to this link: 
#then repeat the process and select a new neighborhood to scrape
#make sure to update the dates and then repeat 
#continue = driver.find_element_by_name('continue')



# # if we find the element we want, we print it. Otherwise, we print 'ZERO'
# for entry in html.find_all('div', {'class':'result content-section-list-row cf with-times'}):
#     try:
#         print(entry.find('div', {'class':'booking'}).text)
#     except:
#         print((0))


# # I'm going to create my empty df first
# import pandas as pd
# dc_eats = pd.DataFrame(columns=["name","location","price","bookings"])


# # loop through each entry
# for entry in html.find_all('div', {'class':'result content-section-list-row cf with-times'}):
#     # grab the name
#     name = entry.find('span', {'class': 'rest-row-name-text'}).text
#     # grab the location
#     location = entry.find('span', {'class': 'rest-row-meta--location rest-row-meta-text'}).text
#     # grab the price
#     try:
#         price = entry.find('i').text.count('$')
#     except:
#         price = "Didnt find price"
#     # try to find the number of bookings
#     try:
#         temp = entry.find('div', {'class':'booking'}).text
#         match = re.search(r'\d+', temp)
#         if match:
#             bookings = match.group()
#     except:
#         bookings = 0
#     # add to df
#     dc_eats.loc[len(dc_eats)]=[name, location, price, bookings]



# check out our work
dc_eats



# all at once:
driver = webdriver.Chrome(executable_path="/Users/joeklein/Downloads/chromedriver")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()