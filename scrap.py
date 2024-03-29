from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By  # Import By class

df = pd.DataFrame(columns=['Player','Salary','Year']) # creates master dataframe 

driver = webdriver.Chrome()

for yr in range(1990,1991):
    page_num = str(yr) + '-' + str(yr+1) +'/'
    url = 'https://hoopshype.com/salaries/players/' + page_num
    driver.get(url)
    
    players = driver.find_elements(By.XPATH, '//td[@class="name"]')
    salaries = driver.find_elements(By.XPATH, '//td[@class="hh-salaries-sorted"]') 
    
    players_list = []
    for p in range(len(players)):
        players_list.append(players[p].text)
    
    salaries_list = []
    for s in range(len(salaries)):
        salaries_list.append(salaries[s].text)
    
    data_tuples = list(zip(players_list[1:],salaries_list[1:])) # list of each players name and salary paired together
    # temp_df = pd.DataFrame(data_tuples, columns=['Player','Salary']) # creates dataframe of each tuple in list
    # temp_df['Year'] = yr # adds season beginning year to each dataframe
    data = {'Player': players_list[1:], 'Salary': salaries_list[1:], 'Year': yr}
    df = pd.concat([pd.DataFrame(data)]) # appends to master dataframe
    df.to_csv('output.csv', index=False)

driver.close()