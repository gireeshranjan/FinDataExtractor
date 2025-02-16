# ============================
#  Jupyter Notebook: extract_data_flant5.ipynb
# ============================

# 1) Install Dependencies (in a terminal or separate notebook cell):
# ---------------------------------------------------------
# !pip install pdfplumber transformers pandas

import pdfplumber
import json
import pandas as pd
from transformers import pipeline

# 2) Load a text-to-text model, e.g., Flan-T5
# ---------------------------------------------------------
# This pipeline can handle text2text-generation tasks
llm_extractor = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"  # or any other generative model
)

# 3) Update file paths to match your actual file locations
# ---------------------------------------------------------
pdf_files = {
    "Eveready": "1_FinancialResults_05022025142214.pdf",
    "Amara Raja": "Amaar raja Earnings Summary.pdf"
}

# 4) Extract Text from PDFs
# ---------------------------------------------------------
def extract_text_from_pdf(pdf_path):
    """
    Reads a PDF file using pdfplumber and returns extracted text.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
    return text

# 5) Prompt Model to Extract Financial Details
# ---------------------------------------------------------
def extract_financial_details_with_llm(text):
    """
    Uses a text2text model (Flan-T5) to parse unstructured text
    and produce a JSON structure with key financial details.
    """
    # We ask for data in a structured JSON format
    prompt = f"""
    You are a helpful assistant extracting financial data. 
    Please find the following details in the text below:
    - Company Name
    - Report Date
    - Profit Before Tax
    - Revenue
    - Net Profit

    Text:
    {text}

    Provide the output as valid JSON with keys exactly:
    "Company Name", "Report Date", "Profit Before Tax", 
    "Revenue", and "Net Profit".
    """

    # Generate the response
    result = llm_extractor(prompt, max_length=512)
    raw_text = result[0]["generated_text"]

    # Attempt to parse JSON. If parsing fails, store raw text in a placeholder.
    try:
        extracted_json = json.loads(raw_text)
    except json.JSONDecodeError:
        extracted_json = {"error": "Invalid JSON from model", "raw_response": raw_text}

    return extracted_json

# 6) Run Extraction for Each PDF
# ---------------------------------------------------------
extracted_texts = {company: extract_text_from_pdf(path) for company, path in pdf_files.items()}
extracted_financial_data = {
    company: extract_financial_details_with_llm(text) 
    for company, text in extracted_texts.items()
}

# 7) Save Extraction Results to JSON
# ---------------------------------------------------------
with open("extracted_financial_data.json", "w", encoding="utf-8") as f:
    json.dump(extracted_financial_data, f, indent=4, ensure_ascii=False)

# 8) Display Results in a DataFrame
# ---------------------------------------------------------
df = pd.DataFrame(extracted_financial_data).T
df
