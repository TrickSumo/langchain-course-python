from langchain.llms import OpenAI

from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model_name="text-davinci-003",temperature=0.5)

res = llm("What is full form of AWS EC2")

print(res)


