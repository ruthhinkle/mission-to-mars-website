# Import dependencies
from flask import Flask, render_template, request, redirect
# from config import password
import scrape_mars
from flask_pymongo import PyMongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to index.html
@app.route("/")
def home():
    
    # Find one record from the mongo database
    mars = mongo.db.mars.find_one()

    # Return template and data
    return render_template("index.html", mars=mars)

# Route for scrape function
@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape_info()
    print(mars_data)
    mongo.db.mars.update({}, mars_data, upsert=True)
    

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
