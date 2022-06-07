import requests
import os
import json

bearer_token = "AAAAAAAAAAAAAAAAAAAAAK2HdAEAAAAAEkcy%2FyrzITemi%2BWbc%2FaBBQlyQMs%3DFhI56PYB5zIFjNv1AzFDPWtvvn38PXtkdZHRQenDy9QR3jHxVF"

search_url = "https://api.twitter.com/2/tweets/search/recent"
search_user_info_url = "https://api.twitter.com/2/users/by/username/baniraotalo" #eldianaXxX: 1531036604604862470 baniraotalo: 866791081639366660
search_tweets_by_user_id = "https://api.twitter.com/2/users/866791081639366660/tweets"
place_url = "https://api.twitter.com/1.1/geo/id/fa3435044b52ecc7.json"

# query: parametro pra ver 
query_params = {'query': '#netflix OR #netflixbr', 'tweet.fields': 'author_id,created_at,geo,in_reply_to_user_id,lang,possibly_sensitive,source', 'max_results': 100}

def bearer_oauth(r):
    print(bearer_token)
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    r.headers["Content-Type"] = f"application/x-www-form-urlencoded;charset=UTF-8"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))
    f = open('tweets_pretratados.json', 'w')
    f.write(str(json.dumps(json_response.get('data'), indent=4, sort_keys=True)))
    f.close


if __name__ == "__main__":
    main()