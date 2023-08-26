from langchain.document_loaders import AsyncChromiumLoader
from bs4 import BeautifulSoup
from langchain.llms import OpenAI
from langchain import PromptTemplate

from langchain.utilities import SerpAPIWrapper

from dotenv import load_dotenv

load_dotenv()


def job_description_processor(url):
    site_loader = AsyncChromiumLoader(urls=[url])
    data = site_loader.load()

    soup = BeautifulSoup(data[0].page_content, "html.parser")
    job_description = soup.find("div", class_="job-description-text")

    llm = OpenAI()
    prompt = PromptTemplate.from_template(
        "Summerize the job description and return comapny details and requirements . Job description {job_description}"
    )
    query = prompt.format(job_description=job_description)
    res = llm(query)

    return res


def google_search(query):
    search = SerpAPIWrapper()
    return search.run(query)
