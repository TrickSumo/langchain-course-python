from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate

from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

message_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are a helpful assistant that re-writes the user's text to sound more upbeat."),
        HumanMessagePromptTemplate.from_template("{data}")
    ]
)

input_data = input("Enter Something \n")
query_message = message_prompt.format_messages(data=input_data)

res = llm(query_message)

print(res)

