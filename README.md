# Trasnlate Documents using Google Cloud Translation API

## Using this script you will be able to translate text document into Multiple languages. Checkout the other branches as well

## Description
Hello, All ! I have written the python script that can be used to translate the document using google translation API.

I have created a seperate branches for different file translation

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usuage](#usuage)


## Prerequisites
1. Install Pyhton and Pip and pandas
2. Create a GCP Account (Google Cloud Platform)

## Usuage
Step 1: Create a GCP Project
    1. Go to the GCP Console: GCP Console
    2. Create a New Project

Step 2: Enable the Cloud Translation API
    1. Navigate to the API Library: In the GCP Console, go to the menu and select "APIs & Services" > "Library."
    2. Enable Cloud Translation API: Search for "Cloud Translation API."

Step 3: Set Up Service Account
    1. Create a Service Account: Go to "IAM & Admin" > "Service Accounts."
    2. Grant Permissions: In the permissions step, select "Project" > "Editor" to grant the necessary permissions.
    3. Create a Key: Find your new service account, Go to the "Keys" tab and click "Add Key" > "Create New Key."

Step 4: Install Google Cloud SDK and Libraries
    1. Install Google Cloud SDK: Follow the installation guide for your OS ([Install Google Cloud SDK](https://cloud.google.com/sdk/docs/install))
    2. Install Python Libraries: pip install google-cloud-storage google-cloud-translate

Step 5: Clone this repository and modify the main.py
    1. Service Account Key: Specify the path to your Google Cloud service account key file. Change "(service-account-file.json)"
    2. Document Path: Update document_path with the path to your document that you want to translate. Replace 'your_document.txt' with the actual filename of your document

Step 6: Execute the script to translate text Doucments into multiple languages
    1. python main.py
    2. wait for the ouput. Output will be saved in the same directory.

### 
- **Make sure both your Python script (script.py) and your service account JSON file (service-account-file.json) are in the same directory. This setup should work seamlessly for your translation task.

