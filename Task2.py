import requests
import openai
from openai import OpenAI
import numpy as np
import pandas as pd

# Set news API key
NEWS_API_KEY = '<INPUT YOUR NEWS API KEY>'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'
DEFAULT_COUNTRY = 'SG'  # Default country is set as Singapore, you can change to other countries as well, like "US"

# Set OpenAI API key
client = OpenAI(api_key='<INPUT YOUR OPEN AI KEY>')

def fetch_top_headlines(api_key, country=DEFAULT_COUNTRY, category=None, page_size=5):
    params = {
        'apiKey': api_key,
        'country': country,
        'pageSize': page_size
    }
    if category:
        params['category'] = category

    response = requests.get(NEWS_API_URL, params=params)
    response.raise_for_status()
    news_data = response.json()
    return [article['title'] for article in news_data['articles']]
    #If you want to summarize news content, can change 'title' to 'content', refer to the code in line 29
    #return [article['content'] for article in news_data['articles']]

def summarize_headline(headline, max_tokens=1000):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize this headline: {headline}"}
        ],
        max_tokens=max_tokens
    )
    summary = response.choices[0].message.content.strip()
    return summary

def main(country=DEFAULT_COUNTRY, category=None, page_size=5):
    try:
        headlines = fetch_top_headlines(NEWS_API_KEY, country, category, page_size)
        summaries = [summarize_headline(headline) for headline in headlines]
        
        #Original headline and summarized headline are printed and exported into news_output.csv
        df=pd.DataFrame({
            'Original Headline':headlines,
            'Summarized Headline':summaries})
        print(df)
        df.to_csv('news_output.csv')

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function, you can change the page_size based on requirement
main(country='SG', page_size=10)
