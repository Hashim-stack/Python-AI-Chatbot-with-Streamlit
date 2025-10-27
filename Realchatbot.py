import streamlit as st  # Import Streamlit for bstlding the web application
from dotenv import load_dotenv  # Import dotenv to load environment variables from a .env file
from openai import OpenAI  # Import OpenAI class for API interaction
import os  # Import os module for accessing environment variables

# Configure the Streamlit page settings
st.set_page_config(
    page_title="Hashim",  # Title of the webpage
    page_icon="🚀",  # Favicon for the webpage
    layout="wide",  # Use wide layout for better st
    initial_sidebar_state="collapsed"  # Sidebar will be collapsed initially
)

# Load environment variables from the .env file
load_dotenv()
# Retrieve the OpenAI API key from environment variables
secret_key = os.getenv("OPENAI_API_KEY")
# Initialize OpenAI client with the retrieved API key
openai_client = OpenAI(api_key=secret_key)

# Display the main title of the application
st.title("✈️ Our first travel AI Agent!!")

# Initial greeting message from the AI assistant
greeting_message = {"role": "assistant",
                    "content": "👋 Hello! I'm your AI Travel Agent. How can I assist you today?"}

# Check if session state contains messages, if not, initialize it
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": """
        Assume you are a travel agent. You used to conduct travel programs across the world!!
        Respond to queries within 2-3 sentences. If the user asks for more details, provide them in a maximum of 10 lines.
        """
         },
        greeting_message  # Add the initial greeting message to session state
    ]

# Get user input through the chat input field
prompt = st.chat_input(greeting_message["content"])

# If the user inputs a message
if prompt:
    # Add the user's message to session state
    st.session_state["messages"].append({"role": "user", "content": prompt})

    # Generate AI response using OpenAI's chat completion
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",  # Specify the GPT model to use
        messages=st.session_state["messages"],  # Provide conversation history
        # temperature=0.7,  # Adjust response randomness (optional, commented out)
        # max_tokens=300  # Limit the response length (optional, commented out)
    )

    # Extract AI's response from OpenAI API response
    ai_message = response.choices[0].message.content

    # Add AI's response to session state
    st.session_state["messages"].append({"role": "assistant", "content": ai_message})

# Display chat messages in the st
for message in st.session_state["messages"][1:]:  # Exclude system message
    with st.chat_message(message["role"]):  # Create chat message component
        st.markdown(message["content"])  # Display message content as markdown

# Sidebar content
st.sidebar.write("Welcome")  # Display text in sidebar
# Sidebar button functionality
if st.sidebar.button("Click Me"):
    st.sidebar.success("Success Message")  # Show success message in sidebar
    # st.success("Success message")  # This line is commented out, but can be used to show success message in the main Ui