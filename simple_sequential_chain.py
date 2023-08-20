from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

chatmodel = ChatOpenAI(model="gpt-3.5-turbo", temperature=1)

prompt1 = PromptTemplate(template="Suggest 2 important interview topics for job profile {job_profile}. Give topic only, no extra description",
                         input_variables=["job_profile"]
                         )
chain1 = LLMChain(llm=chatmodel,prompt=prompt1, verbose=True)


prompt2 = PromptTemplate(template="Suggest 3 job interview questions for topics {topics}",
                         input_variables=["topics"]
                         )
chain2 = LLMChain(llm=chatmodel,prompt=prompt2, verbose=True)


prompt3 = PromptTemplate(template="For given questions, give me short answers {questions}",
                         input_variables=["questions"]
                         )
chain3 = LLMChain(llm=chatmodel,prompt=prompt3, verbose=True)

overall_chain = SimpleSequentialChain(chains=[chain1,chain2,chain3])

res = overall_chain.run("REACT developer")
print(res)

