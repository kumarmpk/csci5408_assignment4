from pymongo import MongoClient
import re
import math
import json
from bson import json_util
import collections
import csv

client = MongoClient(
    'mongodb+srv://user:5408pass3@data-assignment3.xtllw.mongodb.net/ReuterDb?retryWrites=true&w=majority')
reuter_database = client.get_database('ReuterDb')
regular_expression = re.compile(r'https\S+|([^a-zA-Z\s]+?)')
dot_exp = re.compile(r'\.|\,|\&|\;|\<|\>')
news_list = []

records = reuter_database['Reuter_Data']
records_cursor = records.find()
news_list = json.loads(
    json_util.dumps(records_cursor))
search_keyword_list = ['Canada', 'rain', 'cold', 'hot']
table1_counters = []
total_documents = len(news_list)
csv_table1 = []

for news in news_list:
    news_str = str(news['body'])
    news_str = dot_exp.sub(r'', news_str)
    news_str = regular_expression.sub(r'', news_str)
    news_str = news_str.replace('reuter', '')
    news_str = news_str.replace('Reuter', '')
    news_str = news_str.replace('REUTER', '')
    news['body'] = news_str

for keyword in search_keyword_list:
    counter_table1 = 0
    csv_record = []
    for news in news_list:
        news_str = str(news['body'])
        words = news_str.split()
        if keyword in words:
            counter_table1 = counter_table1 + 1
    csv_record.append(keyword)
    csv_record.append(counter_table1)
    csv_record.append(str(total_documents) + '/' + str(counter_table1))
    csv_record.append(math.log10(total_documents/counter_table1))
    csv_table1.append(csv_record)
    table1_counters.append(counter_table1)

with open('Table1.csv', 'w', newline='') as table1:
    writer = csv.writer(table1)
    writer.writerow(['Total	Documents', total_documents])
    writer.writerow(['Search Query', 'Document containing term(df)',
                     'Total Documents(N)/number of documents term appeared (df)', 'Log10(N/df)'])
    writer.writerows(csv_table1)


keyword_index = -1
for keyword in search_keyword_list:
    article_counter = 0
    keyword_index = keyword_index + 1
    with open(keyword + '_table2.csv', 'w', newline='') as table2:
        writer = csv.writer(table2)
        writer.writerow(['Term', keyword])
        writer.writerow([keyword+' appeared in '+str(table1_counters[keyword_index])+' documents', 'News Article', 'Total Words (m)',
                         'Frequency (f)'])
        for news in news_list:
            article_counter = article_counter + 1
            obj = []
            news_str = str(news['body'])
            words = news_str.split()
            if keyword in words:
                obj.append('Article #'+str(article_counter))
                obj.append(news_str)
                obj.append(len(words))
                bow = dict(collections.Counter(words))
                for word, count in bow.items():
                    if word == keyword:
                        obj.append(str(count))
                writer.writerow(obj)


for keyword in search_keyword_list:
    highest_relative_frequency = 0
    max_frequency_article = ''
    max_frequency = 0

    for news in news_list:
        article = news['body']
        words = article.split()
        if keyword in words:
            bow = dict(collections.Counter(words))
            for word, count in bow.items():
                if word == keyword:
                    curr_highest_relative_frequency = count / len(words)
                    if curr_highest_relative_frequency > highest_relative_frequency:
                        highest_relative_frequency = curr_highest_relative_frequency
                        max_frequency_article = article
                        max_frequency = count

    print('Maximum relative frequency of '+keyword +
          ' is : ' + str(highest_relative_frequency))
