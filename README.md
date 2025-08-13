#  AI Product Review Analyzer 

Tired of scrolling through hundreds of product reviews just to figure out if something is worth buying? This AI assistant does the heavy lifting for you! It reads all the reviews, identifies the key topics, and generates a simple, easy-to-read summary of the good, the bad, and the ugly.

![Demo GIF showing the script running and the final report appearing](https://i.imgur.com/your-demo-gif-link.gif)
*(A GIF showing the terminal running the script and the final report would be perfect here!)*

---

###  How It Works: The 3-Agent System

This project isn't just one AI; it's a team of three specialized agents working together like an assembly line:

1.  ** The Theme Sorter:** This agent reads every single review and figures out *what* people are talking about. It finds recurring themes like "Battery Life," "Screen Quality," or "Noise Level."

2.  ** The Sentiment Critic:** For each theme, this agent goes back to the reviews to determine the overall feeling. It decides if the sentiment is `Positive`, `Negative`, or `Mixed`.

3.  ** The Final Reporter:** This agent takes all the structured data from the first two and writes a polished, final report. It explains *why* the sentiment is what it is and gives you a final recommendation.

### ✅ Key Features

*   **Multi-Agent System:** Uses a sophisticated pipeline of specialized AI agents for deep analysis.
*   **Automated Theme Detection:** Automatically discovers what's important to users without any manual input.
*   **Targeted Sentiment Analysis:** Goes beyond a simple overall score to analyze sentiment for each specific feature.
*   **Synthesized Reporting:** Generates a human-friendly executive summary perfect for making quick decisions.
*   **Runs Locally:** No servers or complex setup needed. Everything runs right from your computer.

---

### Tech Stack

*   **Python 3.8+**
*   **LangChain:** The core framework for building and connecting the AI agents.
*   **Google Gemini:** Powered by the `gemini-1.5-flash` model for fast and intelligent text analysis.

---

###  Getting Started: Run it in 5 Steps!

You can get this project up and running on your local machine in just a few minutes.

#### 1. Get the Code 
Clone this repository to your local machine:
git clone https://github.com/your-username/review_analyzer_ai.git
cd review_analyzer_ai

2. Set Up Your "Toolbox" (Virtual Environment) 
This creates an isolated environment for the project so it doesn't interfere with your other Python projects.
On Windows:

python -m venv venv
venv\Scripts\activate
(You'll see (venv) appear in your terminal if it worked!)

4. Install the Dependencies 
Run this single command to install all the necessary libraries:
pip install langchain langchain-google-genai python-dotenv

6. Add Your API Key & Reviews 
Get a Key: Get your free API key from Google AI Studio.
Create .env file: In the project folder, create a file named .env.
Add Key: Open the .env file and add your key like this:
GOOGLE_API_KEY="paste_your_google_api_key_here"

Add Reviews: Create a file named reviews.txt and paste in the product reviews you want to analyze.

8. Run the Magic! 
You're all set. Run the script from your terminal:
python main.py

Sit back and watch as the AI generates its detailed analysis right in your terminal!
🎯 Example Output
Here's a sample of the final report the AI generates, based on reviews for a fictional refrigerator:

============================================================
--- FINAL AI ANALYSIS REPORT ---
============================================================
# AI Analysis Report for a Refrigerator

Based on an analysis of user feedback, here is a summary of the key findings.

### Dominant Themes Identified
*   Design and Finish
*   Storage Space and Layout
*   Ice Maker Performance
*   Noise Level
*   Energy Efficiency

---
### Detailed Analysis

**1. Design and Finish:**
*   **Sentiment:** Positive
*   **AI Summary:** Users consistently praise the sleek, modern design and the effective fingerprint-proof stainless steel finish, noting that it looks amazing in their kitchens.

**2. Ice Maker Performance:**
*   **Sentiment:** Negative
*   **AI Summary:** This is the most significant point of failure according to users. The ice maker is criticized for being extremely slow to produce ice and for frequently jamming, requiring manual intervention.

---
### Executive Summary & Recommendation

**Recommendation:** This product is highly recommended for users who prioritize aesthetics and quiet operation. However, prospective buyers must be willing to tolerate a significantly flawed ice maker.
