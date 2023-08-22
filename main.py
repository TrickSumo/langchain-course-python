from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType

from langchain.utilities import SerpAPIWrapper

from tool import is_prime

from dotenv import load_dotenv
load_dotenv()

prompt_template = PromptTemplate.from_template("{num} is not a prime number, right? If number is prime number search for new rebranded name of twitter by Elon Musk")
chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

serp = SerpAPIWrapper()

agent_tools = [
    Tool.from_function(name="prime number checker",
                       func=is_prime,
                       description="this tool helps to figure out if nuymber is prime or not."),
    Tool.from_function(name="seaerp API google search",
                       func=serp.run,
                       description="tool to do google search engine search")
]

agent = initialize_agent(tools=agent_tools, llm=chat_model,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose=True )

res = agent.run(prompt_template.format_prompt(num=4972450073))
print(res)
