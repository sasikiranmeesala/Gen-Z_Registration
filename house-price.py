import numpy as np
import pickle
import streamlit as st#create account in Streamlit
#map the data
#location,status,property type and facing
location_mapping = {
  'Achutapuram':0,
  'Aganampudi': 1,
  'Akkayyapalem':2,
  'Anakapalle':3,
  'Anandapuram':4,
  'Asilmetta':5,
  'Atchutapuram':6,
  'Auto Nagar':7,
  'Ayinada':8,
  'Bakurupalem Anandapuram Road':9,
  'Balayya Sastri Layout':10
}
#in similar way we do for status,facing and property type
status_mapping = { 'New':0,  'Ready to move':1, 'Resale' :2,  'Under Construction':3}
direction_mapping = {
    'East':0,
    'None':1,
    'North':2,
    'NorthEast':3,
    'NorthWest':4,
    'South':5,
    'SouthEast':6,
    'West':7}
property_type_mapping = {'Apartment':0,
'Independent House':1,
'Residential Plot':2,
'Villa':3}
#reading pickle file
with open("House_price.pkl",'rb')as f:
    model=pickle.load(f)
#create a function to accept inputs and create an array
def predict(Place,Area,Status,Rooms,Bathrooms,Facing,p_Type):
    """Function to accept data"""
    selected_location = location_mapping[Place]
    selected_status = status_mapping[Status]
    selected_direction = direction_mapping[Facing]
    selected_property = property_type_mapping[p_Type]
    input_data = np.array([[selected_location,Area,selected_status,Rooms,Bathrooms,selected_direction,selected_property]])
    return model.predict(input_data)[0]

if __name__ == "__main__":
    st.header("House Price Prediction")
    col1, col2 = st.columns([2, 1])
    bed = col1.slider("No.of Bedrooms",max_value=10,min_value=1,
                      value=2)
    bath = col1.slider("No.of Bathrooms",max_value=10,min_value=0,
                       value=2)
    loc = col1.selectbox("Select a Location",list(location_mapping.keys()))
    size = col1.number_input("Area",max_value=10000,
                             min_value = 500,value=1000,step=500)
    status = col1.selectbox("Select the Status",list(status_mapping.keys()))
    facing = col1.selectbox("Select a Facing",list(direction_mapping.keys()))
    Type = col1.selectbox("Select Property Type",
                          list(property_type_mapping.keys()))
    result = predict(loc,size,status,bed,bath,facing,Type)
    submit_button = st.button("Submit")
    if submit_button:
        larger_text = f"<h2 style='color: blue;'>The Predicted House Price is : {result} Lakhs</h2>"
        st.markdown(larger_text, unsafe_allow_html=True)
        




    
    
    

    
    










                            
    
    
    
    





