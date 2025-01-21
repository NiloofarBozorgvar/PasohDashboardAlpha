import streamlit as st
from streamlit_option_menu import option_menu
import home2 as h
import trend as t
import simulation as s
st.set_page_config(page_title="Pasoh Forest Dashboard", layout="wide")


option_tomenu = option_menu(None, ["Home", "Trends", 'Simulation'],
    icons=['house', 'cloud-upload', "list-task", 'gear'],
    menu_icon="cast", default_index=0, orientation="horizontal")


if option_tomenu == 'Home':
    h.start_home()

if option_tomenu == "Trends":
    t.start_trend()

if option_tomenu == "Simulation":
    s.simulation_start()