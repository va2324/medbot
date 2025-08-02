import time
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_google_community import GoogleSearchAPIWrapper
from langchain.agents import Tool, AgentType, initialize_agent
from dotenv import load_dotenv

load_dotenv()

st.title("MedBot")

template = """
    You are an advanced intelligence agent who serves as a medical assistant. Your job is to provide a detailed medical diagnosis 
    based on accurate information from reliable medical websites when given a list of physiological symptoms that the user is experiencing. 
    Recommend possible treatments for their medical problem, but always remind them to consult with a medical professional about their problem.

    Symptoms: {symptoms}

    Diagnosis:"""

prompt = PromptTemplate(input_variables=["symptoms"], template=template)

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

chain = prompt | llm

search = GoogleSearchAPIWrapper()

toolkit = [
    Tool(
        name="google-search",
        description="Search for Google results on reliable medical websites. Use the chain tool to present results to the user in a detailed manner.",
        func=search.run
    ),
    Tool(
        name="chain",
        description="Provide detailed diagnosis and treatment recommendations to user based on search results",
        func=chain.invoke
    )
]

agent = initialize_agent(
    tools=toolkit,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def stream(text):
    for char in text:
        yield char
        time.sleep(0.02)

def diagnose(symptoms):
    diagnosis = agent.run(symptoms)
    st.write_stream(stream(diagnosis))

with st.form("form"):
    symptoms = st.text_area(label="Enter symptoms: ")
    submitted = st.form_submit_button("Generate Diagnosis")
    if submitted:
        if symptoms == "":
            st.warning("Please enter your symptoms to generate a diagnosis!", icon="⚠")
        else:
            with st.spinner("Diagnosing symptoms"):

                diagnose(symptoms)
