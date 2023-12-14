from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import streamlit as st
import os
from secret_key import openapi_key

if openapi_key == None:
    openapi_key = st.secrets["openapi_key"]

os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_baby_names(lord_name):

    prompt_template_name = PromptTemplate(
        input_variables=['lord_name'],
        template="I want to name a baby which inspired with a character of lord {lord_name} . Suggest some similar indian aesthetic and religious names for this in a comma seperatded."
    )
    p = prompt_template_name.format(lord_name=lord_name)
    print(p)

    chain = LLMChain(llm=llm, prompt=prompt_template_name)
    response = chain.run(lord_name)

    # response = "dharmik, ABC, XYZ, MNO"

    return response

if __name__ == "__main__":
    print(generate_baby_names("Italian"))
