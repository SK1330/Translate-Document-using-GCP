import os
import pandas as pd
from google.cloud import translate_v2 as translate

# Set the environment variable for authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service-account-file.json'

# Function to translate Excel file
def translate_excel(source_language, target_languages, excel_path):
    # Initialize the translation client
    client = translate.Client()

    # Read Excel file
    excel_data = pd.read_excel(excel_path, sheet_name=None)  # Read all sheets into a dictionary of DataFrames

    # Translate each sheet in the Excel file
    for sheet_name, df in excel_data.items():
        print(f"Translating sheet '{sheet_name}'...")
        
        # Translate each column in the DataFrame
        for column in df.columns:
            df[column] = df[column].apply(lambda x: client.translate(x, target_language=target_languages[0], source_language=source_language)['translatedText'])

        # Save translated DataFrame to a new Excel file
        output_excel = f"translated_{sheet_name}.xlsx"
        df.to_excel(output_excel, index=False)
        print(f"Translated content saved to {output_excel}")

if __name__ == "__main__":
    # Example usage
    source_language = 'en'  # Source language (e.g., English)
    target_languages = ['fr', 'es', 'de']  # Target languages (e.g., French, Spanish, German)
    excel_path = 'your_excel_file.xlsx'  # Path to your Excel file in the same directory

    translate_excel(source_language, target_languages, excel_path)
