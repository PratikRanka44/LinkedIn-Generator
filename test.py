from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv(override=True)

key = os.getenv("GROQ_API_KEY")

print("KEY FOUND:", key is not None)
print("KEY PREFIX:", key[:8] if key else None)
print("KEY LENGTH:", len(key) if key else 0)

llm = ChatGroq(
    api_key=key,
    model_name="llama-3.3-70b-versatile"
)

print(llm.invoke("Hello").content)