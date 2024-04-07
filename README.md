# Travel Planner

This application is designed to assist users in planning their travel itineraries by generating detailed plans based on their preferences and requirements.

## Features

- **Destination Highlights:** Provides a list of must-visit attractions in the selected country, along with explanations of why they're worth visiting. The list is generated based on the duration of the trip, with 60% of attractions being must-visit and 40% being optional.

- **Activities:** Recommends activities or experiences suitable for the types of travelers specified by the user.

- **Accommodation:** Offers options for accommodation based on the preferences and needs of the travelers, including the number of adults and kids, preferred type of accommodation, and desired rating.

- **Transportation:** Advises on transportation options within the selected country, considering the size of the group and any specific requirements. Users can specify their preferred mode of transportation.

- **Local Cuisine:** Highlights traditional dishes and recommends places to try them, taking into account any dietary restrictions or health considerations provided by the user.

- **Budget Allocation:** Allows users to input their estimated budget for the trip and provide a breakdown of how they'd like to allocate it across different aspects of the trip.

- **Date Selection:** Enables users to select the start and end dates of their trip, with the duration of the trip automatically calculated based on the selected dates.

## Usage

1. **Select Destination Country:** Choose the destination country from a list of available options.

2. **Select Trip Dates:** Specify the start and end dates of your trip.

3. **Enter Traveler Details:** Provide details such as the number of adults and kids, types of travelers, preferred accommodation type and rating, dietary restrictions, preferred mode of transportation, estimated budget, interests or activities, and budget allocation breakdown.

4. **Generate Travel Plan:** Click the "Generate Travel Plan" button to generate a detailed travel itinerary based on the provided information.

## Technical Implementation

- The application is built using Streamlit, a Python library for building interactive web applications.

- It utilizes the Google Generative AI API to generate content for the travel plan based on the user's input.

- The travel plan includes destination highlights, activities, accommodation options, transportation advice, local cuisine recommendations, budget allocation breakdown, and trip dates.

## Installation

To run the application locally, you'll need to install the following Python packages:

```bash
streamlit
google-generativeai
python-dotenv
langchain
PyPDF2
chromadb
openai
huggingface_hub
pycountry

## Clone the Application
git clone https://github.com/mazenalaghbari/travel-planner.git


for the installation

pip install -r requirements.txt


## runt the application
streamlit run app.py
