from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
#import
app = Flask(__name__)
CORS(app)
# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="aarthika"
)
cursor = db.cursor()

# Check if the connection was successful
try:
    db.ping(reconnect=True)
    print("Connected to the database.")
except mysql.connector.Error as err:
    print("Error connecting to MySQL:", err)



# Home Route
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Aarthika API!"})



if __name__ == '__main__':
    app.run(debug=True)
