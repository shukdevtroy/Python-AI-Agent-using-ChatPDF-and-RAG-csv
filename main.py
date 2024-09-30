# main.py
import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from convo import conversation_tool
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from data_summary import data_summary_tool
from pdf import bangladesh_engine
from dotenv import load_dotenv 
load_dotenv()

conversation_file = os.path.join("data", "conversation.txt")
population_path = os.path.join("data", "Population.csv")
population_df = pd.read_csv(population_path)

population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str
)

population_query_engine.update_prompts({"pandas_prompt": new_prompt})

tools = [
    note_engine,
    conversation_tool,
    data_summary_tool,
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

while True:
    prompt = input("Enter a prompt (q to quit): ").strip()
    
    if prompt.lower() == "q":
        print("Exiting the program.")
        break
    
    result = agent.query(prompt)
    print(result)
    
    save_convo = input("Do you want to save this conversation? (y/n): ").strip().lower()
    if save_convo == 'y':
        conversation_tool.call(prompt, result)

    generate_summary = input("Do you want to generate a data summary of population data? (y/n): ").strip().lower()
    if generate_summary == 'y':
        data_summary_tool.call()

    view_convo = input("Do you want to view previous conversations? (y/n): ").strip().lower()
    if view_convo == 'y':
        if os.path.exists(conversation_file):
            with open(conversation_file, "r") as file:
                print(file.read())
        else:
            print("No previous conversations found.")

    continue_prompt = input("Do you want to ask another question? (y/n): ").strip().lower()
    if continue_prompt != 'y':
        print("Thank you. Exiting the program.")
        break
