
import requests
from google_api_key import key

search_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"


def main():

    res = requests.get(search_url, params={'key': key, 'input': 'AlphaOne', 'inputtype': 'textquery'})
    response = res.json()
    print(response)
    place_id = response['candidates'][0].get('place_id')
    print(place_id)

    res = requests.get(details_url, params={'key': key, 'placeid': place_id})
    response = res.json()
    print(response)


if __name__ == '__main__':
    main()