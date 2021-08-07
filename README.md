# Traffic Psychics

A data analytics and visualisation project submission to Surbana Jurong and Singapore Management University's "Code for Cities: Environmental Sustainability and Resiliency" Hackaton.

This project serves as a proof of concept that aims to determine the amount of **_exhaust emissions_** produced at **_traffic junctions_** in Singapore through **_open-sourced traffic APIs_** and **_Computer Vision Models_**. 

We created an interactive web application that details our entire process from ideation and conceptualisation to a visualised interactive prototype. Do check it out by clicking the badge below!

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/lohkokwee/traffic_psychics/app.py)

![](./assets/prototype_demo.gif)

# Table of Contents
- [About](#about)
- [Usage](#usage)
- [Datasets](#datasets)
- [Development](#development)
- [The Psychics](#the-psychics)

# About
Over the past decade, Singapore has seen a marked increase in the number of vehicles on its roads. _The vast majority of these vehicles still run on Internal Combustion Engines (ICE)_ which emit harmful gases, compromising both the environment and human health. With this in mind, our team _visualised the potential exhaust emissions_ of the many ICE vehicles still on Singapore’s roads by utilizing _open source traffic data_ combined with _computer vision modeling_.

[Back to top](#table-of-contents)

# Usage
Our web app was created with the intention of allowing users at Surbana Jurong's Integrated Command and Control Centre (ICC) to quickly visualise the amount of vehicles at each camera location in Singapore. This was accomplished through three steps:

1. Retrieving real-time traffic images
2. Counting the number of vehicles at each camera location through computer vision
3. Aggregating and visualising data gathered

The end product is two maps, the first being a heat map which allowed for rapid identification of key areas of interests and the second was a markered map which provided actionable data at the area of interest.

[Back to top](#table-of-contents)

# Datasets
Our prototype was developed with the following data.

1. Annual Motor Vehicle Population by Vehicle Type [[Source]](https://data.gov.sg/dataset/annual-motor-vehicle-population-by-vehicle-type)
2. Live Traffic Data [[Source]](https://data.gov.sg/dataset/traffic-images)
3. Euro VI Exhaust Emission Standards Data [[Source]](https://sso.agc.gov.sg/SL/EPMA1999-RG6?DocDate=20120629&ProvIds=Sc1-#Sc1-)

Examples of the data can be found in our [assets folder](./assets).

[Back to top](#table-of-contents)

# Development
The folders for our web application are organised in the following manner with docstrings included for necessary components to aid your understanding.

1. [Apps](./apps) - this is where you can access the  pages to our streamlit web application
2. [Componenets](./components) - this is where the code for our data visualisations are stored
3. [Assets](./assets) - this is where we store our data


[Back to top](#table-of-contents)

# The Psychics
We are a group of undergraduate students from Singapore Management University who are passionate about learning. The Code for Cities hackaton provided us with a great opportunity to learn more about both data analytics and visualisation. We even managed to learn about data science while utilising the open-sourced OpenCV computer vision model.

Despite being complete strangers before this, we managed to complete the hackaton, from conceptualisation to building an interactive web application as a proof of concept in the short 3 days and we are epecially proud of it. We are also thankful to have been able to place third for the hackaton.

Do feel free to connect with us!
- Liam Ayathan [[LinkedIn]]()[[GitHub]]()
- Biondi Lee [[LinkedIn]]()[[GitHub]]()
- Josh Ghinn [[LinkedIn]]()[[GitHub]]()
- Sherlin Choo [[LinkedIn]]()[[GitHub]]()
- Loh Kok Wee [[LinkedIn]]()[[GitHub]]()

[Back to top](#table-of-contents)