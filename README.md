# MedBot
This is a basic AI application built on top of the gpt-4o-mini LLM from OpenAI using the Langchain framework, with a frontend created from Streamlit. This application is an AI medical assistant that can generate diagnoses of medical symptoms provided by users and recommend possible treatments. It is integrated with Google Search to provide accurate information from reliable medical websites. 

## How to Run
Download Visual Studio Code from this website: https://code.visualstudio.com/

Clone the project with the following command.

```
git clone https://github.com/va2324/medbot
```

Make sure you have Python installed on your system. Enter the command below to check if Python is already installed. If not, download Python from this website: https://www.python.org/

```
python --version
```

For best results, create a Python virtual environment to run the program: 
  1. Create a virtual environment with the command `python -m venv my-environment-name`
  2. Activate the virtual environment `my-environment-name\Scripts\activate`
  3. Install all required packages and run the project in the virtual environment.
  4. Deactivate the virtual environment with the command `deactivate`

Install the following packages using PIP (Python's package manager)
```
pip install langchain
pip install langchain-community
pip install langchain-openai
pip install openai
pip install google-api-python-client
pip install streamlit
pip install python-dotenv
```

## API Keys
### OpenAI
Secure an OpenAI API Key by creating an account on OpenAI's website: https://openai.com/

When your account is created, navigate to the **API keys** section of the dashboard and click **Create new secret key** to generate an API key. 

### Google
Secure a Google API key by going to this website: https://console.developers.google.com/

Select a project or create a new one. Navigate to the **APIs & Services** page and choose **Credentials** on the left. Click **Create credentials** and then select **API key**.
Once the key is created, under **API Restrictions**, restrict the API key to the Custom Search API. Be sure to enable the Custom Search API on the **Enabled APIs & Services** page.

### Custom Search Engine
Create a Custom Search Engine by going to this website and click **Get Started**: https://programmablesearchengine.google.com/

You will be redirected to a form for creating a new search engine. Provide a name for the search engine. It is not necessary to add sites to search or change search settings. Just click the verification box and click **Create**. Once the search engine has been created, click **Back to all engines** and select the engine you just created. Navigate to the **Basic** section of the Overview page and copy the **Search Engine ID**.

Inside the project, create a new file '.env' and write the following:
```
OPENAI_API_KEY = your_openai_key
GOOGLE_API_KEY = your_google_key
GOOGLE_CSE_ID = your_cse_id
```

Run the project with the following command.
```
streamlit run medic.py
```
