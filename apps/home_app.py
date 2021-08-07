import streamlit as st

def app():
    st.title("Traffic Psychics")
    st.markdown('''*A Singapore Management University Project*''')
    
    # HTML Description
    page_body = '''
        <link rel="stylesheet" href="https://unicons.iconscout.com/release/v4.0.0/css/line.css">
        <h2 class="">About Us</h2>
            <p>
                Hi, we are Traffic Psychics, a group of undergraduate students from Singapore Management University. Over the past decade, Singapore has seen a marked 
                increase in the number of vehicles on its roads. The vast majority of these vehicles still run on Internal Combustion Engines (ICE) which emit harmful gases, 
                compromising both the environment and human health. With this in mind, our team aims to visualize the impact of the many ICE vehicles still on Singapore’s 
                roads by utilizing open source traffic data combined with computer vision modeling.
            </p>

        <h2>The Psychics</h2>
            <p>Our team consists of:<p>
            <ul>
                <li>Liam Ayathan
                    [<a href = "https://www.linkedin.com/in/liam-ayathan-046b3816b/" target = "_blank">
                        LinkedIn
                    </a>]
                    [<a href = "https://github.com/liam-a-21" target = "_blank">
                        GitHub
                    </a>]                    
                </li>
                <li>Biondi Lee
                    [<a href = "https://www.linkedin.com/in/biondi-lee-516293158/" target = "_blank">
                        LinkedIn
                    </a>]
                    [<a href = "https://github.com/hellobiondi" target = "_blank">
                        GitHub
                    </a>]                      
                </li>
                <li>Josh Ghinn
                    [<a href = "https://www.linkedin.com/in/josh-ghinn-8a4497131/" target = "_blank">
                        LinkedIn
                    </a>]
                    [<a href = "https://github.com/JoshGhinn" target = "_blank">
                        GitHub
                    </a>]                    
                </li>
                <li>Sherlin Choo
                    [<a href = "https://www.linkedin.com/in/sherlin-choo-376096216/" target = "_blank">
                        LinkedIn
                    </a>]
                    [<a href = "https://github.com/sherxl" target = "_blank">
                        GitHub
                    </a>]                    
                </li>
                <li>Loh Kok Wee
                    [<a href = "https://www.linkedin.com/in/loh-kok-wee-59a698142/" target = "_blank">
                        LinkedIn
                    </a>]
                    [<a href = "https://github.com/lohkokwee" target = "_blank">
                        GitHub
                    </a>]     
                </li>
            </ul>
    '''
    st.markdown(page_body, unsafe_allow_html=True)
    