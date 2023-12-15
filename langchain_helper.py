from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import streamlit as st
import os
from secret_key import openapi_key

if openapi_key == "":
    print("NO API KEY FOUND... ADDING though Streamlit Secret")
    openapi_key = st.secrets["openapi_key"]
    print(openapi_key[:6])

os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_baby_names(lord_name):

    prompt_template_name = PromptTemplate(
        input_variables=['lord_name'],
        template="Please offer names inspired by Hindu God or Goddess {lord_name}, reflecting various characteristics and attributes associated with them. I'm looking for Indian names that hold religious and aesthetic significance in Hindu culture. Kindly provide 50-100 names in a comma-separated list."
    )
    p = prompt_template_name.format(lord_name=lord_name)
    print(p)

    chain = LLMChain(llm=llm, prompt=prompt_template_name)
    response = chain.run(lord_name)

    # response = "dharmik, ABC, XYZ, MNO"

    return response

if __name__ == "__main__":
    print(generate_baby_names("Italian"))
