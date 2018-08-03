import imghdr

from flask import Flask, render_template, jsonify
import requests
from google_api_key import key

app = Flask(__name__)

search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"

photos_url = "https://maps.googleapis.com/maps/api/place/photo"


@app.route("/", methods=["GET"])
def retreive():
    return render_template('layout.html')


@app.route("/sendRequest/<string:query>")
def results(query):
    search_payload = {"key": key, 'input': query, 'inputtype': 'textquery'}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()
    place_id = search_json['candidates'][0]['place_id']

    # details_payload = {"key": key, "placeid": place_id}
    # details_resp = requests.get(details_url, params=details_payload)
    # details_json = details_resp.json()
    #
    # url = details_json["result"]["url"]
    # return jsonify({'result': url})

    photo_payload = {"key": key, "maxwidth": 500, "maxheight ": 500, "photoreference": place_id}
    photo_request = requests.get(photos_url, params=photo_payload)
    photo_type = imghdr.what("", photo_request.content)
    photo_name = "static/" + query + "." + photo_type

    with open(photo_name, "wb") as photo:
        photo.write(photo_request.content)

    return '<img src=' + photo_name + '>'


if __name__ == "__main__":
    app.run(debug=True)
