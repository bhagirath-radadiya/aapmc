from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from apps.analytics.models import PriceMaster
from datetime import datetime, timedelta
import pandas


chrome_options = webdriver.ChromeOptions()


def get_date_list(start_date, end_date):
    return pandas.date_range(start_date,end_date,freq='d')

def get_crop_price(start_date='2023-01-01', end_date='2023-01-10'):
    
    date_list = get_date_list(start_date=start_date,end_date=end_date)
    print(date_list)
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://apmcgondal.scmsolution.in/Daily_Rate.aspx')
    
    for date in date_list:
        tmp_date = date.strftime('%d/%m/%Y')
        
        driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txt_date").send_keys(tmp_date)
        driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btn_show").click()

        date = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txt_date").get_attribute('value')

        table = driver.find_element(By.XPATH, """//*[@id="ctl00_ContentPlaceHolder1_grid_pak"]""")

        tr_list = table.find_elements(By.TAG_NAME,"tr")

        for row in tr_list[1:]:
            td_list = row.find_elements(By.TAG_NAME, "td")
            
            name = td_list[1].text
            low = td_list[2].text
            high = td_list[3].text
            average = td_list[4].text
            
            print(name,low,high,average)
            
            obj, created = PriceMaster.objects.get_or_create(name=name, category='crop', date=datetime.strptime(date, '%Y-%m-%d'))
            obj.high=high
            obj.low=low
            obj.average=average
            obj.save()
            
    driver.quit()

def get_veg_price(start_date='2023-01-01', end_date='2023-01-10'):
    
    date_list = get_date_list(start_date=start_date,end_date=end_date)
    print(date_list)
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://apmcgondal.scmsolution.in/Daily_Rates_Veg.aspx')
    
    for date in date_list:
        tmp_date = date.strftime('%d/%m/%Y')
        
        driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txt_date").send_keys(tmp_date)
        driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btn_show").click()

        date = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txt_date").get_attribute('value')

        table = driver.find_element(By.XPATH, """//*[@id="ctl00_ContentPlaceHolder1_grid_veg"]""")

        tr_list = table.find_elements(By.TAG_NAME,"tr")

        for row in tr_list[1:]:
            td_list = row.find_elements(By.TAG_NAME, "td")
            
            name = td_list[1].text
            low = td_list[2].text
            high = td_list[3].text
            average = td_list[4].text
            
            print(name,low,high,average)

            obj, created = PriceMaster.objects.get_or_create(name=name, category='veg', date=datetime.strptime(date, '%Y-%m-%d'))
            obj.high=high
            obj.low=low
            obj.average=average
            obj.save()
            
    driver.quit()

def get_fruit_price(start_date='2023-01-01', end_date='2023-01-10'):
    
    date_list = get_date_list(start_date=start_date,end_date=end_date)
    print(date_list)
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://apmcgondal.scmsolution.in/Daily_Rates_Fruits.aspx')
    
    for date in date_list:
        tmp_date = date.strftime('%d/%m/%Y')
        
        driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txt_date").send_keys(tmp_date)
        driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btn_show").click()

        date = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txt_date").get_attribute('value')

        table = driver.find_element(By.XPATH, """//*[@id="ctl00_ContentPlaceHolder1_grid_frt"]""")

        tr_list = table.find_elements(By.TAG_NAME,"tr")

        for row in tr_list[1:]:
            td_list = row.find_elements(By.TAG_NAME, "td")
            
            name = td_list[1].text
            low = td_list[2].text
            high = td_list[3].text
            average = td_list[4].text
            
            print(name,low,high,average)

            obj, created = PriceMaster.objects.get_or_create(name=name, category='fruit', date=datetime.strptime(date, '%Y-%m-%d'))
            obj.high=high
            obj.low=low
            obj.average=average
            obj.save()
            
            
    driver.quit()
    