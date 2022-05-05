import csv
from fileinput import filename
import json
#from xxlimited import new
import numpy as np

def has_key(dict, key):
        for _ in dict:
            if _ == key:
                return True
        return False

def column_get_matrix_return(filename):
    # initializing the titles and rows list
    return_list = []
    rows = []
    
    # reading csv file
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)   
        for row in csvreader:
            rows.append(row)
    csvfile.close()
    count = 0
    for row in rows[0]:
        if row == 'Targeting Flexible Spec':
            break
        else:
            count +=1
    return_list.append(rows)
    return_list.append(count)
    print(return_list[1])
    return return_list
    
    
def json_column_distinct_value_grab(return_list):
    data_matrix = return_list[0]
    column = return_list[1]
    the_count = 0
    dict_list = []
    with open('C:\\Users\\Scott\\Documents\\GitHub\\facebook_clean\\resources\\example.txt', 'w') as pls:
        for i in range(len(data_matrix)):
            if i > 0:
                current_item = data_matrix[i][column]
                pls.write(str(i))
                pls.write(current_item)
                pls.write('\n')
                #pls.close()
                if not current_item.strip() == '':
                    try:
                        yo = json.loads(current_item.strip(']['))
                        the_dict = dict(yo)
                        dict_list.append(the_dict)
                    except:
                        'uh oh'
        pls.close()
    category_dict = {}
    for _ in dict_list:
        for category_key in _:
            if not has_key(category_dict, category_key):
                category_dict[category_key] = []
            else:
                pass
            sub_dict_list = _[category_key]
            for sub_dict in sub_dict_list:
                if not sub_dict['name'] in category_dict[category_key]:
                    category_dict[category_key].append(sub_dict['name'])
    print(category_dict)
    return category_dict

def category_csv_make(category_dict):
    
    for _ in category_dict:
        a = []
        a.append(_)
        print('============================')
        print(_)
        the_list = category_dict[_]
        height = len(the_list)+1
        mat = np.zeros((height,1), dtype=object)
        mat[0][0] = _
        #print(mat)
        for item in range(len(the_list)):
            print(len(the_list))
            print(the_list[item])
            mat[item+1][0] = the_list[item]
        print(mat)
        
        filename = f"C:\\Users\\Scott\\Documents\\GitHub\\facebook_clean\\csv_write\\{_}.csv"
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(mat)

def updated_table_write(return_list, category_dict):
    expand_rows = len(category_dict) - 1
    original_matrix = return_list[0]
    not_needed_column = return_list[1]
    height = len(original_matrix)
    width = len(original_matrix[0]) + expand_rows
    new_mat = np.zeros((height,width), dtype=object)
    #print(new_mat)
    corrected_column = 0
    for row in range(len(original_matrix)):
        #if row >= not_needed_row:
            #corrected_row = row + 1
        for cell in range(len(original_matrix[0]) - 1):
            if cell >= not_needed_column:
                corrected_column = cell + 1
                new_mat[row][cell] = original_matrix[row][corrected_column]
            else:
                new_mat[row][cell] = original_matrix[row][cell]
    print(new_mat)
    filename = f"C:\\Users\\Scott\\Documents\\GitHub\\facebook_clean\\csv_write\\updated_csv.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(new_mat)

    #need the row index plus attributes ex. {row : dict of }
    print(new_mat[0][-4])


def dict_row_pair(return_list):
    data_matrix = return_list[0]
    column = return_list[1]
    dict_list = []
    for i in range(len(data_matrix)):
        if i > 0:
            current_item = data_matrix[i][column]
            if not current_item.strip() == '':
                try:
                    temp_dict = {}
                    yo = json.loads(current_item.strip(']['))
                    the_dict = dict(yo)
                    temp_dict[i] = the_dict
                    dict_list.append(temp_dict)
                except:
                    'uh oh'
    print(dict_list)
    return dict_list

def dict_row_clean(dict_list):
    total_dict = {}
    key_dict = {}
    for dict in dict_list:
        print('===========================================')
        for key in dict:
            topics = dict[key]
            #print(topics)
            #print('+++++++++++++++++++++++++++++++++++++++++++++')
            topic_dict = {}
            for topic in topics:
                categories = topics[topic]
                #print(categories)
                counter = 0
                my_string = ''
                for category in categories:
                    counter += 1
                    if counter >= len(categories):
                        my_string +=' ' + category['name']
                    else:
                        my_string +=' ' + category['name'] + ' and'
                my_string.strip()
                topic_dict[topic] = my_string
            key_dict[key] = topic_dict
    #print(key_dict)
        
        #for topic in dict:
            #answer_string = ''
            #for category in topic:
                #pass
            #alter_dict[topic] = answer_string
            
            

    
    

                

needed_data = column_get_matrix_return('C:\\Users\\Scott\\Documents\\GitHub\\facebook_clean\\resources\\ORDER_URL_TAG (SHOPIFY_F000193_1.ORDER_URL_TAG) (SHOPIFY_F000193_1)_AD_SET_HISTORY.csv')
category_dict = json_column_distinct_value_grab(needed_data)
category_csv_make(category_dict)
updated_table_write(needed_data, category_dict)
dict_list = dict_row_pair(needed_data)
dict_row_clean(dict_list)