# Traffic API Imports
import requests
from datetime import datetime
import json

# Data Manipulation Imports
import pandas as pd
import numpy as np

# CV Imports
import cv2
import cvlib as cv

# Visualisation Imports
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster


def get_camera_data(API_URL):
    '''
        Returns a list of camera data from traffic-image api URL.
        Note: function will return result based on current date-time.
        Params:
            API_URL: traffic data API url.
    '''

    query = {'date_time' : datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}
    response = requests.get(url = API_URL, params = query)
    response = response.json()

    return response['items'][0]['cameras']


def get_metadata(camera_col):
    '''
        Retrieve metadata from single col of camera data result.
        Params:
            camera_col: single col result from get_camera_data function.
    '''
    
    metadata = []
    for item in camera_col:
        if isinstance(camera_col[item], dict):
            for i in camera_col[item]:
                metadata.append(i)
                
        else:
            metadata.append(item)

    return metadata



def get_camera_data_df(camera_list, metadata): 
    '''
        Returns camera data as a df with camera data from API and metadata.
        Params:
            camera_list: result from get_camera_data() function.
            metadata: result from.
    '''
    
    data = {}
    count = 1

    for dictionary in camera_list:
        reference_list = []

        for reference in dictionary:
            if isinstance(dictionary[reference], dict):
                item = dictionary[reference]

                for i in item:
                    reference_list.append(item[i])

            else:
                reference_list.append(dictionary[reference])

        data[count] = reference_list
        count += 1

    camera_data_df = pd.DataFrame.from_dict(data, orient='index', columns=metadata)
    
    return camera_data_df


def get_vehicle_data(camera_data_df, exhaust_emission_df):
    '''
        Returns orginal df with number of vehicles at each camera.
        Iterates through camera_data_df, appending num_vehicles based on vehicles on the road calculated through image link in df row.
        Params:
            camera_data_df: pd dataframe as input from get_camera_data_df() function.
            exhaust_emission_df: exhaust emission data.
    '''
    CO2_emission_rate = exhaust_emission_df['CO₂'].values
    NOx_emission_rate = exhaust_emission_df['NOx'].values
    CO_emission_rate = exhaust_emission_df['CO'].values
    P_emission_rate = exhaust_emission_df['P'].values


    for index, row in camera_data_df.iterrows():
        image = requests.get(row['image'])
        file = open("sample_image.png", "wb")
        file.write(image.content)

        im = cv2.imread('sample_image.png')
        bbox, label, conf = cv.detect_common_objects(im)

        all_vehicles = np.array([label.count('bus'), label.count('car'), label.count('truck'), label.count('motorcycle')])

        camera_data_df.loc[index, 'vehicle_qty'] = all_vehicles.sum()
        camera_data_df.loc[index, 'total_CO₂'] = np.around(np.multiply(CO2_emission_rate, all_vehicles).sum(), 2)
        camera_data_df.loc[index, 'total_NOx'] = np.around(np.multiply(NOx_emission_rate, all_vehicles).sum(), 2)
        camera_data_df.loc[index, 'total_CO'] = np.around(np.multiply(CO_emission_rate, all_vehicles).sum(), 2)
        camera_data_df.loc[index, 'total_P'] = np.around(np.multiply(P_emission_rate, all_vehicles).sum(), 2)

    return camera_data_df


def get_vehicle_qty_coord(camera_data_df):
    '''
        Returns camera locations and number of vehicles at each location as a list.
        Params:
            camera_data_df: pd dataframe as input from get_camera_data_df() function.
    '''

    vehicle_qty_coord_df = camera_data_df[['latitude', 'longitude', 'vehicle_qty']]
    vehicle_qty_coord = vehicle_qty_coord_df.values.tolist()
    
    return vehicle_qty_coord




def create_heatmap(vehicle_qty_coord):
    '''
        Returns heatmap object for number of vehicles picked up at each location.
        Params:
            vehicle_qty_coord: nested list of lat longs of camera locations with vehicle quantities from traffic_data.py get_vehicle_qty_coord() function. e.g. [[lat, long, vehicle_qty], ...]
    '''
    
    camera_heatmap = folium.Map(location = [1.357, 103.826], zoom_start = 11.4)

    heatmap_gradient = {
        0: 'Black',
        0.6 : 'Navy',
        0.7 : 'Blue',
        0.8 : 'Yellow',
        0.9 : 'Red',
        1.0 : 'Maroon'
    }

    HeatMap(vehicle_qty_coord, radius = 20, gradient = heatmap_gradient).add_to(camera_heatmap)

    return camera_heatmap

def create_cameraId_map(camera_data_df):
    '''
        Returns map object with cameraIDs at each location.
        Params:
            camera_data_df: pd dataframe as input from get_camera_data_df() function.
    '''

    cameraId_map = folium.Map(location = [1.357, 103.826], zoom_start = 11.4)
    marker_cluster = MarkerCluster().add_to(cameraId_map)

    for index, row in camera_data_df.iterrows():        
        folium.Marker(
            location = [row['latitude'],row['longitude']],
            popup = f"<b>Camera</b>: {row['camera_id']}<br><b>Total Vehicles</b>: {row['vehicle_qty']}<br><b>Total CO₂</b>: {row['total_CO₂']}<br><b>Total NOx</b>: {row['total_NOx']}<br><b>Total CO</b>: {row['total_CO']}<br><b>Total P</b>: {row['total_P']}",
            tooltip = f"Camera {row['camera_id']} Data"
        ).add_to(marker_cluster)

    return cameraId_map












if __name__ == '__main__':
    api_url = 'https://api.data.gov.sg/v1/transport/traffic-images'
    camera_data = get_camera_data(api_url)
    metadata = get_metadata(camera_data[0])
    camera_data_df = get_camera_data_df(camera_data, metadata)

    # help(create_cameraId_map)