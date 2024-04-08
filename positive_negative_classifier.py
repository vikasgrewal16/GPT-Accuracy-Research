import pandas as pd
import openai
from secret import openai_api

# Set your OpenAI API key
api_key = openai_api

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to classify a comment
def positive_negative_classifier(comment):
    try:
        # Call the OpenAI Sentiment Analysis API
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Is the following comment positive or negative towards ChatGPT?\n\n{comment}\n\nSentiment:",
            max_tokens=1
        )

        # Extract the label from the API response
        label = response.choices[0].text.strip()
        print(label)
        # Determine if the comment is positive or negative
        if label.lower() == "positive":
            return "Positive"
        elif label.lower() == "negative":
            return "Negative"
        else:
            return "Neutral"  # If sentiment is neither positive nor negative

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Error"

# Read the existing CSV file into a DataFrame
# csv_filename = "/Shikhar/GPT-Accuracy-Research/youtube_gpt_video_data1.csv"
# df = pd.read_csv(csv_filename)

# # Add a new column for the comment classifier results
# df["Comment Classifier"] = df["Comments"].apply(positive_negative_classifier)

# # Save the updated DataFrame back to the CSV file
# updated_csv_filename = "/Shikhar/GPT-Accuracy-Research/youtube_data_classified.csv"
# df.to_csv(updated_csv_filename, index=False)

# print(f"Classifier results added and saved to '{updated_csv_filename}'.")
comment = "Thanks for watching! This is a deeper dive than usual -- hope it&#39;s useful. <b>And let me know what you think of the new [FACILITY] rooms!</b> The Kevins worked for months on them. Can you spot all the easter eggs?"
result = positive_negative_classifier(comment=comment)
print(result)
