#!/usr/bin/env python3
"""
Setup script to help configure the Google API key
"""
import os

def setup_api_key():
    print("Google Generative AI API Key Setup")
    print("=" * 40)
    print("1. Go to: https://makersuite.google.com/app/apikey")
    print("2. Create a new API key")
    print("3. Copy the API key")
    print()
    
    api_key = input("Enter your Google API key: ").strip()
    
    if not api_key:
        print("No API key provided. Exiting.")
        return
    
    # Create .env file content
    env_content = f"# Google Generative AI API Key\nGOOGLE_API_KEY={api_key}\n"
    
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ API key saved to .env file")
        print("You can now run: python scripts/pipeline.py")
    except Exception as e:
        print(f"❌ Error saving API key: {e}")
        print("You can manually create a .env file with:")
        print(f"GOOGLE_API_KEY={api_key}")

if __name__ == "__main__":
    setup_api_key()
