# Chatbot-for-CDP 

The **CDP Support Agent Chatbot** simplifies the process of accessing **Customer Data Platform (CDP)** documentation from tools like **Segment**, **mParticle**, **Lytics**, and **Zeotap**. It provides quick and accurate answers to common integration-related questions, such as setting up data sources, creating user profiles, and building audience segments.

---

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/593ad010-1691-428a-989c-3e9c33bec984)


---

## 🚀 Features  
✔️ **Automated Documentation Parsing** – Utilizes Python's `requests` and `BeautifulSoup` libraries to scrape specific content from official CDP documentation.  
✔️ **Dynamic Query Handling** – Responds to user queries by identifying the relevant CDP and extracting steps from structured HTML content (e.g., `<p>`, `<strong>`, or `<div>` tags).  
✔️ **Streamlit Interface** – Provides an interactive and user-friendly interface for querying and displaying answers.  
✔️ **Error Handling** – Includes robust mechanisms to handle missing sections, connection issues, and invalid queries.  

---

## 🏗️ Tech Stack & Why It Was Chosen  

| Technology       | Purpose                            | Why?                                                                                 |
|------------------|------------------------------------|-------------------------------------------------------------------------------------|
| **Streamlit**    | Frontend                          | Built for an intuitive and interactive user experience.                            |
| **BeautifulSoup**| Documentation Parsing             | Extracts specific content dynamically from structured HTML sources.                |
| **Python**       | Backend Logic                     | Manages query handling, response generation, and error management.                 |

---

## 📂 Data Structures & Why They Were Used  

| Data Structure       | Purpose                                  | Why?                                                                                 |
|----------------------|------------------------------------------|-------------------------------------------------------------------------------------|
| **Dictionary (`{}`)**| Maps CDP query topics to answers         | Enables efficient lookup and retrieval of content based on user queries.            |
| **Event Listeners**  | Captures user interactions               | Handles real-time events like query submission and feedback collection.             |
| **Stack (`Undo/Redo`)**| Manages application states               | Maintains previous states to allow rollback of actions or redoing queries.          |

---

## 📝 Usage  
1. Enter queries about CDP topics like "How to onboard data in Segment?".  
2. View accurate, step-by-step guidance retrieved from official documentation.  
3. If a query is invalid or documentation is unavailable, the chatbot displays helpful error messages.  

---

## Challenges Overcome  
- Parsing inconsistent HTML structures across different documentation platforms.  
- Extracting nested content (e.g., `<strong>` inside `<p>`) accurately while maintaining the logical flow of instructions.  

---

## Outcome  
The chatbot successfully provides step-by-step guidance for integration processes, making it a reliable tool for CDP-related tasks.

---

## Future Enhancements  
- Add support for additional CDPs.  
- Implement natural language processing (NLP) for better query understanding.  
- Enable multi-language support for international documentation.
📦 Installation
Clone the repository:
git clone https://github.com/thilaksagarn/Chatbot-for-CDP.git
Navigate to the project directory:
cd Chatbot for CDP
Open app.py in a browser to run the application.
