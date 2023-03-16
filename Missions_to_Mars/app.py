from flask import Flask, render_template, redirect
import pymongo
import scrape_mars



app = Flask(__name__)

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection


db = client.astrology_db
collection = db.mars


@app.route("/")
def index():
    db = client.astrology_db
    collection = db.mars
    # find one document from our mongo db and return it.
    data = list(collection.find())
    for i in data:
        print(i)
        print("-------------------")
    # pass that listing to render_template
    return render_template("index.html", data_mars=data)

# set our path to /scrape
@app.route("/scrape")
def scraper():
    print("scraping clicked")
    # call the scrape function in our scrape_mars file. This will scrape and save to mongo.
    scraped_data = scrape_mars.scrape()
    # update our listings with the data that is being scraped.
    collection.update({}, scraped_data, upsert=True)
    # return a message to our page so we know it was successful.
    print(scraped_data)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
