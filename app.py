import os
import pandas as pd
import streamlit as st
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from data_summary import data_summary_tool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# File paths
conversation_file = os.path.join("data", "conversation.txt")
summary_file = os.path.join("data", "data_summary.txt")
population_path = os.path.join("data", "Population.csv")
population_df = pd.read_csv(population_path)

# Set up the Streamlit app
st.title("🌎 Population and Bangladesh Data Assistant")

# Sidebar for OpenAI API key
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password", placeholder="sk-...")
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

# Import bangladesh_engine and handle import error
try:
    from pdf import bangladesh_engine
except ImportError as e:
    st.error(f"Import error: {e}. Please ensure 'pdf.py' is in the correct directory and has 'bangladesh_engine' defined.")

# Initialize query engines
population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str
)

population_query_engine.update_prompts({"pandas_prompt": new_prompt})

tools = [
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="Provides information about world population and demographics",
        ),
    ),
    QueryEngineTool(
        query_engine=bangladesh_engine,
        metadata=ToolMetadata(
            name="bangladesh_data",
            description="Provides detailed information about Bangladesh",
        ),
    ),
]

llm = OpenAI(model="gpt-3.5-turbo")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

# Sidebar options
st.sidebar.header("Options")
option = st.sidebar.selectbox("Choose an action:", [
    "Ask a Question",
    "View Previous Conversations",
    "View Data Summary",
    "Save a Note"
])

# Conversation management
conversation_active = st.session_state.get('conversation_active', False)

if option == "Ask a Question":
    if not conversation_active:
        st.session_state.conversation_active = True
        st.session_state.conversation_history = []
    
    prompt = st.text_area("Enter your query:", key="user_input")
    
    if st.button("Submit"):
        if prompt:
            result = agent.query(prompt)
            response_text = result.response  # Extract just the response text
            st.write("Response:", response_text)  # Show only the response text

            # Save the conversation with a timestamp
            timestamp = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state.conversation_history.append((timestamp, prompt, response_text))
        else:
            st.error("Please enter a query.")
    
    if st.button("Save this Conversation"):
        # Save entire conversation history to the file
        with open(conversation_file, "a") as file:
            for timestamp, user_prompt, bot_response in st.session_state.conversation_history:
                file.write(f"Timestamp: {timestamp}\n")
                file.write(f"Prompt: {user_prompt}\n")
                file.write(f"Response: {bot_response}\n")
                file.write("=" * 40 + "\n")
        st.success("Conversation saved.")

    if st.button("End Conversation"):
        st.session_state.conversation_active = False
        st.success("Conversation ended.")

# View previous conversations
elif option == "View Previous Conversations":
    if os.path.exists(conversation_file):
        with open(conversation_file, "r") as file:
            st.text_area("Previous Conversations", file.read(), height=300)
    else:
        st.warning("No previous conversations found.")

# View data summary
elif option == "View Data Summary":
    if os.path.exists(summary_file):
        with open(summary_file, "r") as file:
            st.text_area("Data Summary", file.read(), height=300)
    else:
        st.warning("No data summary found.")

# Save a note
elif option == "Save a Note":
    note = st.text_input("Enter a note to save:")
    if st.button("Save Note"):
        if note:
            # Append note to the conversation file with a timestamp
            timestamp = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(conversation_file, "a") as file:
                file.write(f"Timestamp: {timestamp} (Note)\n")
                file.write(f"Note: {note}\n")
                file.write("=" * 40 + "\n")  # Separator for readability
            st.success("Note saved.")
        else:
            st.error("Please enter a note.")

# Instructions
st.sidebar.subheader("Instructions")
st.sidebar.write(
    "1. Enter your OpenAI API Key in the sidebar.\n"
    "2. Use the sidebar to choose an action: ask a question, view previous conversations, view the data summary, or save a note.\n"
    "3. If you ask a question and click save, the conversation will be saved. If you ask multiple questions and then press save, it will save the whole conversation.\n"
    "4. The End Conversation button will simply end the conversation without saving anything.\n"
)
