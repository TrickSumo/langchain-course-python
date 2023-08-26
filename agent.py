from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import ChatOpenAI
from tools import job_description_processor, google_search
from langchain import PromptTemplate

tools = [
    Tool(
        name="job Description Parser",
        description="This tool take URL of Job description, loads html webpage and processes it",
        func=job_description_processor,
    ),
    Tool(
        name="web search",
        description="this tool is useful for doing google search",
        func=google_search,
    ),
]


def job_desc_agent(company, url):
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    agent = initialize_agent(
        llm=llm, tools=tools, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    prompt = PromptTemplate.from_template(
        "Find information about company {company} then summerize and enhance job description Job description url = {url}"
    )
    query = prompt.format(company=company, url=url)
    res = agent.run(query)
    return res
