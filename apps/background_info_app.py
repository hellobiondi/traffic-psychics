# Data Imports
from components import ev_adoption_scatterplot, vehicle_composition_lineplot, exhaust_emission_barplot

# Streamlit Imports
import streamlit as st
from streamlit_folium import folium_static

def app():
    st.title("Background Information")
    
    background_intro = '''
        <p>
            In this section, we'll go through the problem statement posed by Surbana Jurong (SJ) and some of our thoughts and initial ideas.
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
                Very soon, it became apparent that the limiting factor was not our creativity, but the availibility of "relevant" data.
            </p>

        <h2>The Relevance of Traffic</h2>
            <p>
                After going through several iterations of our project scope, the Traffic Psychics decided to focus our efforts on a 
                <a href = "https://data.gov.sg/dataset/traffic-images" target = "_blank">real-time open data source for traffic images</a>. 
                Below, we visualise the relevance of ICE vehicles in Singapore despite the push for EVs.
            </p>
    '''

    st.markdown(background_intro, unsafe_allow_html = True)


    annual_vehicle_population_paragraph = '''
        <h3>Annual Motor Vehicle Population by Vehicle Type</h3>
        <p>
            With the recency of the EV push, many Internal Combustion Engine (ICE) vehicles continue to remain on the road. The graph below shows
            the breakdown of the motor vehicle population by vehicle types.
        </p>
    '''

    st.markdown(
        annual_vehicle_population_paragraph, unsafe_allow_html = True
    )


    vehicle_composition_chart = vehicle_composition_lineplot.create_lineplot()
    st.write(vehicle_composition_chart)

    ev_adoption_paragraph = '''
        <h3>Expected EV Adoption</h3>
        <p>
            Singapore has ambitious plans to <b>phase out</b> ICE vehicles by 2040. However, ICE vehicless will continue to remain relevant and continue to produce 
            exhaust emissions so long as they are around.
        </p>
        <p>
            We do not have many data points to work with with regards to EVs expected growth in Singapore. However, the government has a goal for 60,000 
            charging points by 2030 with a ratio of 1 charging point to 5 EVs. This means that in 2030 we can expect 300,000 EVs. Assuming a constant amount of 
            ICE vehicles stay in the market and a 1 to 1 exchange between ICE vehicles and EVs. We can expect roughly 300,000 ICE vehicles to remain in 2030.
        </p>
    '''

    st.markdown(
        ev_adoption_paragraph, unsafe_allow_html = True
    )

    st.write("")
    selected_stats = st.multiselect('View how ICE Vehicles compare to EVs in terms of quantities.', ['Electric Vehicles', 'Charging Points', 'ICE Vehicles'], ['Electric Vehicles', 'Charging Points', 'ICE Vehicles'])
    expected_EV_chart = ev_adoption_scatterplot.create_scatterplot(selected_stats)
    st.write(expected_EV_chart)
    st.write("That being said, if our assumptions hold true, in 2030, exhaust emissions will continue to remain a problem despite the push for EVs as ICE Vehicles continue to exist in large numbers.")


    exhaust_emission_paragraph = '''
        <h2>Exhaust Emission for Petrol Driven Motor Vehicles</h2>
        <p>
            In order to better understand the types of exhaust emissions various vehicles produce, we aggregated the different exhaust emissions and broke them down into emissions 
            produced by different vehicle categories. This breakdown can be seen in the barchart below.
        </p>
    '''
    st.markdown(
        exhaust_emission_paragraph, unsafe_allow_html = True
    )
    selected_emissions = st.multiselect('Choose which emission to view.', ['CO₂', 'NOx', 'CO', 'P'], ['CO₂', 'NOx', 'CO', 'P'])


    exhaust_emission_chart = exhaust_emission_barplot.create_barchart(selected_emissions)
    st.write(exhaust_emission_chart)
