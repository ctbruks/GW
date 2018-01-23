from bs4 import BeautifulSoup as bs
import pandas as pd
import requests as req
from splinter import Browser


# In[32]:

#url of page
nasa_url="https://mars.nasa.gov/news/"


# In[33]:

#Retrieve the page that will be scraped
nasa_response = req.get(nasa_url)

#make BS object
nasa_soup = bs(nasa_response.text, 'html.parser')


# In[34]:

news_title = nasa_soup.find(class_='content_title').text.strip()
news_p = nasa_soup.find(class_='rollover_description_inner').text.strip()


# In[35]:

print(news_title + "\n")
print(news_p)


# In[37]:

weather_url = "https://twitter.com/marswxreport?lang=en"
weather_response = req.get(weather_url)
weather_soup = bs(weather_response.text, 'html.parser')


# In[38]:

mars_weather = weather_soup.find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text


# In[39]:

facts_url = "https://space-facts.com/mars/"
facts = pd.read_html(facts_url)


# In[40]:

facts_df = facts[0]
facts_df.columns = ['description','value']
facts_df.set_index('description', inplace=True)


# In[42]:

facts_df


# In[41]:

facts_html = facts_df.to_html()
facts_html


# In[96]:

browser = Browser('chrome', headless=False)
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[84]:

full_image = browser.find_by_id('full_image')
full_image.click()


# In[85]:

more_info = browser.find_link_by_partial_text('more info')
more_info.click()


# In[ ]:

html=browser.html
soup = bs(html, 'html.parser')


# In[86]:

img = soup.find('figure', class_='lede').find('img')['src']


# In[87]:

img_url = f'https://www.jpl.nasa.gov{img}'
print(img_url)

