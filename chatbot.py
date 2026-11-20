from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")


chat_history=[SystemMessage(content="You are a helpful assistant.")]
# print(chat_history)

while True:
    user_input=input('You: ')
    chat_history.append(HumanMessage(content=user_input))

    # print(chat_history)
    if(user_input=='exit') :
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage (result.content[0]["text"]))
    print("AI: ",result.content[0]["text"])

print(chat_history)