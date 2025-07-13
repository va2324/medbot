import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

st.title("MedBot")

def diagnose(symptoms):
    template = """
    You are an advanced intelligence agent who serves as a medical assistant. Your job is to provide a medical diagnosis when given a list 
    of physiological symptoms that the user is experiencing. Recommend possible treatments for their medical problem, but always remind them 
    to consult with a medical professional about their problem.

    Symptoms: {symptoms}

    Diagnosis:"""

    prompt = PromptTemplate(input_variables=["symptoms"], template=template)

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    chain = prompt | llm

    diagnosis = chain.invoke(symptoms)
    st.write(diagnosis.content)

with st.form("form"):
    symptoms = st.text_area(label="Enter symptoms: ")
    submitted = st.form_submit_button("Generate Diagnosis")
    if submitted:
        if symptoms == "":
            st.warning("Please enter your symptoms to generate a diagnosis!", icon="⚠")
        else:
            with st.spinner("Diagnosing symptoms"):
                diagnose(symptoms)