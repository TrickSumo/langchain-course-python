from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

chatmodel = ChatOpenAI(model="gpt-3.5-turbo", temperature=1)

prompt1 = PromptTemplate(template="Suggest 2 important {difficulty} interview topics for job profile {job_profile}. Give topic only, no extra description",
                         input_variables=["difficulty","job_profile"]
                         )
chain1 = LLMChain(llm=chatmodel,prompt=prompt1, verbose=True, output_key="topics")

prompt2 = PromptTemplate(template="for given topics, give me 3 question for each topic {topics}. output should be comma seperated list",
                        input_variables=["topics"])
chain2 = LLMChain(llm=chatmodel,prompt=prompt2, verbose=True,output_key="questions")

prompt3 = PromptTemplate(template="For given questions {questions}, provide short answers.",
                        input_variables=["questions"])
chain3 = LLMChain(llm=chatmodel,prompt=prompt3, verbose=True,output_key="answers")


overall_chain = SequentialChain(chains=[chain1,chain2,chain3],
                                input_variables=["difficulty","job_profile"],
                                output_variables=["topics","questions","answers"],
                                verbose=True
                                )

res = overall_chain({"difficulty":"medium", "job_profile":"devops engineer"})
print(res)