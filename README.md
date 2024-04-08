# GPT-Accuracy-Research

This project focuses on analyzing the accuracy of sentiment classification using OpenAI's GPT (Generative Pre-trained Transformer) model, specifically for comments related to a particular subject, such as ChatGPT. The sentiment analysis is performed using OpenAI's Sentiment Analysis API, which utilizes the powerful GPT model for natural language understanding.

## Data Sources
     *Youtube
     *Reddit

## Features

1. Sentiment Analysis: Utilizes OpenAI's GPT model to classify comments as positive, negative, or neutral regarding a specified subject.
2. API Integration: Integrates with OpenAI's Sentiment Analysis API for accurate sentiment classification.
3. Customizable: Allows flexibility in analyzing comments related to different subjects or topics by modifying the input prompt.
4. Error Handling: Implements error handling to gracefully handle exceptions during sentiment analysis.

## How it Works

1. Initialization: Set up the OpenAI API key for authentication with the OpenAI API.
2. Sentiment Classification: The positive_negative_classifier function classifies comments as positive, negative, or neutral by invoking the OpenAI Sentiment Analysis API.
3. Data Processing: Optionally, the project can process existing data stored in a CSV file by adding a new column for the sentiment classifier results.
4. Output: Returns the sentiment classification result for a given comment.

## What all can be done with this data
1. Classify these comments as positive and negative (can be done through gpt itself)
2. See for the most occured words
3. How often people use the names of competition apps
4. Impact of those comments
5. Whether a person can switch to other competitior apps
