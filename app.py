import streamlit as st
import datetime
import requests


st.markdown("""
            # Hop on, join the _rrride_!
            """
)


'''
### Please specify:
'''


d = st.date_input(
    "Pickup date? ",
    datetime.date(2024, 8, 23))

t = st.time_input('Pickup time? ', datetime.time(00, 00))



pickup_datetime = datetime.datetime.combine(d, t)
pdt_str = pickup_datetime.strftime( "%Y-%m-%d %H:%M:%S")

pickup_longitude = st.slider('Pickup longitude? ', -74.3, -73.7 )
pickup_latitude = st.slider('Pickup latitude? ', 40.5, 40.9)
dropoff_longitude = st.slider('Dropoff longitute? ', -74.3, -73.7)
dropoff_latitude = st.slider('Dropoff latitude? ', 40.5, 40.9)


passenger_count = st.number_input('Number of passengers? ', min_value= 1,max_value= 8,step= 1)


params={ "pickup_datetime" : pdt_str,
        "pickup_longitude" : pickup_longitude,
        "pickup_latitude"  : pickup_latitude,
        "dropoff_longitude" : dropoff_longitude,
        "dropoff_latitude"  : dropoff_latitude,
         "passenger_count" : passenger_count }


url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':
#   st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

"""

### Click button to calculate fare!

"""


if st.button('Get fare'):
    st.write('Calculating...')
    response=requests.get(url, params=params)

    st.write(f" ### Your estimated price is:  __{response.json()['fare']} USD__")
else:
    pass
