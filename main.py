# For loading environment variables
from dotenv import load_dotenv
import os

# LangChain components
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# --- Step 1: Load Environment Variables & Initialize Model ---
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)
print("LLM Initialized.")

# --- Step 2: Load the Review Data ---
def load_reviews_from_file(filepath):
    """Reads the entire content of a text file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None

# --- Step 3: Build the Theme Extractor Agent ---
theme_extraction_prompt_template = """
You are an expert market researcher analyzing customer reviews for a new product.
Read the following block of reviews carefully.
Your goal is to identify and list the main themes or topics that customers are repeatedly talking about.

RULES:
1.  Focus on recurring topics (e.g., if multiple people mention noise, 'Noise Level' is a theme).
2.  List each unique theme only once.
3.  Make the theme names concise and clear (e.g., 'Coffee Taste', 'Build Quality').
4.  Output the themes as a simple comma-separated list. Do not add any other text or explanation.

EXAMPLE OUTPUT: Theme One, Theme Two, Theme Three

Here are the reviews:
---
{reviews_text}
---
"""
theme_extraction_prompt = PromptTemplate(
    template=theme_extraction_prompt_template, 
    input_variables=["reviews_text"]
)
theme_extraction_chain = theme_extraction_prompt | llm

def extract_themes(reviews):
    """Runs the theme extraction agent and returns a list of themes."""
    print("\nExtracting themes from reviews...")
    response = theme_extraction_chain.invoke({"reviews_text": reviews})
    themes_string = response.content
    themes_list = [theme.strip() for theme in themes_string.split(',')]
    print(f"Successfully extracted themes: {themes_list}")
    return themes_list

# --- Step 4: Build the Sentiment Analyzer Agent ---
sentiment_analysis_prompt_template = """
You are a meticulous market research analyst. Your task is to analyze a collection of product reviews for a specific theme.

First, carefully read all the reviews provided.
Then, focus ONLY on the theme of: "{theme}"

RULES:
1.  Find all sentences or phrases in the reviews that are directly related to this theme.
2.  Based on these specific comments, determine the overall sentiment for this theme.
3.  Your final output must be a single word: "Positive", "Negative", or "Mixed".
    - Use "Positive" if the comments about the theme are mostly favorable.
    - Use "Negative" if the comments about the theme are mostly unfavorable.
    - Use "Mixed" if there is a clear blend of both positive and negative comments.
4.  Do not provide any explanation or other text. Just the single-word sentiment.

Here are the reviews:
---
{reviews_text}
---
"""
sentiment_analysis_prompt = PromptTemplate(
    template=sentiment_analysis_prompt_template,
    input_variables=["reviews_text", "theme"]
)
sentiment_analysis_chain = sentiment_analysis_prompt | llm

def analyze_sentiment_for_theme(reviews, theme):
    """Runs the sentiment analysis agent for a single theme."""
    print(f"Analyzing sentiment for theme: '{theme}'...")
    response = sentiment_analysis_chain.invoke({
        "reviews_text": reviews,
        "theme": theme
    })
    sentiment = response.content.strip()
    print(f"Result: {sentiment}")
    return sentiment

# --- Step 5: Build the Report Generator Agent ---
report_generation_prompt_template = """
You are an expert market research analyst tasked with writing a final summary report.
You have been given a collection of customer reviews and a pre-analyzed list of themes and their overall sentiment.

Your goal is to synthesize all of this information into a single, comprehensive, and easy-to-read report.

RULES FOR THE REPORT:
1.  Start with a clear headline like "AI Analysis Report for [Product Name]". Since you don't know the product name, use a generic headline.
2.  List the dominant themes that were identified.
3.  For each theme, create a detailed analysis section with three parts:
    - **Sentiment:** The pre-analyzed sentiment (Positive, Negative, or Mixed).
    - **AI Summary:** A 1-2 sentence summary explaining *why* the sentiment is what it is, using specific examples from the original reviews.
4.  Conclude with a final "Executive Summary & Recommendation" that gives a balanced overview and a purchasing recommendation.
5.  The entire output should be a single, coherent block of text formatted nicely with markdown-style headings.

Here is the pre-analyzed data:
---
{analysis_results}
---

Here are the original customer reviews to pull examples from:
---
{reviews_text}
---
"""
report_generation_prompt = PromptTemplate(
    template=report_generation_prompt_template,
    input_variables=["analysis_results", "reviews_text"]
)
report_generation_chain = report_generation_prompt | llm

def generate_final_report(reviews, analyzed_data):
    """Runs the report generation agent to produce the final summary."""
    print("\nGenerating final analysis report...")
    analysis_string = "\n".join([f"- Theme: {item['theme']}, Sentiment: {item['sentiment']}" for item in analyzed_data])
    response = report_generation_chain.invoke({
        "analysis_results": analysis_string,
        "reviews_text": reviews
    })
    report = response.content
    print("Report generated successfully.")
    return report

# --- Main Execution ---
if __name__ == "__main__":
    all_reviews = load_reviews_from_file("reviews.txt")
    
    if all_reviews:
        # Step 1: Run the Theme Extractor
        extracted_themes = extract_themes(all_reviews)
        
        # Step 2: Run Sentiment Analysis for each theme
        analyzed_data = []
        if extracted_themes and extracted_themes[0]: # Ensure themes were found
            for theme in extracted_themes:
                sentiment = analyze_sentiment_for_theme(all_reviews, theme)
                analyzed_data.append({"theme": theme, "sentiment": sentiment})
        
        # Step 3: Generate the Final Report
        if analyzed_data:
            final_report = generate_final_report(all_reviews, analyzed_data)
            
            # Print the final, comprehensive report
            print("\n" + "="*60)
            print("--- FINAL AI ANALYSIS REPORT ---")
            print("="*60)
            print(final_report)
        else:
            print("\nCould not complete analysis. No data was generated from the previous steps.")