import streamlit as st
import google.generativeai as genai
import os
import json
import pandas as pd

def generate_travel_plan(country, num_adults, kinds_of_travelers, start_date, end_date, budget, num_days):
    input_prompt = f"""
    You are planning a trip to {country} with {num_adults} adults and {kinds_of_travelers}. Create a detailed travel itinerary that caters to your group's interests and preferences for {num_days} days. Your itinerary should cover the following aspects:

    1. **Destination Highlights:** List three must-visit attractions in {country} and explain why they're worth visiting.

    2. **Activities:** Recommend activities or experiences suitable for {kinds_of_travelers}, such as adventure sports, cultural events, family-friendly activities, engineering experiences, culinary adventures, entertainment options, and other fantastic activities.

    3. **Accommodation:** Provide options for accommodation, considering the preferences and needs of {num_adults} adults and {kinds_of_travelers}. Mention the best areas to stay for different preferences and budgets.

    4. **Transportation:** Advise on transportation options within {country}, considering the size of your group and any specific requirements.

    5. **Local Cuisine:** Highlight traditional dishes and recommend places to try them, taking into account the tastes of your group members.

    6. **Cultural Insights:** Share insights into the local culture, customs, and festivals that would interest your group.

    7. **Safety Tips:** Offer essential safety tips tailored to your group's needs and concerns, including health precautions and advice on respecting local customs.

    8. **Date Selection:** Your trip dates are from {start_date.strftime("%Y-%m-%d")} to {end_date.strftime("%Y-%m-%d")}. The duration of your trip is {num_days} days.

    9. **Budget Estimation:** Your estimated budget for the trip is {budget}.

    10. ** Day by Day activities  : **
        I want to see in table your suuport as I'm planning a trip to [Destination] from [Start Date] to [End Date].  I'd like a detailed daily itinerary that includes breakfast, lunch, and dinner suggestions. While I'd love to see as much as possible, I'm also interested in having some time to relax and enjoy each location.  Please prioritize interesting and culturally significant places over cramming in too many.  Let me know the estimated travel time between locations, and suggest transportation options.

    

    Feel free to provide more details about your group's interests or ask for specific recommendations. also provide the travel day by day activity plan base on dates are from {start_date.strftime("%Y-%m-%d")} to {end_date.strftime("%Y-%m-%d")}.

    """
    return input_prompt

# Streamlit App
st.title("Travel Planner")

# Input fields
country = st.text_input("Enter the destination country:")
num_adults = st.number_input("Enter the number of adults:", min_value=1, value=1)
kinds_of_travelers = st.selectbox("Describe the kinds of travelers", ["Family", "Friends", "Solo"])
start_date = st.date_input("Select trip start date:")
end_date = st.date_input("Select trip end date:")
budget = st.number_input("Enter estimated budget:", min_value=0, value=1000)
num_days = st.number_input("Enter the number of days for the trip:", min_value=1, value=7)

# Button to generate travel plan
if st.button("Generate Travel Plan"):
    input_prompt = generate_travel_plan(country, num_adults, kinds_of_travelers, start_date, end_date, budget, num_days)

    # Configure Google Generative AI
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_prompt)

    # Display travel plan
    st.subheader("Generated Travel Plan:")
    st.write(response.candidates[0].content.parts[0].text)
