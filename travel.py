import streamlit as st
import google.generativeai as genai
import os
import json
import pandas as pd
from datetime import datetime
import pycountry

def generate_travel_plan(country, num_adults, num_kids, travel_type, kinds_of_travelers, start_date, end_date, budget, num_days, accommodation_type, accommodation_rating, dietary_restrictions, transportation_mode, interests_activities, budget_allocation):
    input_prompt = f"""
    You are planning a trip to {country} with {num_adults} adults and {num_kids} kids. 
    Your travel type is {travel_type}.
    
    Create a detailed travel itinerary that caters to your group's interests and preferences for {num_days} days. 
    Your itinerary should cover the following aspects:

    1. **Destination Highlights:** List three must-visit attractions in {country} and explain why they're worth visiting.

    2. **Activities:** Recommend activities or experiences suitable for {kinds_of_travelers}, such as {interests_activities}.

    3. **Accommodation:** Provide options for accommodation, considering the preferences and needs of {num_adults} adults and {num_kids} kids. 
       Your preferred type of accommodation is {accommodation_type} with a rating of {accommodation_rating}.
       
    4. **Transportation:** Advise on transportation options within {country}, considering the size of your group and any specific requirements. 
       Your preferred mode of transportation is {transportation_mode}.
       
    5. **Local Cuisine:** Highlight traditional dishes and recommend places to try them, taking into account the tastes of your group members. 
       Please consider {dietary_restrictions} when making recommendations.
       
    6. **Budget Allocation:** Your estimated budget for the trip is {budget}. 
       Breakdown of budget allocation: {budget_allocation}.
       
    7. **Date Selection:** Your trip dates are from {start_date.strftime("%Y-%m-%d")} to {end_date.strftime("%Y-%m-%d")}. The duration of your trip is {num_days} days.

    Feel free to provide more details about your group's interests or ask for specific recommendations. 
    Also provide the travel day by day activity plan based on dates are from {start_date.strftime("%Y-%m-%d")} to {end_date.strftime("%Y-%m-%d")}.
    """
    return input_prompt

# Fetch list of all countries
all_countries = [country.name for country in pycountry.countries]

# Streamlit App
st.title("Travel Planner")

# Input fields
selected_country = st.selectbox("Enter the destination country:", all_countries)
start_date = st.date_input("Select trip start date:")
end_date = st.date_input("Select trip end date:")
num_adults = st.number_input("Enter the number of adults:", min_value=1, value=1)
num_kids = st.number_input("Enter the number of kids:", min_value=0, value=0)
kinds_of_travelers = st.selectbox("Describe the kinds of travelers:", ["Family", "Friends", "Solo"])
travel_type = st.selectbox("Select travel type:", ["Business", "Economy", "Other"])
accommodation_type = st.selectbox("Preferred accommodation type:", ["Hotel", "Hostel", "Airbnb"])
accommodation_rating = st.slider("Preferred accommodation rating:", 1, 5, 3)
dietary_restrictions = st.selectbox("Select dietary restrictions or health considerations:", ["None", "Vegetarian", "Vegan", "Gluten-free"])
transportation_mode = st.selectbox("Preferred mode of transportation:", ["Flight", "Train", "Rental Car", "Public Transportation"])
budget = st.number_input("Enter estimated budget:", min_value=0, value=1000)
interests_activities = st.selectbox("Enter interests or activities you'd like to include:", ["Hiking", "Sightseeing", "Cultural Events", "Shopping"])
budget_allocation = st.text_area("Enter breakdown of budget allocation for different aspects of the trip:")

# Calculate duration based on start and end date
duration = (end_date - start_date).days + 1

# Button to generate travel plan
if st.button("Generate Travel Plan"):
    input_prompt = generate_travel_plan(selected_country, num_adults, num_kids, travel_type, kinds_of_travelers, start_date, end_date, budget, duration, accommodation_type, accommodation_rating, dietary_restrictions, transportation_mode, interests_activities, budget_allocation)

    # Configure Google Generative AI
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt)

    # Display travel plan
    st.subheader("Generated Travel Plan:")
    st.write(response.candidates[0].content.parts[0].text)
