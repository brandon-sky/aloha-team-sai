import streamlit as st
from datetime import datetime, timedelta
import pytz

# Define the timezones for Honolulu and Stuttgart
HNL_TZ = pytz.timezone('Pacific/Honolulu')
STR_TZ = pytz.timezone('Europe/Berlin')

def TimeBar():
    # Get the current time in Honolulu and Stuttgart
    stuttgart_time = datetime.now(STR_TZ).strftime("%d.%b, %H:%M")
    honolulu_time = datetime.now(HNL_TZ).strftime("%d.%b, %H:%M")

    # Display the time in two separate Metric Elements
    col1, col2 = st.columns(2)
    col1.metric("Stuttgart", stuttgart_time)
    col2.metric("Honolulu", honolulu_time)
    return 
