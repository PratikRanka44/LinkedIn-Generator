from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv(override=True)

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="openai/gpt-oss-120b"
)