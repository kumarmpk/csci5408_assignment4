from pymongo import MongoClient
import re
import json
from bson import json_util
import csv
from dateutil.parser import parse
from datetime import datetime

client = MongoClient(
    'mongodb+srv://user:5408pass3@data-assignment3.xtllw.mongodb.net/ProcessedDb?retryWrites=true&w=majority')

processed_database = client.get_database('ProcessedDb')
search_keyword_list = ["Storm", "Winter", "Canada",
                       "Temperature", "Flu", "Snow", "Indoor", "Safety"]
tweet_text_list = []
regular_expression = re.compile(r'https\S+|([^a-zA-Z\s]+?)')
dot_exp = re.compile(r'\.|\,|\&|\;|\<|\>')
regular_expression = re.compile(
    r'\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8}|https?://(?:[-w.]|(?:%[\da-fA-F]{2}))+|[!@#$]|//?|<.*?>|\\?')
csv_list = []

for keyword_word in search_keyword_list:
    records = processed_database[keyword_word]
    records_cursor = records.find()
    processed_data_list = json.loads(
        json_util.dumps(records_cursor))
    processed_data_list = processed_data_list[:800]

    for tweet in processed_data_list:
        if 'text' in tweet and 'user' in tweet and 'retweet_count' in tweet and tweet['text'].strip() != '':
            user = tweet['user']
            if 'created_at' in user and 'location' in user and user['created_at'].strip() != '' and user['location'].strip() != '':
                text = tweet['text']
                text = dot_exp.sub(r'', text)
                processed_tweet = re.sub(r"http\S+", "", text)
                processed_tweet = regular_expression.sub(r'', processed_tweet)
                if processed_tweet not in tweet_text_list:
                    csv_obj = {}
                    tweet_text_list.append(processed_tweet)
                    created_at_str = tweet['user']['created_at']
                    datetime_obj = parse(created_at_str)
                    timestamp = datetime.timestamp(datetime_obj)
                    csv_obj['created_at'] = timestamp
                    csv_list.append(csv_obj)

print(len(csv_list))
csv_list = csv_list[:3000]
headers = csv_list[0].keys()
with open('R_CSV.csv', 'w', newline='') as r_table:
    writer = csv.DictWriter(r_table, headers)
    writer.writeheader()
    writer.writerows(csv_list)
