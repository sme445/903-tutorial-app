import pandas as pd
import streamlit as st
import numpy as np
import json 
import plotly.express as px

def ingress(df):
    # TODO convert the birthday column to datetimes
    # TODO convert strings to ints e.g. '1' = 1
    df['SEX']=df['SEX'].map(
        {1:'Male',
         2:'Female'}
    )
    df['DOB']=pd.to_datetime(df['DOB'],format='%d/%m/%Y',errors = 'coerce')
    df['AGE']=pd.to_datetime('today').normalize() - df['DOB']
    df['AGE']=(df['AGE']/np.timedelta64(1,'Y')).astype('int')
    return df
def gender_count(df):
    male = len(df[df['SEX']=='Male'])
    female =     len(df[df['SEX']=='Female'])

    return male, female

def child_count(df):
    return len(df['CHILD'].unique())

# Page Title
st.title("903 Header Analysis App")
# Button to upload file
upload =st.file_uploader("Upload 903 Header File")


if upload:

    df = pd.read_csv(upload)
 
 #   with st.sidebar:
 #       ethnicities = st.sidebar.multiselect(
 #           'Select Ethnicity',
 #           df['ETHNIC'].unique,
 #           df['ETHNIC'].unique            
 #       )

    df = ingress(df) # recode genders

    child_pop = child_count(df)
    male, female = gender_count(df)
    mean_age = round(df['AGE'].mean(),0)
    st.write(f'The total population of children is: {child_pop}.')
    st.write(f'The total number of males is: {male}')
    st.write(f'The total number of females is: {female}')
    st.write(f'The average age is {mean_age}')

    gender_bar = px.bar(df,x='SEX',
                        title='Number of CYPs in each Sex',
                        labels={'SEX':'Sex',
                                'count':'Number of CYPs'})

    ethnic_bar = px.bar(df,x='ETHNIC',
                        title='Number of CYPs by Ethnicity',
                        labels={'ETHNIC':'Ethnicity',
                                'count':'Number of CYPs'})

    age_histogram = px.histogram(df['AGE'],
                        title='Number of CYPs by Age',
                        labels={'AGE':'Age',
                                'count':'Frequency'})
    st.plotly_chart(age_histogram)
    st.plotly_chart(gender_bar)
    st.plotly_chart(ethnic_bar)

    st.dataframe(df)