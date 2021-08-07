import pandas as pd
import streamlit as st

def app():
    # Example Dataframes
    try:
        exhaust_emission_df = pd.read_csv("./assets/exhaust_emissions.csv")
        annual_motor_vehicle_preproc_example_df = pd.read_csv("./assets/annual-motor-vehicle-population-by-vehicle-type.csv")
        annual_motor_vehicle_postproc_example_df = pd.read_csv("./assets/annual_motor_vehicle_example.csv")
        camera_data_df_example = pd.read_csv("./assets/camera_data_df_example.csv")
        cv_ideal = "./assets/cv_ideal.png"
        cv_actual = "./assets/cv_actual.png"
        camera_data_df_cv_example = pd.read_csv("./assets/camera_data_df_cv_example.csv")
         
    except:
        exhaust_emission_df = pd.read_csv("../assets/exhaust_emissions.csv")
        annual_motor_vehicle_preproc_example_df = pd.read_csv("../assets/annual-motor-vehicle-population-by-vehicle-type.csv")
        annual_motor_vehicle_postproc_example_df = pd.read_csv("../assets/annual_motor_vehicle_example.csv")
        camera_data_df_example = pd.read_csv("../assets/camera_data_df_example.csv")
        cv_ideal = "../assets/cv_ideal.png"
        cv_actual = "../assets/cv_actual.png"
        camera_data_df_cv_example = pd.read_csv("../assets/camera_data_df_cv_example.csv")


    st.title("Methodology")    
    methodology_intro = '''
        <p>
            The open-sourced data that we utilised was not formatted consistently and a lot of it had to be engineered to fit our requirements.
        </p>
        <p>
            In this section, we demonstrate our project's entire data pipeline, from how we sourced and engineered our data, to how we fed it into 
            the OpenCV Computer Vision model, to finally producing the results on a heatmap.
        </p>
    '''
    st.markdown(methodology_intro, unsafe_allow_html = True)

    methodology_exhaust_emission_1 = '''
        <h2>Exhaust Emission Data</h2>
        <p>
            We first find out the maximum possible emissions of CO, NOx and particulate matter by vehicle category 
            (motorcycles, cars, commercial goods vehicle, buses). This is possible by perusing the 
            <a href = "https://sso.agc.gov.sg/SL/EPMA1999-RG6?DocDate=20120629&ProvIds=Sc1-#Sc1-" target = "_blank">Euro VI Emission Standards</a>, 
            which is a regulation framework that cars in Singapore adhere to.
        </p>
    '''
    st.markdown(methodology_exhaust_emission_1, unsafe_allow_html = True)
    st.write(exhaust_emission_df)

    methodology_exhaust_emission_2 = '''
        <p>
            For CO₂ emissions, we estimated a weighted average based on both the published dataset of fuel economy data of the vehicles, 
            and Singapore Total Car Population by Make using <a href = "https://data.gov.sg/dataset/annual-motor-vehicle-population-by-vehicle-type" target = "_blank">
            LTA’s Annual Vehicle Statistics 2020</a>.
        </p>
        <p>
            The data retrieved also had to be flattened in order to align it to the categories identified in the exhaust emission data. Little details 
            from inconsistent capitalisation to larger ones such as category aggregation was conducted with Pandas.
        </p>
    '''
    st.markdown(methodology_exhaust_emission_2, unsafe_allow_html = True)

    vehicle_breakdown_data = st.selectbox('Annual Vehicle Statistic Stage:', ['Pre-processed Annual Vehicle Statistic', 'Post-processed Annual Vehicle Statistic'])
    if vehicle_breakdown_data == 'Pre-processed Annual Vehicle Statistic':
        st.write(annual_motor_vehicle_preproc_example_df)
    else:
        st.write(annual_motor_vehicle_postproc_example_df)


    methodology_camera_data_1 = '''
        <h2>Live Traffic Images</h2>
        <h3>Traffic Data</h3>
        <p>
            Next, we retrieved the JSON file from <a href = 'https://data.gov.sg/dataset/traffic-images'>LTA’s Live Traffic API</a>. As expected, the JSON file 
            was nested and we had to format it in order to convert it nicely into a Pandas dataframe. The dataframe allowed us to visualise the structure of the 
            data intuitively and allowed the images’ URL from LTA’s 87 cameras to be retrieved with relative ease. The images of roads are captured real-time 
            every 20 seconds.
        </p>


    '''
    st.markdown(methodology_camera_data_1, unsafe_allow_html = True)
    st.write(camera_data_df_example)

    methodology_camera_data_2 = '''
        <h3>OpenCV</h3>
        <p>
            We then used OpenCV’s open-source Computer Vision model to identify vehicles by the vehicle categories mentioned earlier. OpenCV's model yielded lacklustre results,
            however, as we did not have the time to experiment with different models while completing the prototype within the 3 days duration, we made do with OpenCV's model 
            as a proof of concept.
        </p>
    '''
    st.markdown(methodology_camera_data_2, unsafe_allow_html = True)

    image_select = st.selectbox('OpenCV Vehicle Identification Demonstration:', ['Actual Result w/ Low-Res Traffic Image', 'Ideal Result w/ High-Res Traffic Image'])
    if image_select == 'Actual Result w/ Low-Res Traffic Image':
        st.image(cv_actual)
    else:
        st.image(cv_ideal)

    methodology_camera_data_3 = '''
        <p>
            It should be noted that from the image comparison, with a higher quality image where vehicles are closer to the camera, OpenCV has the potential to yield decent result, 
            being able to identify even potted plants.
        </p>
    '''
    st.markdown(methodology_camera_data_3, unsafe_allow_html = True)


    methodology_data_agg = '''
        <h2>Data Aggregation</h2>
        <p>
            With the labels generated from OpenCV's model, we calculated the exhaust emissions produced based on the different types of vehicles identified and aggregated the data
            into the same dataframe. This allows us to identify the potential amount of exhaust emission at each camera location.
        </p>
    '''
    st.markdown(methodology_data_agg, unsafe_allow_html = True)
    st.write(camera_data_df_cv_example)



    methodology_data_vis = '''
        <h2>Data Visualisation</h2>
        <p>
            We decided to visualise our data onto a map, essentially, creating our prototype. Our prototype is the culmination of our entire methodology from start till end. The 
            prototype identifies the quantity of vehicles at each of the 87 camera locations provided in LTA's open dataset through Open CV's computer vision model. The respective 
            exhaust emission for each type of vehicle is then summed to determine the potential exhaust emissions on the road. 
        </p>
        <p>
            This is all visualised onto two different maps. Together, they aim to allow the ICC to make informed decisions which can be backed by data.
        </p>
    '''
    st.markdown(methodology_data_vis, unsafe_allow_html = True)

    