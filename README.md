# Mission to Mars: Web Scraping Challenge

The purpose of this project was to scrape data about Mars from 4 different websites and display the scraped data on a local web browser using MongoDB with Flask,

## Scraping
I used Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter to scrape our data. Once I retrieved each item, I stored the results in a dictionary and wrapped the code in a function. 

### Sources:
* [NASA Mars News](https://mars.nasa.gov/news/): retrieve the most recent article title and preview text. 
* [JPL Featured Space Image](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html): retrieve the most recently featured space image.
* [Mars Facts](https://space-facts.com/mars/): retrieve the table of Mars facts.
* [USGS Astrogeology](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars): retrieve high resolution images of each hemisphere. 

## MongoDB & Flask Application
I used Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

## Repository Contents
* Mission_to_Mars
    * app.py
    * mission_to_mars.ipynb
    * scrape_mars.py
    * templates
        * index.html
* App_Screenshot_1.png
* App_Screenshot_2.png
* App_Screenshot_3.png