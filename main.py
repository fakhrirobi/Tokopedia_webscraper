from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


#importing edge webdriver 

driver = webdriver.Chrome(r'C:/Users/fakhri.robi/webdriver/bin/chromedriver.exe')

search_item = 'sepeda'
def generate_url(search_item) : 
    url = 'https://www.tokopedia.com/search?st=product&q={}&navsource=home'.format(search_item)
    return url 

driver.get(generate_url(search_item))

#extracting html page from the search query 
#page 1
#locating how many number of pages






driver.page_source
soup = BeautifulSoup(driver.page_source,'html.parser')




yield_result = {}

len(results)


#yield_result['price']  = results[0].find('div',{'class' : 'css-rhd610'}).text
yield_result
def extract_record() : 
    results = soup.find_all('div',{'class':'css-7fmtuv'})
    for result in results : 
        desc = result.find('div', 'css-18c4yhp').text
        price  = result.find('div' , 'css-rhd610').text
        compiled = (desc,price)
    return compiled
    
    # parent_detail = result.find('div','css-vogbyu')
    # parent_detail
    # loc = result.find('span','css-1mv2cn2').text
    
yield_result   
    




    
    #cashback availability 
    # try : 
    #     yield_result['cashback_availability'] = result.find('div',{'class':'css-1a4ihta'}).text
    # except AttributeError : 
    #     yield_result['cashback_availability']  = ''
    # #product details part like rating and num of sales
    # more_details = result.find('div',{'class' : 'css-d0wwk7'})
    
    # yield_result['rating'] = more_details.find('span',{'class' : 'css-etd83i'}).text
    # yield_result['num_of_sales'] = more_details.find('span',{'class' : 'css-1mv2cn2'}).text 
    # yield_result['seller_location'] = result.find('span',{'class' : 'css-4pwgpi'}).text
#session after page 1 done



def scrap_multipages(search_item,num_page) : 
    url = 'https://www.tokopedia.com/search?navsource=home&page={num_page}&q={search_item}&st=product'
    return url 

pagination_len = soup.find_all('button',{'class':'css-k21wea-unf-pagination-item e19tp72t1'})
pagination_len
button_values = [x.text for x in pagination_len]
button_values = [x.replace('.','') for x in button_values ]
button_values = [int(x) for x in button_values]
button_values


max_pages = max (button_values)
max_pages

for i in range((max_pages)+1) : 
    driver.get(scrap_multipages('payung',i))
    driver.page_source
    soup = BeautifulSoup(driver.page_source,'html.parser')
    results = soup.find_all('div',{'class':'css-1g20a2m'})
    for result in results : 
        yield_result['product_desc'] = result.find('div', 'css-18c4yhp').text
        yield_result['price']  = result.find('div' , 'css-rhd610').text
        yield_result['price']  = result.find('div' , 'css-rhd610').text

    print('page', str(i))
yield_result
    

    yield_result['price']  = result.find('div',{'class' : 'css-rhd610'}).text
    yield_result['product_desc'] = result.find('div',{'class' : 'css-18c4yhp'}).text
    #cashback availability 
    yield_result['cashback_availability'] = result.find('div',{'class':'css-1a4ihta'}).text
    
    #product details part like rating and num of sales
    more_details = result.find('div',{'class' : 'css-d0wwk7'})
    
    yield_result['rating'] = more_details.find('span',{'class' : 'css-etd83i'}).text
    yield_result['num_of_sales'] = more_details.find('span',{'class' : 'css-1mv2cn2'}).text 
    yield_result['seller_location'] = result.find('span',{'class' : 'css-4pwgpi'}).text


data = pd.DataFrame(yield_result,columns=['product','desc'])

data.to_csv('data.csv',index=False)
