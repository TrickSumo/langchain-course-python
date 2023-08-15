from langchain.llms import OpenAI
from langchain import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model_name="text-davinci-003",temperature=0.5)

input_data1 = input("Enter something:- \n")
input_data2 = input("Enter lang:- \n")

# prompt_template = PromptTemplate(template="What is full form of {data}",input_variables=["data"])
# query = prompt_template.format(data=input_data)

# prompt_template = PromptTemplate.from_template(template="What is full form of {data}")
# query = prompt_template.format(data=input_data)

prompt_template = PromptTemplate(template="Translate {sentence} to {lang}",input_variables=["sentence","lang"])
query = prompt_template.format(sentence=input_data1,lang=input_data2)

print(query)

res = llm(query)
print(res)
