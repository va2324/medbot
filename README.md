# MedBot
This is a basic AI application built on top of the gpt-4o-mini LLM from OpenAI using the Langchain framework, with a frontend created from Streamlit. This application is an AI medical assistant that can generate diagnoses of medical symptoms provided by users. 

## How to Run
Download Visual Studio Code from this website: https://code.visualstudio.com/

Make sure you have Python installed on your system. Enter the command below to check if Python is already installed. If not, download Python from this website: https://www.python.org/

`python --version`

For best results, create a Python virtual environment to run the program: 
  1. Create a virtual environment with the command `python -m venv my-environment-name`
  2. Activate the virtual environment `my-environment-name\Scripts\activate`
  3. Install all required packages and run the project in the virtual environment.
  4. Deactivate the virtual environment with the command `deactivate`

Install the following packages using PIP (Python's package manager)
```
pip install langchain
pip install langchain-openai
pip install streamlit
```
Secure an OpenAI API Key by creating an account on OpenAI's website: https://openai.com/

When your account is created, navigate to the 'API keys' section of the dashboard and click "Create new secret key" to generate an API key. 
You will need to input this key into the application to run the LLM. 

Clone the project
`git clone https://github.com/va2324/medbot`

Run the project with the following command
`streamlit run medic.py`
