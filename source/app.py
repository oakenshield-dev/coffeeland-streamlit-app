import streamlit as st
import pandas as pd 

def main():
    st.title("Coffee Data")
    
    # Load the coffee data
    coffee_data = pd.read_csv('coffee.csv')
    
    # Display common statistics can get with pandas
    st.subheader("Coffee Data Statistics")
    st.write(coffee_data.describe())        

    # Display the columns statistics using pandas
    st.subheader("Coffee Data Columns Statistics")
    st.write(coffee_data.dtypes)    


    # List the countrys with most coffee production
    st.subheader("10 Countries with Most Coffee Production")
    countries = coffee_data.groupby('Location.Country')['Data.Production.Number of bags'].sum()
    top_countries = countries.sort_values(ascending=False).head(10)
    st.write(top_countries)

    # Display a dataset of the coffee data but can filter by Data.Type.Variety   
    st.subheader("Coffee Data")
    variety_filter = st.selectbox("Select Coffee Variety", coffee_data['Data.Type.Variety'].unique())
    filtered_data = coffee_data[coffee_data['Data.Type.Variety'] == variety_filter]
    st.write(filtered_data)

    # Display a dataset of the coffee data but can filter by Data.Type.Processing Method
    st.subheader("Coffee Data by Processing Method")
    processing_method_filter = st.selectbox("Select Processing Method", coffee_data['Data.Type.Processing Method'].unique())
    filtered_processing_data = coffee_data[coffee_data['Data.Type.Processing Method'] == processing_method_filter]
    st.write(filtered_processing_data)

if __name__ == "__main__":
    main()
    