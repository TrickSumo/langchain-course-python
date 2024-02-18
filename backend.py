from langchain_openai import OpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv

load_dotenv()


def domain_name_generator(niche):
    llm = OpenAI()

    output_parser = CommaSeparatedListOutputParser()
    format_instruction = output_parser.get_format_instructions()

    prompt_template = PromptTemplate(
        template="""You are SEO expert having 10 years of experience. 
                                    Suggest me 3 SEO optimized .com domain names for my blog in niche {niche} \n {format_instruction}""",
        input_variables=["niche"],
        partial_variables={"format_instruction": format_instruction},
    )

    query = prompt_template.format(niche=niche)

    res = output_parser.parse(llm(query))
    print(res)

    return res
