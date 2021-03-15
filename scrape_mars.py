
# Import dependencies
import os
import pandas as pd
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time

def init_browser(): 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()

#Define mars dictionary
mars = {}

# MARS NEWS
# Visit URL
mars_news_url = 'https://mars.nasa.gov/news'
browser.visit(mars_news_url)
html = browser.html
mars_soup = BeautifulSoup(html, 'html.parser')

# Grab Mars news title and tet
news_title = mars_soup.find('div', class_ = 'image_and_description_container').find('div', class_ = 'content_title').text.strip()
news_text = mars_soup.find('div', class_ = 'image_and_description_container').find('div', class_ = 'article_teaser_body').text.strip()

mars["news_title"] = news_title
mars["news_text"] = news_text


# JPL IMAGES
# Visit URL
jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(jpl_url)
time.sleep(.5)
browser.find_link_by_partial_text('FULL IMAGE').click()
html = browser.html

# Parse HTML with Beautiful Soup
jpl_soup = BeautifulSoup(html, 'html.parser')
type(jpl_soup)

# Retrieve all elements that contain image information
mars_image = jpl_soup.find('img', class_='headerimage fade-in')
print('https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/')
mars_image["src"]
featured_image = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'+ mars_image["src"]

# Add to mars dictionary
mars["featured_image"] = featured_image_url


# ## MARS FACTS
facts_url = 'https://space-facts.com/mars'
browser.visit(facts_url)
facts_soup = BeautifulSoup(html, 'html.parser')

#Grab table
facts_table = pd.read_html(facts_url)
facts_table

# Convert to data frame
facts_df = facts_table[0]

# Drop Index
facts_df.set_index(0, inplace=True)
facts_df

# Name columns
facts_df.columns = ['Mars']
facts_df

# Convert to html
facts_html = facts_df.to_html()

mars['facts_html'] = facts_html

# MARS HEMISPHERES
base_url = 'https://astrogeology.usgs.gov'
astro_url = base_url + '/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(astro_url)
astro_soup = BeautifulSoup(html, 'html.parser')

# loop to grab links and put in dictionary
link_list=browser.find_by_css("a.product-item h3")
mars_hemisphere_image_urls = []
for x in range(len(link_list)):
    hemisphere={}
    browser.find_by_css("a.product-item h3")[x].click()
    sample = browser.links.find_by_text("Sample").first
    hemisphere["img_url"]=sample["href"]
    hemisphere["title"]=browser.find_by_css("h2.title").text
    mars_hemisphere_image_urls.append(hemisphere)
    browser.back()
mars_hemisphere_image_urls    
mars["hemisphere"]=mars_hemisphere_image_urls 


browser.quit()
return mars
