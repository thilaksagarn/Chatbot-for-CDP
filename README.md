# Chatbot-for-CDP
Objective

The CDP Support Agent Chatbot simplifies the process of accessing Customer Data Platform (CDP) documentation from tools like Segment, mParticle, Lytics, and Zeotap. It provides quick and accurate answers to common integration-related questions, such as setting up data sources, creating user profiles, and building audience segments.

🚀 Features

✔️ Automated Documentation Parsing – Utilizes Python's requests and BeautifulSoup libraries to scrape specific content from official CDP documentation.

✔️ Dynamic Query Handling – Responds to user queries by identifying the relevant CDP and extracting steps from structured HTML content (e.g., <p>, <strong>, or <div> tags).

✔️ Streamlit Interface – Provides an interactive and user-friendly interface for querying and displaying answers.

✔️ Error Handling – Includes robust mechanisms to handle missing sections, connection issues, and invalid queries.

🔧 Tech Stack & Why It Was Chosen

Technology

Purpose

Why?

Streamlit

Frontend

Built for an intuitive and interactive user experience.

BeautifulSoup

Documentation Parsing

Extracts specific content dynamically from structured HTML sources.

Python

Backend Logic

Manages query handling, response generation, and error management.

📂 Data Structures & Why They Were Used

Data Structure

Purpose

Why?

Dictionary ({})

Maps CDP query topics to answers

Enables efficient lookup and retrieval of content based on user queries.

Event Listeners

Captures user interactions

Handles real-time events like query submission and feedback collection.

Stack (Undo/Redo)

Manages application states

Maintains previous states to allow rollback of actions or redoing queries.

🖋️ Usage

Enter Queries: Input questions about CDP topics like "How to onboard data in Segment?".

View Answers: Receive accurate, step-by-step guidance retrieved from official documentation.

Handle Errors: In case of invalid queries or missing documentation, view helpful error messages.
