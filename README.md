# Task2 - Python Script

## Overview

This project retrieves news headlines, summarizes them using OpenAI's API, print and export the results to a CSV file. Follow the instructions below to set up and run the project.

## Installation

1. **Install Required Python Packages**

   To get started, install the necessary Python packages using the following command:

   ```bash
   pip install requests openai numpy pandas

2. **Configure API Keys**

   News API Key

   Open the script and replace the placeholder with your News API key:

   ```python
   NEWS_API_KEY = '<INPUT YOUR NEWS API KEY>'
   
3. **Configure OpenAI API Key**
   
   Replace the placeholder in the following line with your OpenAI API key:
   
   ```python
   client = OpenAI(api_key='<INPUT YOUR OPEN AI KEY>')
   
4. **Run the Python Script**

   Use the command line to execute the Python script:

   ```bash
   python3 Task2.py
   
5. **Check the Results**

   After running the script, review the printed results in the command line output and the generated '.csv' file in your local path.

## Notes

1. **OpenAI API Requirements**:

   OpenAI requires you to link a credit card and top up at least $5 to use the API.
  
2. **Summarizing News Content**:

   To summarize news content instead of the title, change 'title' to 'content'. Refer to line 29 in the code for this adjustment.
  
3. **Fetching More News**:

   To fetch more news articles from the News API, adjust the page size parameter. Refer to line 59 in the code for this modification.

 
