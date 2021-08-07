import streamlit as st

def app():
    # HTML Description
    home_overview = '''
        <link rel="stylesheet" href="https://unicons.iconscout.com/release/v4.0.0/css/line.css">
        <h1>Traffic Psychics</h1>  
            <p><i>August 2021</i></p>
            <p>
                This project was conducted as part of a submission to Surbana Jurong and Singapore Management University's "Code for Cities: Environmental Sustainability 
                and Resiliency" Hackaton.
            </p>
            <p>
                This interactive web application serves as a platform for us to document and demonstrate our entire journey, from ideation to conceptualisation and 
                eventually creating the prototype. Enjoy! 
            </p>
        <h2>A Brief Overview</h2>
            <p>
                Over the past decade, Singapore has seen a marked increase in the number of vehicles on its roads. The vast majority of these vehicles still run on Internal 
                Combustion Engines (ICE) which emit harmful gases, compromising both the environment and human health. With this in mind, our team aims to visualize the 
                impact of the many ICE vehicles still on Singapore’s roads by utilizing open source traffic data combined with computer vision modeling.
            </p>
    '''
    st.markdown(home_overview, unsafe_allow_html=True)
    st.image("./assets/prototype_demo.gif")

    home_about = '''
        <h2>The Psychics</h2>
            <p>
                We are a group of undergraduate students from Singapore Management University. Entering the competition as strangers, this was a great opportunity for us to 
                not only learn more about data analytics and visualisation through directly applying our knowledge, but also meet like minded individuals who are passionate about
                the field.
            </p>
            <p>
                Feel free to view our source code <a href = "https://github.com/lohkokwee/Traffic_Psychics" target = "_blank">here</a> and connect with us through the links below!
            </p>
            <ul>
                <li>Liam Ayathan
                    <a href = "https://www.linkedin.com/in/liam-ayathan-046b3816b/" target = "_blank"></i><i class="uil uil-linkedin"></i></a> 
                    <a href = "https://github.com/liam-a-21" target = "_blank"><i class="uil uil-github"></a>
                </li>
                <li>Biondi Lee
                    <a href = "https://www.linkedin.com/in/biondi-lee-516293158/" target = "_blank"><i class="uil uil-linkedin"></a>
                    <a href = "https://github.com/hellobiondi" target = "_blank"><i class="uil uil-github"></a>
                </li>
                <li>Josh Ghinn
                    <a href = "https://www.linkedin.com/in/josh-ghinn-8a4497131/" target = "_blank"><i class="uil uil-linkedin"></a>
                    <a href = "https://github.com/JoshGhinn" target = "_blank"><i class="uil uil-github"></a>
                </li>
                <li>Sherlin Choo
                    <a href = "https://www.linkedin.com/in/sherlin-choo-376096216/" target = "_blank"><i class="uil uil-linkedin"></a>
                    <a href = "https://github.com/sherxl" target = "_blank"><i class="uil uil-github"></a>
                </li>
                <li>Loh Kok Wee
                    <a href = "https://www.linkedin.com/in/loh-kok-wee-59a698142/" target = "_blank"><i class="uil uil-linkedin"></a>
                    <a href = "https://github.com/lohkokwee" target = "_blank"><i class="uil uil-github"></a>
                </li>
            </ul>
    '''
    st.markdown(home_about, unsafe_allow_html=True)
    