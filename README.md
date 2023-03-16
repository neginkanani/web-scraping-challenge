# web-scraping-challenge

In this challenge several websites are being used to prepare a dashboard for a user 

Here are the list of websites:
Mars News Site(https://redplanetscience.com/) to collect the latest News Title and Paragraph Text.
(https://spaceimages-mars.com) to get the featured space image
(https://galaxyfacts-mars.com) to scrape the table containing facts about the planet including Diameter, Mass, etc.
(https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

Finally the information scraped above are passed to MongoDB and being read by Flask templating to create a new HTML page that displays all of the information.