import os
import google.generativeai as genai
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable")
genai.configure(api_key=api_key)

DEFAULT_FIELDS = {
    'headquarters_city': 'Unknown',
    'founded_year': 'Unknown',
    'employee_count': 'Unknown',
    'annual_revenue_usd': 'Unknown',
    'business_model': 'Unknown',
    'financing_types': 'Unknown',
    'credit_requirements': 'Unknown',
    'avg_interest_rate': 'Unknown',
    'max_financing_amount_usd': 'Unknown',
    'avg_term_months': 'Unknown'
}

def extract_company_info(text):
    # Return default values if no text provided
    if not text or text.strip() == "":
        print("No text provided for extraction, returning default values")
        return DEFAULT_FIELDS.copy()
    
    prompt = f"""
    Extract the following information from the company text:
    - headquarters_city
    - founded_year
    - employee_count
    - annual_revenue_usd
    - business_model
    - financing_types
    - credit_requirements
    - avg_interest_rate
    - max_financing_amount_usd
    - avg_term_months

    Return output as JSON. Use 'Unknown' if not found.

    Text: {text}
    """

    try:
        # Correct method for Google Generative AI - using latest model
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
    except Exception as e:
        print(f"Error calling Google AI API: {e}")
        print("Returning default values")
        return DEFAULT_FIELDS.copy()
    
    text_output = response.text

    try:
        start = text_output.find('{')
        end = text_output.rfind('}') + 1
        if start == -1 or end == -1:
            return DEFAULT_FIELDS.copy()
        json_text = text_output[start:end]
        data = json.loads(json_text)
        for key in DEFAULT_FIELDS:
            if key not in data:
                data[key] = 'Unknown'
        return data
    except Exception:
        return DEFAULT_FIELDS.copy()