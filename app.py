import streamlit as st

from multiapp import MultiApp
from apps import home_app, background_info_app, methodology_app, prototype_app

app = MultiApp()


# Navigation
app.add_app("Traffic Psychics", home_app.app)
app.add_app("Background Information", background_info_app.app)
app.add_app("Methodology", methodology_app.app)
app.add_app("Prototype", prototype_app.app)

# Main App
app.run()