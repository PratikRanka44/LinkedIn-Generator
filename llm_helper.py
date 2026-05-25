from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(api_key = os.getenv("GROQ_API_KEY"), model_name ="openai/gpt-oss-120b")

response = llm.invoke("What is the capital of France?")
print("\n" + response.content + "\n")