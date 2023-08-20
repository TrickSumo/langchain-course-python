from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser

from dotenv import load_dotenv
load_dotenv()

output_parser = CommaSeparatedListOutputParser()

prompt_template = PromptTemplate(template="Give me list of 5 icrecreams of flavour {data} \n {format_instruction}",
                                 input_variables=["data"],
                                 partial_variables={"format_instruction":output_parser.get_format_instructions()}
                                 )

chatmodel = ChatOpenAI(model="gpt-3.5-turbo", temperature=1)

chain = LLMChain(llm=chatmodel, prompt=prompt_template, output_parser=output_parser)

res=  chain.run({"data":"strawberry"})
print(res)