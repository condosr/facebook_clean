import csv
from fileinput import filename
import json
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
    for i in range(len(data_matrix)):
        if i > 0:
            current_item = data_matrix[i][column]
            if not current_item.strip() == '':
                try:
                    yo = json.loads(current_item.strip(']['))
                    the_dict = dict(yo)
                    dict_list.append(the_dict)
                except:
                    'uh oh'
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
        #b = []
        #master = []
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
        #print(mat)
        #master.append(a)
        #master.append(b)
        #print(master)
        
        #my_mat = np.array(a, dtype = object)
        
        print(mat)
        #print(my_mat)
        #print(type(my_mat))
        #print(height)
        #my_mat.shape
        #print(my_mat)
        #print(a)
        filename = f"C:\\Users\\Scott\\Documents\\GitHub\\facebook_clean\\csv_write\\{_}.csv"
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            
            # writing the fields
            #csvwriter.writerow(fields)
            
            # writing the data rows
            csvwriter.writerows(mat)
    
    
    

                

needed_data = column_get_matrix_return('C:\\Users\\Scott\\Documents\\GitHub\\facebook_clean\\resources\\ORDER_URL_TAG (SHOPIFY_F000193_1.ORDER_URL_TAG) (SHOPIFY_F000193_1)_AD_SET_HISTORY.csv')
category_dict = json_column_distinct_value_grab(needed_data)
category_csv_make(category_dict)