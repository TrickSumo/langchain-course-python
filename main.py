from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, field_validator

from typing import List

from dotenv import load_dotenv
load_dotenv()

# {"domain":[1,2,3],"title":[1,2,3]}

class Domain(BaseModel):
    domain_name:List = Field(description="suggested domain name for my blog")
    site_title :List = Field(description="site title of my blog")

    @field_validator("domain_name")
    def domain_name_tld(cls,feild):
        for domain in feild:
            if domain.split(".")[-1] != "com":
                raise ValueError("TLD is not .com")
        return feild


output_parser = PydanticOutputParser(pydantic_object=Domain)

format_instruction = output_parser.get_format_instructions()

prompt_template = PromptTemplate(template="Suggest me three unique .com domain names and creative site title for each domain in niche {niche} \n {format_instruction}",
                                 input_variables=["niche"],
                                 partial_variables={"format_instruction":format_instruction})

query = prompt_template.format(niche="Quantum computing")

llm = OpenAI(model_name="text-davinci-003", temperature=1)

res = llm(query)
res = output_parser.parse(res)

print(res.model_dump_json())