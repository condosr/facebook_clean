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
    #print(return_list[1])
    return return_list
    
    
def json_column_distinct_value_grab(return_list):
    data_matrix = return_list[0]
    column = return_list[1]
    the_count = 0
    dict_list = []
    
    for i in range(len(data_matrix)):
        if i > 0:
            current_item = data_matrix[i][column]
            if not current_item.strip() == '':
                current_item = current_item.replace('\n', '')
                current_item = current_item.replace(' ', '')
                current_item = current_item.strip()
                yo = json.loads(current_item)
                dict_list.append(yo)
    category_dict = {}
    for sub_list in dict_list:
        for _ in sub_list:
            for category_key in _:
                if not has_key(category_dict, category_key):
                    category_dict[category_key] = []
                else:
                    pass
                sub_dict_list = _[category_key]
                for sub_dict in sub_dict_list:
                    if type(sub_dict) == 'dict':
                        if not sub_dict['name'] in category_dict[category_key]:
                            category_dict[category_key].append(sub_dict['name']) 
                    else:
                        try: 
                            if not sub_dict in category_dict[category_key]:
                                temp_dict = json.loads(sub_dict)
                                category_dict[category_key].append(temp_dict['name'])
                        except:
                            if not sub_dict in category_dict[category_key]:
                                category_dict[category_key].append(sub_dict)
    return category_dict

def category_csv_make(category_dict):
    topic_dict = {}
    for topic in category_dict:
        categories = category_dict[topic]
        topic_dict[topic] = []
        for category in categories:
            try:
                topic_dict[topic].append(category['name'])
            except:
                topic_dict[topic].append(category)
    print(topic_dict)
    
    for _ in topic_dict:
        a = []
        a.append(_)
        the_list = topic_dict[_]
        height = len(the_list)+1
        mat = np.zeros((height,1), dtype=object)
        mat[0][0] = _
    
        for item in range(len(the_list)):
            mat[item+1][0] = the_list[item]
        
        filename = f"C:\\Users\\Scott\\Documents\\GitHub\\facebook_clean\\csv_write\\{_}.csv"
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(mat)
        csvfile.close()
    return topic_dict

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
        for cell in range(len(original_matrix[0]) - 1):
            if cell >= not_needed_column:
                corrected_column = cell + 1
                new_mat[row][cell] = original_matrix[row][corrected_column]
            else:
                new_mat[row][cell] = original_matrix[row][cell]
    
    filename = f"C:\\Users\\Scott\\Documents\\GitHub\\facebook_clean\\csv_write\\updated_csv.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(new_mat)


def dict_row_pair(return_list):
    data_matrix = return_list[0]
    column = return_list[1]
    dict_list = []
    for i in range(len(data_matrix)):
        pair = []
        if i > 0:
            current_item = data_matrix[i][column]
            if not current_item.strip() == '':
                current_item = current_item.replace('\n', '')
                current_item = current_item.replace(' ', '')
                current_item = current_item.strip()
                yo = json.loads(current_item)
                pair.append(i)
                pair.append(yo)
                dict_list.append(pair)
    print('__________________________________________________')
    #print(dict_list)
    the_key = 0
    new_list = []
    for _ in dict_list:
        yo = {}
        the_key = _[0]
        value = _[1]
        yo[the_key] = value
        new_list.append(yo)
    print(new_list)
    return new_list

    

def dict_row_clean(dict_list):
    total_dict = {}
    key_dict = {}
    for dict in dict_list:
        for row_num in dict:
            print('++++++++++++++++++++++++')
            key_dict[row_num] = {}
            topics = dict[row_num]
            for topic_dicts in topics:
                print('===============')
                print(topic_dicts)
                for topic in topic_dicts:
                    categories = topic_dicts[topic]
                    category_string = ''
                    category_count = 0
                    amount_of_categories = len(categories)
                    for category_dict in categories:
                        category_count += 1
                        #print(category_dict)
                        if type(category_dict) == int:
                            stringed = str(category_dict)
                            if category_count < amount_of_categories and category_count > 1 and amount_of_categories >= 1:
                                category_string += ' ' + stringed + ' and'
                            elif category_count == 1 and amount_of_categories > 1:
                                category_string += stringed + ' and'
                            elif category_count >= amount_of_categories and amount_of_categories >=1:
                                category_string += ' ' + stringed
                            elif amount_of_categories == 1:
                                category_string += stringed
                        else:
                            name = category_dict['name']
                            if type(name) == list:
                                name = "".join(name)
                            elif type(name) == int:
                                name = str(int)
                            if category_count < amount_of_categories and category_count > 1 and amount_of_categories >= 1:
                                category_string += ' ' + name + ' and'
                            elif category_count == 1 and amount_of_categories > 1:
                                category_string += name + ' and'
                            elif category_count >= amount_of_categories and amount_of_categories >=1:
                                category_string += ' ' + name
                            elif amount_of_categories == 1:
                                category_string += name
                        #row_num_dict = key_dict[row_num] 
                        key_dict[row_num][topic] = category_string
    print('@@@@@@@@@@@@@@@@@@@@@@')
    print(key_dict)
    return key_dict

    '''
    total_dict = {}
    key_dict = {}
    for dict in dict_list:
        #print('===========================================')
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
    '''
def json_fix(string_json):
    open_paren_count = 0
    #close_paren_count = 0
    for _ in string_json:
        #print(_)
        if _ == '{':
            open_paren_count += 1
        elif _ == '}':
            open_paren_count -= 1
        print(open_paren_count)
    print(open_paren_count)
        
            
            

    
    

                
#json_fix('{"family_statuses":[{"id":"6023005458383","name":"Parentswithtoddlers(01-02years)"},{"id":"6023005529383","name":"Parentswithpreschoolers(03-05years)"},{"id":"6023005570783","name":"Parentswithearlyschool-agechildren(06-08years)"},{"id":"6023080302983","name":"Parentswithpreteens(09-12years)"}]},{"education_statuses":[11,3,9]}')
needed_data = column_get_matrix_return('C:\\Users\\Scott\\Documents\\GitHub\\facebook_clean\\resources\\ORDER_URL_TAG (SHOPIFY_F000193_1.ORDER_URL_TAG) (SHOPIFY_F000193_1)_AD_SET_HISTORY.csv')
category_dict = json_column_distinct_value_grab(needed_data)
category_csv_make(category_dict)
updated_table_write(needed_data, category_dict)
dict_list = dict_row_pair(needed_data)
dict_row_clean(dict_list)