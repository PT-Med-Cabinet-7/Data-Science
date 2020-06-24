"""to retrieve data from the database"""
import sqlite3
import numpy as np

def kush_info(id_list, distance_list):
    """takes in the list of two arrays returned from the model
    and returns all the information about the strains
    in a json format"""

    #connecting to the database
    conn = sqlite3.connect('med_cabinet3.sqlite3')
    curs = conn.cursor()

    needed_columns = ['Strain', 'Type', 'Rating', 'Effects', 'Flavor', 'Description']

    # scale distance to a score from 1 to 3
    distances = []
    for i in range(0, 5):
        distances.append(distance_list[i])
    distances = np.asarray(distances)

    scaler = MinMaxScaler(feature_range=(1, 3))
    
    scaled = scaler.fit_transform(distances.reshape(-1, 1))
    scaled = scaled.round()
    scores = scaled.reshape(1,-1)
    for i in range(0, 5):
        kush_list = {}
        kush_list['Recommendation'] = i + 1
        for item in needed_columns:
            request = f'SELECT {item} FROM strain_info WHERE id = {int(id_list[i])};'
            value = str(curs.execute(request).fetchall())
            #For some reason the SQL query returns something 
            # formatted like (['<strain-name>,]) so this is 
            # to remove all the useless characters
            value = value.replace(')', '')
            value = value.replace('[', '')
            value = value.replace(']', '')
            value = value.replace('(', '')
            value = value.replace(',', '')
            value = value.replace("'", '')
            value = value.replace('\ ', '')
            value = value.replace('"', '')
            kush_list[item] = value
        kush_list['Score'] = scores[0][i]
        return_list.append(kush_list)
    curs.close()
    return return_list