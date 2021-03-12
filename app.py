from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)


conn = "mongodb+srv://rhinkle:Tr@visR0cks@cluster0.gsked.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"