import os
import pandas as pd
from google.cloud import translate_v2 as translate

# Set the environment variable for authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service-account-file.json'

# Initialize Google Cloud Translation client
client = translate.Client()

# Function to translate text, handling empty values
def translate_text_safe(text, target_language):
    if pd.isna(text):  # Check if the value is NaN
        return ''
    else:
        translation = client.translate(text, target_language=target_language)
        return translation['translatedText']

# Function to detect the language of a given text
def detect_language(text):
    if pd.isna(text):  # Check if the value is NaN
        return None
    else:
        detection = client.detect_language(text)
        return detection['language']

# Function to translate Excel file
def translate_excel(target_languages, excel_path):
    # Read Excel file
    excel_data = pd.read_excel(excel_path, sheet_name=None)  # Read all sheets into a dictionary of DataFrames

    # Detect source language from the first non-empty cell in the first sheet
    first_sheet = list(excel_data.values())[0]
    for cell in first_sheet.stack():
        source_language = detect_language(cell)
        if source_language:
            break
    print(f"Detected source language: {source_language}")

    # Iterate over target languages
    for target_language in target_languages:
        # Translate each sheet in the Excel file
        translated_sheets = {}
        for sheet_name, df in excel_data.items():
            print(f"Translating sheet '{sheet_name}' into '{target_language}'...")

            # Translate each column in the DataFrame
            for column in df.columns:
                df[column] = df[column].apply(lambda x: translate_text_safe(str(x), target_language))

            # Store translated DataFrame
            translated_sheets[sheet_name] = df

        # Save translated DataFrames to a new Excel file
        output_excel = f"translated_{os.path.splitext(os.path.basename(excel_path))[0]}_{target_language}.xlsx"
        with pd.ExcelWriter(output_excel) as writer:
            for sheet_name, translated_df in translated_sheets.items():
                translated_df.to_excel(writer, sheet_name=sheet_name, index=False)
        print(f"Translated content saved to {output_excel}")

if __name__ == "__main__":
    # Example usage
    target_languages = ['fr', 'es', 'de']  # Target languages (e.g., French, Spanish, German)
    excel_path = 'your_excel_file.xlsx'  # Path to your Excel file in the same directory

    translate_excel(target_languages, excel_path)
