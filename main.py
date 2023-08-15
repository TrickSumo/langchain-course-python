from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate
# from langchain.schema import SystemMessage,HumanMessage,AIMessage

from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

input_data = input("Enter something \n ")

prompt_message = ChatPromptTemplate.from_messages(
    [
    SystemMessage(content="You are a helpful assistant that re-writes the user's text to sound more upbeat."),
    HumanMessagePromptTemplate.from_template("{data}"),
]
)
query_message = prompt_message.format_messages(data = input_data)

res = llm(query_message)

print(res)

# llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
# messages = [SystemMessage(content="You are AWS certified solutions architect, help me to learn AWS"),
#             HumanMessage(content="Hi, what is AWS?")
# ]

# res = llm(messages)
# print(res)














