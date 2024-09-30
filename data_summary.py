# data_summary.py

from llama_index.core.tools import FunctionTool

import pandas as pd
import os

summary_file = os.path.join("data", "data_summary.txt")

# Function to generate and save data summary
def save_data_summary(df):
    summary = df.describe().to_string()
    if not os.path.exists(summary_file):
        open(summary_file, "w").close()  # Create file if not exists

    with open(summary_file, "w") as f:
        f.write("Data Summary:\n")
        f.write(summary)
    
    return "data summary saved"

population_path = os.path.join("data", "Population.csv")

population_df = pd.read_csv(population_path)

# Create FunctionTool for data summary saving
data_summary_tool = FunctionTool.from_defaults(
    fn=lambda: save_data_summary(population_df),  # Use the global dataframe
    name="data_summary_saver",
    description="This tool generates and saves a summary of the data to a file.",
)
