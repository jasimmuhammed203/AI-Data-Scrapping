import pandas as pd
import os
import time
from datetime import datetime
from web_scraper import scrape_website
from ai_extractor import extract_company_info

def main():
    # Get the directory of this script and construct absolute path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    csv_path = os.path.join(project_root, 'data', 'assignment_uno_southAfrica.csv')
    
    df = pd.read_csv(csv_path)
    
    # Convert columns to object type to avoid dtype warnings
    for col in df.columns:
        if col not in ['id', 'name', 'legal_name', 'website', 'status', 'created_at']:
            df[col] = df[col].astype('object')
    
    for index, row in df.iterrows():
        print(f"Processing {row['name']}")
        text = scrape_website(row['website'])
        info = extract_company_info(text)
        for key in info:
            if key in df.columns:
                df.at[index, key] = info[key]
        df.at[index, 'updated_at'] = datetime.now()
        
        # Add small delay to avoid rate limiting
        time.sleep(1)
    
    output_path = os.path.join(project_root, 'data', 'enriched_companies.csv')
    df.to_csv(output_path, index=False)
    print("Enrichment complete. Saved to data/enriched_companies.csv")

if __name__ == "__main__":
    main()