from positive_words import positive_word_list
from negative_words import negative_word_list
from pymongo import MongoClient
import json
import re
from bson import json_util
import collections
import csv

client = MongoClient(
    'mongodb+srv://user:5408pass3@data-assignment3.xtllw.mongodb.net/ProcessDb?retryWrites=true&w=majority')
processed_database = client.get_database('ProcessedDb')
search_keyword_list = ["Storm", "Winter", "Canada",
                       "Temperature", "Flu", "Snow", "Indoor", "Safety"]
tweet_text_list = []

for keyword_word in search_keyword_list:
    records = processed_database[keyword_word]
    records_cursor = records.find()
    processed_data_list = json.loads(
        json_util.dumps(records_cursor))
    processed_data_list = processed_data_list[:400]

    for tweet in processed_data_list:
        if 'text' in tweet:
            tweet_text_list.append(tweet['text'])

tweet_text_list = tweet_text_list[:2000]
record_counter = 0
csv_record_list = []


def createBOW(text):
    words = text.split()
    outDict = {}
    for word in words:
        if word in outDict:
            outDict[word] = outDict[word] + 1
        else:
            outDict[word] = 1
    return outDict


for tweet in tweet_text_list:
    csv_record = {}
    positive_counter = 0
    matched_positive_word_list = ''
    negative_counter = 0
    matched_negative_word_list = ''
    polarity = ''
    words = tweet.split()
    bow = createBOW(tweet)

    record_counter = record_counter + 1

    for word, count in bow.items():
        if word in positive_word_list:
            positive_counter = positive_counter + count
            if matched_positive_word_list == '':
                matched_positive_word_list = word
            else:
                matched_positive_word_list = matched_positive_word_list + ', ' + word
        if word in negative_word_list:
            negative_counter = negative_counter + count
            if matched_negative_word_list == '':
                matched_negative_word_list = word
            else:
                matched_negative_word_list = matched_negative_word_list + ', ' + word

    if positive_counter > negative_counter:
        polarity = 'Positive'
    elif positive_counter < negative_counter:
        polarity = 'Negative'
    else:
        polarity = 'Neutral'

    csv_record['Tweet'] = record_counter
    csv_record['Text'] = tweet
    csv_record['Matched_Positive_Words'] = matched_positive_word_list
    csv_record['Matched_Negative_Words'] = matched_negative_word_list
    csv_record['Polarity'] = polarity
    csv_record_list.append(csv_record)

headers = csv_record_list[0].keys()
with open('sentiment_analysis.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, headers)
    dict_writer.writeheader()
    dict_writer.writerows(csv_record_list)
