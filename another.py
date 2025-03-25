import requests

bearer_token = "YOUR_BEARER_TOKEN"
headers = {"Authorization": f"Bearer {bearer_token}"}
woeid = 23424977  # USA

url = f"https://api.twitter.com/1.1/trends/place.json?id={woeid}"
response = requests.get(url, headers=headers).json()

for trend in response[0]['trends'][:10]:
    print(trend['name'])