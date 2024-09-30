# Python-AI-Agent-using-ChatPDF-and-RAG-csv

Modify the .env file and paste your OPENAI_API_KEY="your_openapi_key".

# Data Folder

This repository includes a `data` folder with the following files:

## Files

1. **Bangladesh.pdf**
   - Description: A PDF document related to Bangladesh. The content of this document may include reports, research papers, or other relevant data about Bangladesh.
   
2. **Population.csv**
   - Description: A CSV file containing population data. This file likely includes tabular data on population statistics, such as year, population size, and demographic details.
   - 
## Usage

To use these files, download the repository and navigate to the `data` folder. You can view and analyze the `.pdf` file with any PDF reader, and you can work with the `.csv` file using spreadsheet software or data analysis tools like pandas in Python.

## How to run?

python main.py

# Population and Bangladesh Data Assistant User Manual Streamlit APP

## Overview
The **Population and Bangladesh Data Assistant** is a Streamlit web application designed to assist users in querying population data and specific information about Bangladesh. The application utilizes OpenAI's GPT-3.5-turbo model to process queries and provide insightful responses.

## Features
- **Ask a Question**: Users can ask specific questions related to world population and demographics or Bangladesh-related information.
- **View Previous Conversations**: Users can view their past interactions with the assistant.
- **View Data Summary**: Access a summary of the data used in the application.
- **Save a Note**: Users can save personal notes along with timestamps.

## Getting Started

### Prerequisites
- Ensure you have Python installed on your system.
- You will need an OpenAI API key to use the application.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/shukdevtroy/Python-AI-Agent-using-ChatPDF-and-RAG-csv.git
   cd Python-AI-Agent-using-ChatPDF-and-RAG-csv
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

### Running the Application
To start the application, run:
```bash
streamlit run app.py
```
Replace `app.py` with the name of your main Python file if it differs.

## Using the Application

### Step 1: Enter OpenAI API Key
- In the sidebar, enter your OpenAI API key in the designated field.

### Step 2: Choose an Action
- The sidebar allows you to choose one of the following actions:
  - **Ask a Question**: Enter your query in the text area and click the "Submit" button. The assistant will respond based on the query.
  - **View Previous Conversations**: Click this option to display all past interactions.
  - **View Data Summary**: Access a summary of the data used in the application.
  - **Save a Note**: Input a note in the text field and click "Save Note" to store it with a timestamp.

### Step 3: Interact with the Assistant
- If you choose to ask a question, you can save the conversation by clicking the "Save this Conversation" button. This will log the entire conversation history up to that point.
- To end the conversation without saving, click the "End Conversation" button.

### Step 4: View and Save Data
- **Previous Conversations**: Access a history of your interactions with the assistant. If there are no previous conversations, a warning will be displayed.
- **Data Summary**: View a summary of the population data being utilized.
- **Saving Notes**: Notes are saved with timestamps for future reference.

## Instructions
- **Enter Your OpenAI API Key**: Required for querying.
- **Use Sidebar Options**: Navigate easily between different functionalities.
- **Multiple Queries**: Save the entire conversation by clicking the appropriate button after asking multiple questions.
- **End Conversation**: This will simply terminate the session without saving the current conversation.

## Troubleshooting
- Ensure your OpenAI API key is valid and correctly entered.
- If you encounter issues loading files, check that the data files (`conversation.txt`, `data_summary.txt`, `population.csv`) are present in the `data` directory.

## License

This repository is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for more details.

## Contact
For any issues or feedback, please open an issue in the GitHub repository or contact the developer.

---

Feel free to modify the text to fit your specific needs or preferences!





