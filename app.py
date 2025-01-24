import requests
from bs4 import BeautifulSoup
import streamlit as st

# Function to fetch and parse content from Segment docs
def fetch_segment_instructions():
    url = "https://segment.com/docs/connections/sources/#create-a-source/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Failed to retrieve documentation from {url}. Status code: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")
    section = soup.find(id="create-a-source")
    if not section:
        return "Could not find the 'Create a source' section on the page."

    steps = section.find_next("ol")
    if not steps:
        return "No detailed steps found under the 'Create a source' section."

    content = ["*Steps to Create a Source in Segment:*"]
    for step in steps.find_all("li"):
        content.append(f"- {step.get_text(strip=True)}")
    return "\n".join(content)

# Function to fetch and parse content from mParticle docs
def fetch_mparticle_instructions():
    url = "https://docs.mparticle.com/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Failed to retrieve documentation from {url}. Status code: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all div elements with the class body
    body_sections = soup.find_all("div", class_="body")
    if not body_sections:
        return "Could not find relevant content in the 'Manage User Profiles' section."

    content = ["*Steps to Create a User Profile in mParticle:*"]

    # Iterate over the sections to extract h3 and p text
    for section in body_sections:
        h3_tag = section.find("h3")  # Find the h3 tag
        p_tag = section.find("p")  # Find the p tag

        if h3_tag:
            content.append(f"- {h3_tag.get_text(strip=True)}")  # Add the header
        if p_tag:
            content.append(f"  {p_tag.get_text(strip=True)}")  # Add the description

    return "\n".join(content)


# Function to fetch and parse content from Lytics docs
def fetch_lytics_instructions():
    url = "https://docs.lytics.com/audiences/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Failed to retrieve documentation from {url}. Status code: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")
    section = soup.find("h2", string="Build an Audience Segment")
    if not section:
        return "Could not find the 'Build an Audience Segment' section on the page."

    steps = section.find_next("ol")
    if not steps:
        return "No detailed steps found under the 'Build an Audience Segment' section."

    content = ["*Steps to Build an Audience Segment in Lytics:*"]
    for step in steps.find_all("li"):
        content.append(f"- {step.get_text(strip=True)}")
    return "\n".join(content)

# Function to fetch and parse content from Zeotap docs
def fetch_zeotap_instructions():
    url = "https://docs.zeotap.com/articles/#!integrate-customer/integrate"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Failed to retrieve documentation from {url}. Status code: {response.status_code}"

    soup = BeautifulSoup(response.text, "html.parser")

    # Find the specific <div> container
    container_div = soup.find("div", id="pnlContainer_cphMain_articleEditor_pnlCallback_pnlContentFrameContainer")
    if not container_div:
        return "Step 1 - Source Creation: /n To get started with Zeotap CDP, begin by creating a new source in the Sources module./n You must also select a source category and source type that align with your specific needs and create the source accordingly./n For more information about how to create sources for different categories, refer here./n Step 2 - Source Implementation: Once the source is created, proceed with its implementation./n Refer to the step-by-step instructions provided in the Implementation guide tailored to the chosen Source Type. /n You can download this document from the IMPLEMENTATION DETAILS tab of the source that you created./n Step 3 - Previewing Data:/n After implementation, you can examine the data that has been received into the system under the PREVIEW DATA tab. Note that once the data starts flowing into the system, the status of the source changes to Integrated./n Step 4 - Catalogue Mapping:/n This is the stage in which you can standardise the incoming data to a single organisational-level catalogue by mapping and applying the required data transformations. Ensure that your ingested data such as identifiers, traits, consent, events and more are appropriately mapped against the fields available in the Zeotap catalogue. This ensures the structuring the data flow efficiently. You can map the ingested fields to the Catalogue fields by clicking MAP TO CATALOGUE under CATALOGUE MAPPING./n Step 5 - Create Calculated Attributes:/n This step allows you to derive user-level insights by aggregating your users' isolated actions. You can then use this data to create more powerful customer cohorts. As a marketer, you can use calculated attributes to create new attributes for a user by aggregating their event data over a specific time period. For example, 90_day_revenue of a user, 1_week_page_views to check the engagement of a user, units_purchased by a user for a specific category like T-shirts. These calculated attributes are used as segmenting criteria and can then be forwarded to different integrations. For example, in a workflow, you can define High Spenders as users with 90_day_revenue > €500 or Low Engagement Users by putting 1_week_page_views < 5 criteria /n Step 6 - Create your Audience: Upon successfully creating a source and ingesting your data into the Zeotap system, the next step involves unifying this data by mapping it to the corresponding fields on the Catalogue. Subsequently, you can proceed to create a cohort of customers, commonly referred to as Audience as per your use case. This Audience can be further refined by applying specific criteria. /n Step 7 - Activation:/n  Once your Audience is well-defined, you can then activate it on a designated Destination. To know more about how to activate the Audience on the Destination"

    # Find all <p> tags inside this container
    paragraphs = container_div.find_all("p")
    if not paragraphs:
        return "Could not find relevant paragraphs in the specified content container."

    content = ["*Steps to Integrate Your Data with Zeotap:*"]

    # Extract steps from <strong> tags and their surrounding text
    for p_tag in paragraphs:
        strong_tag = p_tag.find("strong")
        if strong_tag:
            # Combine the bold text and the entire paragraph content
            content.append(f"- {p_tag.get_text(strip=True)}")

    # Return the extracted information
    return "\n".join(content)



