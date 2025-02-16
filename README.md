# Financial Data Extraction from PDFs

## Overview
This project extracts key financial data from PDF documents using a **text-to-text generation model (Flan-T5)**. The extracted data includes:
- **Company Name**
- **Report Date**
- **Profit Before Tax**
- **Revenue**
- **Net Profit**

The extracted data is saved as a **JSON file** for easy analysis.

## Requirements
Before running the script, ensure you have the following dependencies installed:

```bash
pip install pdfplumber transformers pandas
```

## Model Used
This project uses the **Flan-T5** model, specifically `google/flan-t5-base`, which is a **fine-tuned version of the T5 model** by Google. Flan-T5 is designed for general-purpose text-to-text transformation tasks, making it well-suited for **extracting structured financial data from unstructured PDFs**. It has been trained on instruction-following tasks, which allows it to handle prompts that require summarization and entity extraction.

### Why Flan-T5?
- **Instruction-Tuned:** Works well with structured prompts.
- **Text-to-Text Format:** Converts unstructured text into structured outputs like JSON.
- **Pretrained by Google:** Reliable and optimized for various NLP tasks.

## How to Run
### 1️⃣ Run the Python Script
If you are using a Python script, execute:
```bash
python script.py
```

### 2️⃣ Run in Jupyter Notebook
If using **Jupyter Notebook**, open `extract_data_flant5.ipynb` and run all cells.

## Output Format
The extracted data will be saved in `extracted_financial_data.json` with the following structure:

```json
{
    "Eveready": {
        "Company Name": "Eveready Industries India Limited",
        "Report Date": "December 31, 2024",
        "Profit Before Tax": "15.88 crores",
        "Revenue": "333.59 crores",
        "Net Profit": "13.05 crores"
    },
    "Amara Raja": {
        "Company Name": "Amara Raja Energy & Mobility Limited",
        "Report Date": "September 30, 2024",
        "Profit Before Tax": "323.97 crores",
        "Revenue": "3,154.30 crores",
        "Net Profit": "240.71 crores"
    }
}
```

## Troubleshooting
### File Not Found Error
Ensure that the PDF files are in the correct directory. Update file paths in `script.py` if necessary.

### JSON Formatting Issues
If the extracted JSON is not valid, check the raw output in the script and format it manually.

## License
This project is licensed under the **MIT License**.


