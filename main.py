import os
from google.cloud import translate_v2 as translate

# Set the environment variable for authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service-account-file.json'

# Function to translate document
def translate_document(source_language, target_languages, document_path):
    # Initialize the translation client
    client = translate.Client()

    # Read the document content
    with open(document_path, 'r', encoding='utf-8') as file:
        document_content = file.read()

    # Translate to each target language
    for target_language in target_languages:
        print(f"Translating to {target_language}...")
        translation = client.translate(document_content, target_language=target_language, source_language=source_language)

        # Save translated content to a file
        output_file = f"translated_{target_language}.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(translation['translatedText'])

        print(f"Translated content saved to {output_file}")

if __name__ == "__main__":
    # Example usage
    source_language = 'en'  # Source language (e.g., English)
    target_languages = ['fr', 'es', 'de']  # Target languages (e.g., French, Spanish, German)
    document_path = 'your_document.txt'  # Name of your document in the same directory

    translate_document(source_language, target_languages, document_path)
