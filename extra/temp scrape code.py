#Note: Fort Drive (#25) was skipped, since it didn't have any listings, (#28, #33)

driver = webdriver.Chrome(executable_path="/Users/admin/Downloads/chromedriver 2") # initiate chrome driver

for i in range(52,74):
    driver.get("https://www.taxpayerservicecenter.com/RP_Search.jsp?search_type=Assessment") #go to OTR landing page

    time.sleep(1) #wait a second
    
    driver.find_element_by_xpath("//*[@id='SearchForm']/table/tbody/tr/td/table[2]/tbody/tr[5]/td[2]/table/tbody/tr/td[1]/select/option[{}]".format(i)).click()
    print('Neighborhood: ', i)
        
    time.sleep(1)
    start_date = driver.find_element_by_name("dtFrom") 
    end_date = driver.find_element_by_name("dtTo") 
    start_date.send_keys("01/01/1990") 
    end_date.send_keys("12/13/2017") 
    
    driver.find_element_by_name("imgSearch").click() #clicks to first listing page
    
    assert "District of Columbia: Search Results" in driver.title #makes sure we're on a search page
    
    last_table = None #last table carries no value
    
    a = 1 #the start of the counter
    
    last_page = False    
    while last_page is False:
        
        html = driver.page_source #scrapes page
        
        soup = BeautifulSoup(html, "lxml") 
        table = soup.find('table', {'cellspacing' : "2"}) #finding number of pages
        
        table_rows = table.find_all('tr')
        
        print(len(table_rows), type(table_rows))
        
        if len(table_rows)<101:
            last_page = True
        
        time.sleep(1)
            
        for j, tr in enumerate(table.find_all('tr'), start = 2): #confirms length of table
            
            try:
                listings = driver.find_element_by_xpath("//*[@id='TABLE1']/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[{}]/td[1]/a".format(j)).click()
                
            except:
                break 
            
            print('listing: ', j-1, " on page ", a)
            
            scrape = driver.page_source #scrapes listing page
            
            soup = BeautifulSoup(scrape, 'lxml')

            home_data = soup.find_all('td', class_= 'RPRowData')
            price = soup.find_all('td', class_= 'RPRightData')

            records = []

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

            records.append((neighborhood, sub_neighborhood, use_code, exception, tax_type, tax_class, homestead, assessor, building_area,
                     ward, land_area, triennial_group, owner_name, address, sale_price, date, instrument_no, sales_code, 
                     sales_type, current_value, new_value, land_2017, land_2018, improvements_2017, improvements_2018, 
                     value_2017, value_2018, assessment_2017, assessment_2018))

            df = pd.DataFrame(records, columns=['neighborhood', 'sub_neighborhood', 'use_code', 'exception', 'tax_type', 'tax_class',
            'homestead', 'assessor', 'building_area', 'ward', 'land_area', 'triennial_group', 'owner_name', 'address',
            'sale_price', 'date', 'instrument_no', 'sales_code', 'sales_type', 'current_value', 'new_value', 'land_2017',
            'land_2018', 'improvements_2017', 'improvements_2018', 'value_2017', 'value_2018', 'assessment_2017',
            'assessment_2018'])
                
            df.to_csv('otr.csv', index = False, mode ='a', header = False, encoding='utf-8')#writes to CSV
            #resource: http://bit.ly/2xF7luv
            print('just saved listing {} to csv'.format(j))

            driver.find_element_by_name("imgPrev_Arrow").click() #go back to listing page
        
#         last_table == table_rows
#         print('last_table == table_rows')
        a+=1 #increase page counter

        if a <= 2:
            driver.find_element_by_xpath("//*[@id='TABLE1']/tbody/tr/td[2]/div/table/tbody/tr[3]/td/font/a[2]").click()
            print("going to listing page {}".format(a)) #clicks to next listing page

        elif a > 3:
            driver.find_element_by_xpath("//*[@id='TABLE1']/tbody/tr/td[2]/div/table/tbody/tr[3]/td/font/a[3]").click()     
            print("going to listing page {}".format(a))
        
        else:
            print("problem clicking through to new listing page")
        

        
            