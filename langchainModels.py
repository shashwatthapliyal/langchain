from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

print("Enter")

model=ChatGoogleGenerativeAI(
     model="gemini-3-flash-preview",
     temperature=0.6
)

print("exit")
print(model)
result=model.invoke("write about india in 20 words")
print(result.content[0])2
