#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# <h1>Extracting and Visualizing Stock Data</h1>
# <h2>Description</h2>
# 

# Extracting essential data from a dataset and displaying it is a necessary part of data science; therefore individuals can make correct decisions based on the data. In this assignment, you will extract some stock data, you will then display this data in a graph.
# 

# <h2>Table of Contents</h2>
# <div class="alert alert-block alert-info" style="margin-top: 20px">
#     <ul>
#         <li>Define a Function that Makes a Graph</li>
#         <li>Question 1: Use yfinance to Extract Stock Data</li>
#         <li>Question 2: Use Webscraping to Extract Tesla Revenue Data</li>
#         <li>Question 3: Use yfinance to Extract Stock Data</li>
#         <li>Question 4: Use Webscraping to Extract GME Revenue Data</li>
#         <li>Question 5: Plot Tesla Stock Graph</li>
#         <li>Question 6: Plot GameStop Stock Graph</li>
#     </ul>
# <p>
#     Estimated Time Needed: <strong>30 min</strong></p>
# </div>
# 
# <hr>
# 

# ***Note***:- If you are working Locally using anaconda, please uncomment the following code and execute it.
# Use the version as per your python version.
# 

# In[2]:


get_ipython().system('pip install yfinance')
get_ipython().system('pip install bs4')
get_ipython().system('pip install nbformat')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install pandas')
get_ipython().system('pip install lxml')
get_ipython().system('pip install beautifulsoup4')
get_ipython().system('pip install requests')


# In[1]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup


# In Python, you can ignore warnings using the warnings module. You can use the filterwarnings function to filter or ignore specific warning messages or categories.
# 

# In[3]:


import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)


# ## Define Graphing Function
# 

# In this section, we define the function `make_graph`. **You don't have to know how the function works, you should only care about the inputs. It takes a dataframe with stock data (dataframe must contain Date and Close columns), a dataframe with revenue data (dataframe must contain Date and Revenue columns), and the name of the stock.**
# 

# In[7]:


# The make_graph function has been modified to use Matplotlib for static graphs. Earlier, it used Plotly to generate interactive dashboards, which caused issues when uploading the notebook in the MARK assignment submission.



import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data, stock):
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Stock price
    axes[0].plot(pd.to_datetime(stock_data_specific.Date), stock_data_specific.Close.astype("float"), label="Share Price", color="blue")
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    # Revenue
    axes[1].plot(pd.to_datetime(revenue_data_specific.Date), revenue_data_specific.Revenue.astype("float"), label="Revenue", color="green")
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()


# Use the make_graph function that we’ve already defined. You’ll need to invoke it in questions 5 and 6 to display the graphs and create the dashboard. 
# > **Note: You don’t need to redefine the function for plotting graphs anywhere else in this notebook; just use the existing function.**
# 

# ## Question 1: Use yfinance to Extract Stock Data
# 

# Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is Tesla and its ticker symbol is `TSLA`.
# 

# In[13]:


get_ipython().system('pip install yfinance')
get_ipython().system('pip install bs4')
get_ipython().system('pip install nbformat')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install pandas')
get_ipython().system('pip install lxml')
get_ipython().system('pip install beautifulsoup4')
get_ipython().system('pip install requests')



import yfinance as yf
tesla = yf.Ticker("TSLA")


# Using the ticker object and the function `history` extract stock information and save it in a dataframe named `tesla_data`. Set the `period` parameter to ` "max" ` so we get information for the maximum amount of time.
# 

# In[14]:


tesla_data = tesla.history(period = "max")


# **Reset the index** using the `reset_index(inplace=True)` function on the tesla_data DataFrame and display the first five rows of the `tesla_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 1 to the results below.
# 

# In[15]:


tesla_data.reset_index(inplace=True)
tesla_data.head()


# ## Question 2: Use Webscraping to Extract Tesla Revenue Data
# 

# Use the `requests` library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm Save the text of the response as a variable named `html_data`.
# 

# In[16]:


import requests 
from bs4 import BeautifulSoup

url = " https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

html_data = requests.get(url).text


# Parse the html data using `beautiful_soup` using parser i.e `html5lib` or `html.parser`.
# 

# In[6]:


soup =BeautifulSoup (html_data,"html.parser")


# Using `BeautifulSoup` or the `read_html` function extract the table with `Tesla Revenue` and store it into a dataframe named `tesla_revenue`. The dataframe should have columns `Date` and `Revenue`.
# 

# <details><summary>Step-by-step instructions</summary>
# 
# ```
# 
# Here are the step-by-step instructions:
# 
# 1. Create an Empty DataFrame
# 2. Find the Relevant Table
# 3. Check for the Tesla Quarterly Revenue Table
# 4. Iterate Through Rows in the Table Body
# 5. Extract Data from Columns
# 6. Append Data to the DataFrame
# 
# ```
# </details>
# 

# <details><summary>Click here if you need help locating the table</summary>
# 
# ```
#     
# Below is the code to isolate the table, you will now need to loop through the rows and columns like in the previous lab
#     
# soup.find_all("tbody")[1]
#     
# If you want to use the read_html function the table is located at index 1
# 
# We are focusing on quarterly revenue in the lab.
# ```
# 
# </details>
# 

