import requests
import json
import base64
import datetime

# user and password, and link
url = "http://cryptomarketguides.com/wp-json/wp/v2"
user = "crypto"
password = "WBk5 7PNl ABmn PY2I PB1N QcGd"

# Encode the connection of your WordPress website
wp_connection = user + ":" + password
token = base64.b64encode(wp_connection.encode())

# Prepare the header of our request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {token.decode('utf-8')}",
    "Username": "crypto",
    "Password": token.decode("utf-8"),
}


# title for our first post
post_title = "This is my first post using Python and REST API"
post_body = "This is the body content of first post using Python and REST API"

# Python dictionary
data = {
    "title": "Testing via API via Python",
    "content": "tEST CONTENT OF THE THIS TEST PAGE via PYTHON",
    "status": "publish",
}

# request to post
wp_request = requests.post(url + "/posts", headers=headers, data=json.dumps(data))

print(wp_request)
