from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model_name="text-davinci-003",temperature=1)

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()

prompt_template = PromptTemplate(template="List five {object} \n {format_instructions}",
                                 input_variables=["object"],
                                 partial_variables={"format_instructions":format_instructions})
query = prompt_template.format(object="chocolate ice cream")

# print(query)

res = llm(query)
# print(res)

parsed_data = output_parser.parse(res)
print(parsed_data)