# In[17]:


import pandas as pd 

tables = pd.read_html(url)

tesla_revenue = tables[1]

tesla_revenue.columns = ["Date","Revenue"]

tesla_revenue.head()


# Execute the following line to remove the comma and dollar sign from the `Revenue` column. 
# 

# In[18]:


tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"",regex=True)


# Execute the following lines to remove an null or empty strings in the Revenue column.
# 

# In[19]:


tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


# Display the last 5 row of the `tesla_revenue` dataframe using the `tail` function. Take a screenshot of the results.
# 

# In[20]:


tesla_revenue.tail()


# ## Question 3: Use yfinance to Extract Stock Data
# 

# Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is GameStop and its ticker symbol is `GME`.
# 

# In[22]:


import yfinance as yfinance
gme = yf.Ticker("GME")


# Using the ticker object and the function `history` extract stock information and save it in a dataframe named `gme_data`. Set the `period` parameter to ` "max" ` so we get information for the maximum amount of time.
# 

# In[24]:


gme_data = gme.history(period = "max")


# **Reset the index** using the `reset_index(inplace=True)` function on the gme_data DataFrame and display the first five rows of the `gme_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 3 to the results below.
# 

# In[25]:


gme_data.reset_index(inplace = True)
gme_data.head()


# ## Question 4: Use Webscraping to Extract GME Revenue Data
# 

# Use the `requests` library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html. Save the text of the response as a variable named `html_data_2`
# 

# In[27]:


url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

html_data_2 = requests.get(url2).text


# Parse the html data using `beautiful_soup` using parser i.e `html5lib` or `html.parser`.
# 

# In[29]:


soup2 = BeautifulSoup(html_data_2,"html.parser")


# Using `BeautifulSoup` or the `read_html` function extract the table with `GameStop Revenue` and store it into a dataframe named `gme_revenue`. The dataframe should have columns `Date` and `Revenue`. Make sure the comma and dollar sign is removed from the `Revenue` column.
# 

# > **Note: Use the method similar to what you did in question 2.**  
# 

# <details><summary>Click here if you need help locating the table</summary>
# 
# ```
#     
# Below is the code to isolate the table, you will now need to loop through the rows and columns like in the previous lab
#     
# soup.find_all("tbody")[1]
#     
# If you want to use the read_html function the table is located at index 1
# 
# 
# ```
# 
# </details>
# 

# In[43]:


rows = []
table = soup2.find_all("tbody")[1]
for row in table.find_all("tr"):
    cols = row.find_all("td")
    if len(cols)>=2:
        rows.append({"Date":cols[0].text.strip(),"Revenue":cols[1].text.strip()})

gme_revenue = pd.DataFrame(rows,columns=["Date","Revenue"])


# Remove the comma and dollar sign, an null or empty strings from the Revenue column.
# 

# In[45]:


gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(',|\$',"",regex = True)
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue']!=""] 


# Display the last five rows of the `gme_revenue` dataframe using the `tail` function. Take a screenshot of the results.
# 

# In[46]:


gme_revenue.tail()


# ## Question 5: Plot Tesla Stock Graph
# 

# Use the `make_graph` function to graph the Tesla Stock Data, also provide a title for the graph. Note the graph will only show data upto June 2021.
# 

# <details><summary>Hint</summary>
# 
# ```
# 
# You just need to invoke the make_graph function with the required parameter to print the graphs.The structure to call the `make_graph` function is `make_graph(tesla_data, tesla_revenue, 'Tesla')`.
# 
# ```
#     
# </details>
# 

# ## Question 6: Plot GameStop Stock Graph
# 

# In[47]:


make_graph(tesla_data,tesla_revenue,'Tesla')


# Use the `make_graph` function to graph the GameStop Stock Data, also provide a title for the graph. The structure to call the `make_graph` function is `make_graph(gme_data, gme_revenue, 'GameStop')`. Note the graph will only show data upto June 2021.
# 

# <details><summary>Hint</summary>
# 
# ```
# 
# You just need to invoke the make_graph function with the required parameter to print the graphs.The structure to call the `make_graph` function is `make_graph(gme_data, gme_revenue, 'GameStop')`
# 
# ```
#     
# </details>
# 

# In[48]:


make_graph(gme_data,gme_revenue,'GameStop')


# <h2>About the Authors:</h2> 
# 
# <a href="https://www.linkedin.com/in/joseph-s-50398b136/">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 
# Azim Hirjani
# 

# ## Change Log
# 
# | Date (YYYY-MM-DD) | Version | Changed By    | Change Description        |
# | ----------------- | ------- | ------------- | ------------------------- |
# | 2022-02-28        | 1.2     | Lakshmi Holla | Changed the URL of GameStop |
# | 2020-11-10        | 1.1     | Malika Singla | Deleted the Optional part |
# | 2020-08-27        | 1.0     | Malika Singla | Added lab to GitLab       |
# 
# <hr>
# 

# Copyright © 2020 IBM Corporation. All rights reserved.
# 
