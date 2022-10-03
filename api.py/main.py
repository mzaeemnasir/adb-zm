import requests
import json
import base64

#user and password, and link
url= "http://cryptomarketguides.com/wp-json/wp/v2"
user= "crypto"
password= "sQXX OQJ8 wJC4 fzyx va9e UMD0"

#Encode the connection of your WordPress website
wp_connection = user + ":" + password
token = base64.b64encode(wp_connection.encode())

#Prepare the header of our request
headers = {"Authorization": "Basic " + token.decode("utf-8")}


#title for our first post
post_title = "This is my first post using Python and REST API"
post_body = "This is the body content of first post using Python and REST API"

#Python dictionary
post = {
    "title": post_title,
    "status": "publish",
    "content": post_body,
    "author": "1",
    "format": "standard"
}

#request to post
wp_request = requests.post(url + "/posts", headers=headers, json=post)