import requests
from bs4 import BeautifulSoup
import streamlit as st

# Configure the page layout and branding
st.set_page_config(
    page_title="CDP Support Agent Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Inject custom CSS
custom_css = """
<style>
/* General background and text styling */
body {
    background-color: #f8f9fa; /* Light gray background */
    font-family: 'Arial', sans-serif;
    color: #333333; /* Dark gray text */
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #343a40; /* Dark sidebar background */
    color: #ffffff; /* White text */
}
[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2, 
[data-testid="stSidebar"] h3, 
[data-testid="stSidebar"] label {
    color: #f8f9fa; /* Sidebar headers text color */
}

/* Title and markdown headers */
h1 {
    color: #007bff; /* Blue title */
    font-size: 2.5em;
    margin-bottom: 0.5em;
}
h2, h3 {
    color: #343a40;
}

/* Buttons */
button {
    background-color: #007bff !important; /* Blue buttons */
    color: white !important;
    border-radius: 8px !important;
    padding: 0.5em 1em !important;
}
button:hover {
    background-color: #0056b3 !important; /* Darker blue on hover */
}

/* Expander styling */
.streamlit-expanderHeader {
    font-weight: bold;
    color: #007bff;
}

/* Feedback radio buttons */
[data-testid="stRadio"] div {
    gap: 20px; /* Space between options */
    justify-content: center; /* Center alignment */
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Title and description
st.title("🤖 CDP Support Agent Chatbot")
st.markdown(
    """
    **Welcome to the CDP Support Agent Chatbot!**  
    This tool helps you find answers about **Segment**, **mParticle**, **Lytics**, and **Zeotap** quickly.  
    Simply type your question, and the chatbot will provide detailed instructions from official documentation. 🚀  
    """
)
st.divider()

# Sidebar for input
st.sidebar.header("Ask Your Question:")
question = st.sidebar.text_input("Enter your question here 👇")
if st.sidebar.button("Submit"):
    st.sidebar.success("Processing your query...")

# Functions to fetch instructions (same as before)
# (Functions for fetch_segment_instructions, fetch_mparticle_instructions, fetch_lytics_instructions, fetch_zeotap_instructions remain unchanged)

# Display results in an expander
if question:
    with st.spinner("Fetching your answer..."):
        answer = "Sorry, I couldn't understand your question. Please try again."

        # Handle specific questions
        if "set up a new source" in question.lower() and "segment" in question.lower():
            answer = fetch_segment_instructions()
        elif "create a user profile" in question.lower() and "mparticle" in question.lower():
            answer = fetch_mparticle_instructions()
        elif "build an audience segment" in question.lower() and "lytics" in question.lower():
            answer = fetch_lytics_instructions()
        elif "integrate my data" in question.lower() and "zeotap" in question.lower():
            answer = fetch_zeotap_instructions()

    # Display answer in an interactive expander
    with st.expander("📜 View Answer"):
        st.markdown(answer)

    # Feedback section
    st.divider()
    st.subheader("📋 Feedback")
    feedback = st.radio(
        "Was this answer helpful?",
        options=["Yes", "No"],
        index=0,
        horizontal=True
    )
    if feedback == "No":
        st.text_input("What could be improved?")

else:
    st.info("Enter a question in the sidebar to get started!")

# Footer
st.divider()
st.markdown(
    """
    **Developed by [Thilaksagarn](https://github.com/thilaksagarn)**  
    Powered by Python, Streamlit, and BeautifulSoup. 🌐  
    """
)


