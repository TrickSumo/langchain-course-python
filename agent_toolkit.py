from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

llm=OpenAI(model="text-davinci-003", temperature=0.3)
# llm = ChatOpenAI(model="gpt-3.5-turbo",temperature=0.3)


python_agent = create_python_agent(llm=llm,tool=PythonREPLTool(),verbose=True)

res = python_agent.run("In data.csv file, evaluate expresssion in first column and save it to second cloumn. Do this for all rows and save in new file as solved.csv")