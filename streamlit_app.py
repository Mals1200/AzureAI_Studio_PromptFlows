import streamlit as st
import urllib.request
import json
import ssl
import os

# Allow self-signed certificates if needed
def allowSelfSignedHttps(allowed):
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True)

# Endpoint and API key
url = 'https://cxqa-genai-project-igysf.eastus.inference.ml.azure.com/score'
api_key = 'GOukNWuYMiwzcHHos35MUIyHrrknWibM'

# Initialize session state for storing chat history and the last message
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'last_message' not in st.session_state:
    st.session_state.last_message = ""
if 'question' not in st.session_state:  # Initialize question input in session state
    st.session_state.question = ""

# Apply CSS to set background to white, center the title, and style input
st.markdown(
    """
    <style>
        /* Set entire page background to white */
        .main {
            background-color: #ffffff;
        }
        /* Center the title and set its color */
        h1 {
            color: #000000;
            text-align: center;
        }
        
        /* Style for buttons */
        .stButton > button {
            background-color: #ffffff !important;
            color: black !important;
            border: 2px solid #000000 !important; /* Add border to buttons */
            border-radius: 5px;
            padding: 5px 10px;  /* Reduced padding for smaller buttons */
            font-size: 12px;     /* Smaller font size */
            cursor: pointer;
        }

        /* Set styles for chat container */
        .chat-container {
            max-height: 300px;
            overflow-y: auto;
            padding: 0;
            border: 2px solid #000000; /* Add border to chat container */
            border-radius: 5px;
            background-color: #ffffff;
        }
        /* Style for the input box */
        input[type="text"] {
            border: 2px solid #000000 !important;
            background-color: #ffffff !important;
            color: #333 !important;
            padding: 8px !important;
            border-radius: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Centered title
st.title("Azure Chatbot")

# Create a scrollable container for the chat history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display the chat history in reverse order so the latest appears at the top
for item in reversed(st.session_state.chat_history):
    st.markdown(
        f"""
        <div style="border: 1px solid #ddd; padding: 10px; margin: 5px 0; border-radius: 5px; background-color: #ffffff;">
            <p style="color: #000000;"><strong>You:</strong> {item['question']}</p>
            <p style="color: #000000;"><strong>Bot:</strong> {item['answer']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Close the scrollable container div
st.markdown("</div>", unsafe_allow_html=True)

# Text input for the user's question, linked to session state
question = st.text_input("Enter your question:", value=st.session_state.question, key="input_question")

# Function to call the API with the corrected format
def ask_question(question, chat_history):
    # Prepare chat history in the format expected by the API
    chat_history_list = [
        {"inputs": {"question": item["question"]}, "outputs": {"answer": item["answer"]}}
        for item in chat_history
    ]
    
    # Structure the data with 'question' and 'chat_history' as top-level keys
    data = {
        "question": question,
        "chat_history": chat_history_list  # Send all previous questions and answers in the correct format
    }
    
    body = str.encode(json.dumps(data))
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + api_key}
    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        return result
    except urllib.error.HTTPError as error:
        st.error(f"HTTP Error: {error.code}")
        st.error(f"Error details: {error.read().decode('utf8', 'ignore')}")
        return {"answer": "Error retrieving answer due to HTTP error."}
    except urllib.error.URLError as error:
        st.error(f"Network Error: {error.reason}")
        return {"answer": "Error retrieving answer due to network error."}
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return {"answer": "Unexpected error occurred. Please check your configuration."}


# Submit button to handle question submission
if st.button("Submit"):
    if question:
        # Call the API with the current question and all previous chat history
        response = ask_question(question, st.session_state.chat_history)
        answer = response.get("answer", "No answer available.")
        # Add the question and answer to history
        st.session_state.chat_history.append({"question": question, "answer": answer})
        # Store the last message in session state
        st.session_state.last_message = answer
        # Clear the input box by resetting the session state variable
        st.session_state.question = ""

# Display the last message below the buttons
if st.session_state.last_message:
    st.markdown(f"<p style='color: #000000;'><strong>Bot:</strong> {st.session_state.last_message}</p>", unsafe_allow_html=True)
