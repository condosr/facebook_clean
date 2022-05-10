from doctest import master
import pandas as pd
import json


df = pd.read_csv('C:\\Users\\Scott\\Documents\\GitHub\\facebook_clean\\resources\\ORDER_URL_TAG (SHOPIFY_F000193_1.ORDER_URL_TAG) (SHOPIFY_F000193_1)_AD_SET_HISTORY.csv')

def topic_get():
    topic_list = []
    for row in df['Targeting Flexible Spec']:
        if not type(row) == float:
            # Want to add each row data into the Interests column
            dict_list = json.loads(row)
            for topic_dict in dict_list:
                for topic in topic_dict:
                    if topic not in topic_list:
                        topic_list.append(topic)
    return topic_list

def row_dict_make():
    count = 0
    key_dict = {}
    for row in df['Targeting Flexible Spec']:
        if not type(row) == float:
            key_dict[count] = {}
            dict_list = json.loads(row)
            for topic_dict in dict_list:
                for topic in topic_dict:
                    #print(topic_dict[topic])
                    topic_string = ""
                    category_list = topic_dict[topic]
                    for category in category_list:
                        #print(category)
                        if not type(category) == int:
                            topic_string = topic_string + category['name'] + ','
                        else:
                            topic_string = topic_string + str(category) + ','
                    topic_string = list(topic_string)
                    topic_string[-1] = ''
                    topic_string = "".join(topic_string)
                    key_dict[count][topic] = topic_string
            count += 1
        else:
            count += 1
    return key_dict

def remake(key_dict, topic_list):
    for topic in topic_list:
        df[topic] = ''
    for key in key_dict:
        for topic in key_dict[key]:
            print(df.at[topic, key])

topic_list = topic_get()
key_dict = row_dict_make()
remake(key_dict, topic_list)