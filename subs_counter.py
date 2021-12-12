import requests
import json
key="AIzaSyBDZWQtwm9pghSAlPo-iFwYlgpQLNAS-P4"
channel_id ="UC2RfVS8qXK9sK-a2IxoxYJA"

params = {

  "key": key,
  "id": channel_id,
  "part":"statistics"
}

endpoint = "https://www.googleapis.com/youtube/v3/channels"

def  get_sub_count():

  response= requests.get(endpoint,params =  params)
  d= json.loads(response.content)
  items = d['items']
  item = items[0]
  statistics = item['statistics']
  sub_count = statistics['subscriberCount']
  print(d)
  return sub_count