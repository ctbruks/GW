from bs4 import BeautifulSoup as bs
import pandas as pd
import requests as req
from splinter import Browser
import time


def scrape_urls():

    nasa_url="https://mars.nasa.gov/news/"
    weather_url = "https://twitter.com/marswxreport?lang=en"
    facts_url = "https://space-facts.com/mars/"

    mars = {}

    nasa_response = req.get(nasa_url)
    nasa_soup = bs(nasa_response.text, 'html.parser')
    news_title = nasa_soup.find(class_='content_title').text.strip()
    news_p = nasa_soup.find(class_='rollover_description_inner').text.strip()

    weather_response = req.get(weather_url)
    weather_soup = bs(weather_response.text, 'html.parser')
    mars_weather = weather_soup.find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    facts_url = "https://space-facts.com/mars/"
    facts = pd.read_html(facts_url)
    facts_df = facts[0]
    facts_df.columns = ['description','value']
    facts_df.set_index('description', inplace=True)
    facts_html = facts_df.to_html()

    browser = Browser('chrome', headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    full_image = browser.find_by_id('full_image')
    full_image.click()
    time.sleep(1)
    more_info = browser.find_link_by_partial_text('more info')
    more_info.click()
    html=browser.html
    soup = bs(html, 'html.parser')
    img = soup.find('figure', class_='lede').find('img')['src']
    img_url = 'https://www.jpl.nasa.gov'+ img


    mars["Headline"] = news_title
    mars["Description"] = news_p
    mars["Weather"] = mars_weather
    mars["Facts"] = facts_html
    mars["Image"] = img_url
    
    return mars

