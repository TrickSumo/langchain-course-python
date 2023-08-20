# from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser

from dotenv import load_dotenv
load_dotenv()

output_parser = CommaSeparatedListOutputParser()

prompt_template = PromptTemplate.from_template("Give me list of 5 icrecreams of flavour {data} \n {format_instruction}")

# llm = OpenAI(model_name="text-davinci-003", temperature=1)
chatmodel = ChatOpenAI(model="gpt-3.5-turbo", temperature=1)

chain = LLMChain(llm=chatmodel, prompt=prompt_template, output_parser=output_parser)

res=  chain.run({"data":"strawberry","format_instruction":output_parser.get_format_instructions()})
# res = chain.run("strawberry")
# res = chain.run(data="strawberry")
print(res)