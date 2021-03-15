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

ALLOWED_EXTENSIONS = set(['jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def scrape_info():
    
    # Run chrome driver manager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Define dictionary
    mars = {}

    # MARS NEWS
    mars_news_url = 'https://mars.nasa.gov/news'
    browser.visit(mars_news_url)
    html = browser.html
    mars_soup = BeautifulSoup(html, 'html.parser')

    # Create variable for title and text
    # mars_container = mars_soup.find('div', class_ = 'image_and_description_container')
    resultA = mars_soup.find_all('div', class_ = 'content_title')
    resultB = mars_soup.find('div', class_ = 'article_teaser_body')

    news_title = resultA[1].text.strip()
    news_text = resultB.text.strip()

    # Put variables in dictionary
    mars["news_title"] = news_title
    mars["news_text"] = news_text


    # JPL IMAGES
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

    #put image in dictionary
    mars["featured_image"] = featured_image


    # MARS FACTS
    facts_url = 'https://space-facts.com/mars'
    browser.visit(facts_url)
    facts_soup = BeautifulSoup(html, 'html.parser')

    # Grab table
    facts_table = pd.read_html(facts_url)
    facts_df = facts_table[0]

    # reset index
    facts_df.set_index(0, inplace=True)
    facts_df

    # Name columns
    facts_df.columns = ['Mars']
    facts_df

    #Convert to html
    facts_html = facts_df.to_html()

    # Put html in mars dictionary
    mars['facts_html'] = facts_html


    # HEMISPHERES
    base_url = 'https://astrogeology.usgs.gov'
    astro_url = base_url + '/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astro_url)
    astro_soup = BeautifulSoup(html, 'html.parser')

    # Run loop to grab images
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

    # Put hemisphere image urls into mars dictionary
    mars["hemisphere"]=mars_hemisphere_image_urls 

    print(mars)
    
    browser.quit()

    # Return results
    return mars

if __name__ == "__main__":
    print(scrape_info())