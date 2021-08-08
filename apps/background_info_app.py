# Data Imports
from components import ev_adoption_scatterplot, vehicle_composition_lineplot, exhaust_emission_barplot

# Streamlit Imports
import streamlit as st
from streamlit_folium import folium_static

def app():
    background_intro = '''
        <h1>Background Information</h1>
            <p>
                In this section, we'll go through the problem statement posed by Surbana Jurong (SJ) and visualise some of our thoughts and initial ideas.
            </p>

        <h2>SJ's Problem Statement</h2>
            <p>
                "Propose innovative solutions based upon data analytics insights from relevant open-sourced data sets for an Integrated 
                facility Command and Control centre (ICC) in Singapore."
            </p>
            <p>
                This was the problem statement posed by SJ. The problem statement was vague which allowed us to conceptualise various creative ideas. 
                However, upon expanding on those ideas, many were shot down due to the lack of free open-source datasets.
            </p>
            <p>
                Very soon, it became apparent that the <i><b>limiting factor</i></b> was not our creativity, but the <i><b>availibility of relevant data</i></b>. 
                Despite being less than ideal, due to the short time frame, we pivoted our ideation process from a problem first approach to a <i><b>data first 
                approach</i></b>. 
            </p>

        <h2>The Relevance of Traffic</h2>
            <p>
                After going through several iterations of our project scope, the Traffic Psychics decided to focus our efforts on a 
                <a href = "https://data.gov.sg/dataset/traffic-images" target = "_blank">real-time open source API for traffic images</a>. We explored the 
                the different use cases for this dataset and decided that <i><b>vehicle exhaust emissions</i></b> was one of the potentially more interesting use 
                cases that was still relevant to the theme of the hackaton. 
            </p>
            <p>
                Below, we visualise the relevance of ICE vehicles in Singapore despite the push for EVs.
            </p>
    '''
    st.markdown(background_intro, unsafe_allow_html = True)


    background_annual_vehicle_population_1 = '''
        <h3>Annual Motor Vehicle Population by Vehicle Type</h3>
            <p>
                Despite the recent push for Electric Vehicles (EV), many Internal Combustion Engine (ICE) vehicles continue to remain on the road. The graph below shows
                the breakdown of the motor vehicle population by vehicle types. 
            </p>
    '''
    st.markdown(background_annual_vehicle_population_1, unsafe_allow_html = True)
    vehicle_composition_chart = vehicle_composition_lineplot.create_lineplot()
    st.write(vehicle_composition_chart)

    background_annual_vehicle_population_2 = '''
        <p>
            Note that the graph does not show us exactly how many EVs are on the road, but rather the <i><b>total population of vehicles, including EVs</i></b>. This 
            gives us a good gauge to estimate the expected number of EVs to ICE vehicles on the roads later on.
        </p>
    '''
    st.markdown(background_annual_vehicle_population_2, unsafe_allow_html = True)

    background_ev_adoption_1 = '''
        <h3>Expected EV Adoption</h3>
        <p>
            Singapore has ambitious plans to <i><b>phase out ICE vehicles by 2040</b></i>. However, ICE vehicless will continue to remain relevant and continue to produce 
            exhaust emissions so long as they are around.
        </p>
        <p>
            We do not have many data points to work with with regards to the expected growth of EVs in Singapore. However, the government has a goal for 60,000 
            charging points by 2030 with a ratio of 1 charging point to 5 EVs. This means that in 2030 we are expecting 300,000 EVs. Assuming a constant amount of 
            ICE vehicles stay in the market and a 1 to 1 exchange between ICE vehicles and EVs. We can expect roughly 300,000 ICE vehicles to remain in 2030.
        </p>
        <p>
            In the chart below, we used a linear regression model in Ordinary Least Sqaures to guesstimate the year-on-year change in ICE vehicles, EVs and Charging Points 
            with the data points provided from <a href = "https://www.channelnewsasia.com/singapore/obstacles-remain-electric-vehicle-despite-incentives-transport-359331" target = "_blank">
            Singapore's 2030 Green Plan</a> and  <a href = "https://www.channelnewsasia.com/singapore/ev-electric-vehicle-registrations-rise-in-2021-2058496" target = "_blank">
            various other sources</a>.
        </p>
    '''
    st.markdown(background_ev_adoption_1, unsafe_allow_html = True)

    selected_stats = st.multiselect('View how ICE Vehicles compare to EVs in terms of quantities.', ['Electric Vehicles', 'Charging Points', 'ICE Vehicles'], ['Electric Vehicles', 'Charging Points', 'ICE Vehicles'])
    expected_EV_chart = ev_adoption_scatterplot.create_scatterplot(selected_stats)
    st.write(expected_EV_chart)

    background_ev_adoption_2 = '''
        <p>
            That being said, if our assumptions hold true, in 2030, <i><b>exhaust emissions will continue to remain a problem</b></i> despite the push for EVs as ICE Vehicles continue to exist in large numbers.
        </p>
    '''
    st.markdown(background_ev_adoption_2, unsafe_allow_html = True)

    background_exhaust_emission_1 = '''
        <h2>Exhaust Emission for Petrol Driven Motor Vehicles</h2>
            <p>
                Additionally, in order to get a general overview and better understand the types of exhaust emissions various vehicles produce, we aggregated the different exhaust emissions from the 
                <a href = "https://sso.agc.gov.sg/SL/EPMA1999-RG6?DocDate=20120629&ProvIds=Sc1-#Sc1-" target = "_blank">Euro VI Emission Standards</a> and broke them down into emissions 
                produced by different vehicle categories. This breakdown can be seen in the barchart below.
            </p>
    '''
    st.markdown(background_exhaust_emission_1, unsafe_allow_html = True)
    
    selected_emissions = st.multiselect('Choose which emission to view.', ['CO₂', 'NOx', 'CO', 'P'], ['CO₂', 'NOx', 'CO', 'P'])
    exhaust_emission_chart = exhaust_emission_barplot.create_barchart(selected_emissions)
    st.write(exhaust_emission_chart)

    background_exhaust_emission_2 = '''
        <p>
            Note that the barchart is <i><b>log-scaled<b></i>. This means that at higher levels of emissions in that of CO₂, the difference between vehicle categories is larger than it seems on the chart.
        </p>
    '''
    st.markdown(background_exhaust_emission_2, unsafe_allow_html = True)
