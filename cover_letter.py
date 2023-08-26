from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.document_loaders import PyPDFLoader
from agent import job_desc_agent

import os
from dotenv import load_dotenv
load_dotenv()

def cover_letter_generator(company,url):

    llm = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo", verbose=True)

    current_dir = os.path.dirname(__file__)
    pdf_path = os.path.join(current_dir,"myData.pdf")
    pdf_loader = PyPDFLoader(file_path=pdf_path)
    resume  = pdf_loader.load()

    job_description = job_desc_agent(company,url)

    prompt_template = PromptTemplate(template="""For given resume and job description, create cover letter to join comapny
                                     \n resume = {resume}
                                     \n {job_description}
                                     
                                     \n Give output in well formatted html tags like <div> <br>""",
                                     input_variables=["resume","job_description"])
    chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)

    res = chain.run({"resume":resume, "job_description":job_description})
    print(res)
    return res




