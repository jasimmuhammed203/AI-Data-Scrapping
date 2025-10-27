# 🧠 AI-Driven Company Data Enrichment Pipeline

### 📌 Overview
This project automates the enrichment of company data by extracting missing information from publicly available online sources.  
It combines **web scraping** with **AI-based text understanding** using Google’s Generative AI (`gemini-2.5-flash`) to extract structured attributes like:

- Headquarters city  
- Founded year  
- Employee count  
- Annual revenue (USD)  
- Business model  
- Financing types  
- Credit requirements  
- Average interest rate  
- Maximum financing amount (USD)  
- Average term (months)  

This system was developed as part of an internship evaluation task and demonstrates practical knowledge in **AI, automation, and data engineering**.

---

## 🏗️ System Architecture

### **1. Data Ingestion**
- Reads company data from a CSV file using **pandas**.
- Detects missing fields for enrichment.

### **2. Data Source Identification**
- Identifies public sources, mainly **company websites**, for relevant text content.

### **3. Web Scraping**
- Uses `requests` and `BeautifulSoup` to fetch text content.
- Removes scripts, styles, and irrelevant tags.
- Extracts and cleans human-readable text.

### **4. AI Extraction**
- Sends scraped text to **Google Generative AI (Gemini 2.5 Flash)**.
- Uses structured prompts to extract fields as JSON.
- Automatically fills missing attributes in the dataset.

### **5. Validation & Normalization**
- Validates extracted data (e.g., year ≤ current year, percentages between 0–100).  
- Normalizes numeric fields (e.g., converts "$1.2M" → `1200000`).  
- Replaces any missing values with `"Unknown"` for data consistency.

### **6. Storage**
- Saves the final enriched dataset as `enriched_companies.csv`.
- Each record includes a timestamp column (`updated_at`).

### **7. Automation**
- Adds small time delays between iterations to prevent rate limits.
- Includes logging and error handling for smooth operation.

---

## 🤖 AI Extraction Approach

| Technique | Purpose | Example |
|------------|----------|----------|
| **LLM (Gemini)** | Extract complex contextual info like business models or credit terms | “Company offers microloans…” → `business_model = lending platform` |
| **NER (Named Entity Recognition)** | Detect structured fields like cities, dates, and numbers | “Founded in 2015 in Cape Town” → `founded_year = 2015` |
| **Pattern-Based Parsing** | Extract numerical data using regex patterns | “Interest rate up to 12%” → `avg_interest_rate = 12%` |

🧩 A **hybrid approach** ensures accurate and flexible extraction across multiple data types.

---

## ✅ Data Quality & Reliability

1. **Field validation**: Every field is checked for type and range.  
2. **Cross-source verification**: Can cross-check data across multiple pages if expanded.  
3. **Normalization**: All units, currencies, and city names standardized.  
4. **Logging**: Errors, missing data, and timestamp logs maintained.  
5. **Human-in-the-loop**: Low-confidence results can be flagged for review.

---

## 🧱 Schema Materialization

| Field | Data Type | Example | Validation |
|-------|------------|----------|-------------|
| headquarters_city | String | "Johannesburg" | Must be text |
| founded_year | Integer | 2010 | 4-digit ≤ current year |
| employee_count | Integer | 200 | > 0 |
| annual_revenue_usd | Float | 1200000 | ≥ 0 |
| avg_interest_rate | Float | 10.5 | 0–50 |
| updated_at | Datetime | 2025-10-26 | Valid timestamp |

---

## ⚙️ Scalability & Ethics

### **Scalability**
- Parallel processing using async tasks for large datasets.  
- Cloud deployment (AWS/GCP) for high-volume enrichment.  
- Cached requests and deduplication for faster processing.  

### **Ethics & Compliance**
- Respects `robots.txt` and avoids scraping personal data.  
- Complies with data privacy standards (GDPR, CCPA).  
- Uses AI responsibly with transparent logic and validation.  

---

## 🧩 Folder Structure

<pre>
```
smartphone_finance_enrichment/
│
├── data/
│   ├── assignment_uno_southAfrica.csv      # Original dataset
│   └── enriched_companies.csv              # Output with enriched data
│
├── scripts/
│   ├── ai_extractor.py                     # AI extraction logic using Gemini API
│   ├── pipeline.py                         # Main enrichment pipeline
│   └── web_scraper.py                      # Web scraping logic
│
├── .env                                   # Contains your Google API key
├── requirements.txt                       # Python dependencies
└── README.md                              # Project documentation
```
</pre>

---

