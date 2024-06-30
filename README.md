# Project README

## Introduction

Welcome to our project! This README file provides a comprehensive guide to understanding the challenges we encountered, and the steps required to set up the CallChimp.AI webhook. We aim to streamline the process for you, ensuring a smooth setup and integration.

## Challenges We Encountered

### Integrating Multiple Features

The first problem we faced was integrating the numerous features of our website into one cohesive platform. Combining diverse functionalities and ensuring they work seamlessly together required extensive planning, testing, and debugging.

### Integrating CallChimp AI

Integrating CallChimp AI with our project presented significant challenges:

- **Lack of Documentation:** There was no updated documentation available for the CallChimp AI Python SDK. This necessitated reading each file individually to perform basic tasks like initiating calls, which was time-consuming and inefficient.
- **Outbound Call Issues:** While using CallChimp AI's outbound calls with transactional variables, the language model (LLM) was hallucinating despite multiple script changes and different branching strategies. To resolve this, we had to update the script for each call. Although not ideal, this approach helped mitigate the hallucination issue.
- **Lata Voice Module:** The Lata voice module was not working properly, which took a significant amount of time to address. We were unaware that these voice modules could break the entire script, causing further delays and complications.

### Azure Content Filter Issues

We also faced issues with the Azure content filter. Our project involves summarizing crime cases using GPT-4.0, but Azure's filter was blocking the responses. To address this, we modified Azure's AI LLM internal configuration to change the filtration procedure.

### Conclusion

These challenges required us to adapt and find innovative solutions. While some approaches were not perfect, they enabled us to move forward and achieve our project goals.


## CallChimp.AI Webhook Setup

### Step 1: Clone the Webhook Repository

First, clone the webhook repository to your local machine:


git clone <this_repo>

### Step 2: Install Requirements

Navigate to the cloned repository and install the necessary dependencies:
pip install -r requirements.txt
bash
Copy code
pip install -r requirements.txt
### Step 3: Create a CallChimp.AI Sandbox Account

Go to CallChimp.AI and create a sandbox account.

### Step 4: Create a New Campaign

Create a new campaign in your CallChimp.AI dashboard.

Attach the following script to the campaign:

- **Script:** Blank script (just type any word because it will be updated before initializing the call).

### Step 5: Add a New List

Add a new list in your CallChimp.AI dashboard.

Add supervisors and subscribe them to your newly created list.

### Step 6: Update `initcall.py`

With your recently created lead ID, head over to `initcall.py` and add your lead ID in the provided placeholder in the code.

### Step 7: Update `updatescript.py`

With your script ID (the blank script you recently created), head over to `updatescript.py` and replace the script ID with your own.

### Step 8: Run `webhook.py`

Run the `webhook.py` script:

Copy code
python webhook.py

You will see a URL in your terminal.

### Step 9: Update `reportcrime.js`

Go to the front end of the Dashabhujha website and add the URL from the terminal in the `reportcrime.js` file, appending `/analyse` to the end of the URL.

### Step 10: Configure CallChimp.AI Webhook

Head over to your CallChimp.AI sandbox console.

Go to settings and then to the webhook section.

Add a new webhook using the same URL from step 8 but replace `/analyse` with `/webhook-endpoint`.

### Step 11: Update Environment Variables

Update the `.env` file with the following configurations:

- Your CallChimp.AI API key
- GPT-4.0 vision
- Twilio configurations

## Conclusion

Your application should now be up and running. If you encounter any issues, refer to the documentation or contact support for assistance.
