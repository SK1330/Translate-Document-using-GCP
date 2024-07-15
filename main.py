from google.cloud import storage, translate_v2 as translate

def translate_document(data, context):
    try:
        client = storage.Client()
        translate_client = translate.Client()
        target_languages = ['es', 'fr', 'de', 'hi']  # Spanish, French, German, Hindi
        
        bucket_name = data['bucket']
        file_name = data['name']
        
        input_bucket = client.bucket(bucket_name)
        output_bucket = client.bucket('translated-documents-translation-project')
        
        blob = input_bucket.blob(file_name)
        content = blob.download_as_string()
        
        # Detect the content type to handle appropriately
        content_type = blob.content_type
        
        if content_type.startswith('text'):
            text = content.decode('utf-8')
        else:
            # Handle non-text content appropriately (binary data)
            text = content
        
        # You may need specific handling based on document type here
        # For example, PDFs may need to be converted to text first
        
        for language in target_languages:
            translated_text = translate_client.translate(text, target_language=language)['translatedText']
            output_blob = output_bucket.blob(f'{file_name}_{language}.txt')
            output_blob.upload_from_string(translated_text)
            
            print(f'Translated document saved as {file_name}_{language}.txt')
    
    except Exception as e:
        print(f'Error translating document: {str(e)}')
        raise
