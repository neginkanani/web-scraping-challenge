from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # Scrape the [Mars News Site](https://redplanetscience.com/) to collect the latest News Title and Paragraph Text.
    #open the website
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    #reading the html code
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #scarping the data 
    latest_news_title = soup.find('div', class_='content_title')
    news_title = latest_news_title.text
    latest_news_paragraph = soup.find('div', class_='article_teaser_body')
    news_paragraph = latest_news_paragraph.text
    time.sleep(1)


    # Visiting the url for the Featured Space Image site [here](https://spaceimages-mars.com)
    # opening hte url in a browser
    url_image='https://spaceimages-mars.com'
    browser.visit(url_image)
    # Reading the html code
    html_image=browser.html
    soup_image=BeautifulSoup(html_image, 'html.parser' )
    #clicking on the full image
    browser.links.find_by_partial_text('FULL IMAGE').click()
    #Finding the html code for the image
    html_image_featured=browser.html
    soup_image_featured=BeautifulSoup(html_image_featured, 'html.parser' )
    #Saving the path to the image
    partial_url_image = soup_image_featured.find('div', class_="floating_text_area").a['href']
    featured_image_url=url_image + "/" + partial_url_image
    time.sleep(1)


    # Visiting the Mars Facts webpage [here](https://galaxyfacts-mars.com) and using Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    #opening the url
    url_fact = 'https://galaxyfacts-mars.com'
    browser.visit(url_fact)
    #finding the html code
    html_fact = browser.html
    soup_fact=BeautifulSoup(html_fact,'html.parser')
    tables_fact = pd.read_html(url_fact)
    #read and clean teh table
    tables_fact_mars = tables_fact[0]
    tables_fact_mars_clean = tables_fact_mars.rename(columns=tables_fact_mars.iloc[0,:])
    tables_fact_mars_clean_final = tables_fact_mars_clean.to_html(index=False).replace("\n","")
    time.sleep(1)

    # Visiting the astrogeology site [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres
    url_ast = 'https://marshemispheres.com/'
    browser.visit(url_ast)
    html_ast = browser.html
    soup_ast = BeautifulSoup(html_ast, 'html.parser')
    # looping through different links to hemisphere information
    # and getting the title and link tot he image into a list with dictionaries
    hemisphere_image_urls=[]
    hemisphere_list= ['Cerberus Hemisphere Enhanced', 'Schiaparelli Hemisphere Enhanced',
                 'Syrtis Major Hemisphere Enhanced', 'Valles Marineris Hemisphere Enhanced']
    for i in hemisphere_list:
        browser.links.find_by_partial_text(i).click()
        html_ast_hem = browser.html
        soup_ast_hem = BeautifulSoup(html_ast_hem, 'html.parser')
        hem = {
        "title" : soup_ast_hem.find('div', class_='cover').h2.text,
        "img_url" : url_ast + soup_ast_hem.find('div', class_='downloads').a['href']
        }
        hemisphere_image_urls.append(hem)
        browser.links.find_by_partial_text('Back').click()
    hemisphere_image_urls

    dict_data={"news_title":news_title,
               "news_paragraph":news_paragraph,
               "featured_image_url":featured_image_url,
               "tables_fact_mars_clean_final":tables_fact_mars_clean_final,
               "hemisphere_image_urls":hemisphere_image_urls
    }

    # Quit the browser
    browser.quit()
    
    return dict_data

