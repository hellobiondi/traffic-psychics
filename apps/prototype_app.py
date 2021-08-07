# Processing Imports
import requests

# Data Manipulation Imports
import pandas as pd
import numpy as np

# CV Imports
import cv2
import cvlib as cv

# Data Imports
from components import traffic_maps

# Streamlit Imports
import streamlit as st
from streamlit_folium import folium_static

def app():
    # Traffic Camera Data
    API_URL = 'https://api.data.gov.sg/v1/transport/traffic-images'

    camera_data = traffic_maps.get_camera_data(API_URL)
    metadata = traffic_maps.get_metadata(camera_data[0])
    camera_data_df = traffic_maps.get_camera_data_df(camera_data, metadata)

    # Exhaust Emission Data
    try:
        exhaust_emission_df = pd.read_csv("./assets/exhaust_emissions.csv")
    except:
        exhaust_emission_df = pd.read_csv("../assets/exhaust_emissions.csv")

    st.title("The Prototype")
    # Explanation
    st.header('Geospatial Breakdown of Traffic Conditions')
    st.subheader('Prototype Explanation')
    st.write("Our prototype aims to allow the ICC to make informed traffic decisions based on the current exhaust emissions on the road.")
    st.write("It utilises OpenCV's Computer Vision model to calculate the number of vehicles at each camera location based on categories and aggregates the vehicle's exhaust emissions data to provide the expected emissions at each camera location.")
    st.write("Note: the model may take some time to process the images from all 87 cameras.")

    cv_progress_bar = st.progress(0)
    camera_progress_rate = 1/len(camera_data_df.index)
    
    # Heatmap
    @st.cache(ttl = 300)
    def run_CV(camera_data_df, exhaust_emission_df):
        ## Image Processing function from traffic_maps component
        # traffic_maps.get_vehicle_data(camera_data_df, exhaust_emission_df)
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
            test = label.count('bus')

            camera_data_df.loc[index, 'vehicle_qty'] = all_vehicles.sum()
            camera_data_df.loc[index, 'total_CO₂'] = np.around(np.multiply(CO2_emission_rate, all_vehicles).sum(), 2)
            camera_data_df.loc[index, 'total_NOx'] = np.around(np.multiply(NOx_emission_rate, all_vehicles).sum(), 2)
            camera_data_df.loc[index, 'total_CO'] = np.around(np.multiply(CO_emission_rate, all_vehicles).sum(), 2)
            camera_data_df.loc[index, 'total_P'] = np.around(np.multiply(P_emission_rate, all_vehicles).sum(), 2)
   
            cv_progress_bar.progress(index * camera_progress_rate)

        return camera_data_df

    run_CV(camera_data_df, exhaust_emission_df)

    st.subheader('Traffic Geospatial Heatmap')
    st.write("The geospatial heatmap aims to give the ICC an overview of the number of vehicles on the road through a heat gradient. The 'hotter' an area is, the more vehicles there are at that location.")

    vehicle_qty_coord = traffic_maps.get_vehicle_qty_coord(camera_data_df)
    heatmap = traffic_maps.create_heatmap(vehicle_qty_coord)

    folium_static(heatmap) # Displays heatmap on Streamlit


    # Camera Locations Map
    st.subheader('Exhaust Emission Markers')
    st.write("After identifying a location of interest through the heatmap, the user can then zoom in on the said location in the map below and identify the exact amount of vehicles picked up at this location and the total derived exhaust emissions.")

    cameraId_map = traffic_maps.create_cameraId_map(camera_data_df)
    folium_static(cameraId_map) 

