import os
from dotenv import load_dotenv

from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

from langchain.vectorstores import Pinecone
import pinecone


load_dotenv()
pinecone.init(
    api_key=os.environ.get("PINECONE_API_KEY"),
    environment=os.environ.get("PINECONE_REGION")
)

def rag(query, chat_history):

    embedding = OpenAIEmbeddings(model="text-embedding-ada-002")
    vector_store = Pinecone.from_existing_index(index_name="chatpdf", embedding=embedding)

    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})
    # res = retriever.get_relevant_documents("qantum mechanics")

    chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5, verbose=True)

    # chain = RetrievalQA.from_chain_type(llm=chat_model, chain_type="stuff", retriever=retriever, verbose = True)
    chain = ConversationalRetrievalChain.from_llm(llm=chat_model, retriever=retriever, verbose=True)

    # res = chain({"query":query})
    res = chain({"question":query, "chat_history":chat_history})
    
    return res

