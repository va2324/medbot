import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

st.title("MedBot")
api_key = st.sidebar.text_input("OpenAI API Key", type="password")
valid = False
if api_key.startswith("sk-"):
    st.sidebar.text("API Key Verified")
    valid = True
elif len(api_key) > 0 and not api_key.startswith("sk-"):
    st.sidebar.text("Invalid API Key")

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
        if not valid:
            st.warning("Please enter your OpenAI API key!", icon="⚠")
        if symptoms == "":
            st.warning("Please enter your symptoms to generate a diagnosis!", icon="⚠")
        if valid and symptoms != "":
            with st.spinner("Diagnosing symptoms"):
                diagnose(symptoms)