import csv
from fileinput import filename
import json
import numpy as np

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
            if not category_dict in category_key:
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
        
        the_list = category_dict[_]
        for item in the_list:
            a.append(item)
        my_mat = np.array(a)
        print(my_mat)
        print(a)
        filename = f"/Users/scottcondo/Documents/GitHub/facebook_clean/csv_files/{_}.csv"
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            
            # writing the fields
            #csvwriter.writerow(fields)
            
            # writing the data rows
            csvwriter.writerows(my_mat)
    

                

needed_data = column_get_matrix_return('/Users/scottcondo/Documents/GitHub/facebook_clean/resources/ORDER_URL_TAG (SHOPIFY_F000193_1.ORDER_URL_TAG) (SHOPIFY_F000193_1)_AD_SET_HISTORY.csv')
category_dict = json_column_distinct_value_grab(needed_data)
category_csv_make(category_dict)