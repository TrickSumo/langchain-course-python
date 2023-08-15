from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage,HumanMessage,AIMessage

from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

messages = [SystemMessage(content="You are AWS certified solutions architect, help me to learn AWS"),
            HumanMessage(content="Hi, I want to know what is AWS"),
            AIMessage(content="""Hi there! AWS stands for Amazon Web Services. It is a cloud computing platform provided by Amazon. AWS offers a wide range of cloud services, including computing power, storage options, content delivery, databases, analytics, machine learning, and more. It allows individuals and organizations to build and deliver applications and services 
using the power of cloud computing. AWS provides a scalable and flexible infrastructure that enables businesses to quickly scale up or down based on their needs, pay only for 
the resources they use, and eliminate the need for upfront infrastructure investments."""),
HumanMessage(content="how many questions I asked?")
]

res = llm(messages)
print(res)




