
import os
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# 1. Initialize the LLM
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


# 2. Create tools

@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    try:
    
        # For demonstration only.
        # Use a safe expression parser in production.
        import ast
        import operator

        operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
        }

        def evaluate(node):
            if isinstance(node, ast.Constant) and type(node.value) in (int, float):
                return node.value

            if isinstance(node, ast.BinOp) and type(node.op) in operators:
                return operators[type(node.op)](
                    evaluate(node.left),
                    evaluate(node.right)
                )

            if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
                return -evaluate(node.operand)

            raise ValueError("Invalid mathematical expression")

        return str(evaluate(ast.parse(expression, mode="eval").body))

    except Exception as e:
        return f"Calculation error: {e}"


@tool
def get_weather(city: str) -> str:
    """Get weather information for a city."""

    # Replace this with a real weather API.
    return f"Weather information for {city} is currently unavailable."


@tool
def get_current_date() -> str:
    """Get the current date and time."""

    from datetime import datetime

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


@tool
def search_information(query: str) -> str:
    """Search for information about a topic."""

    # Replace this with a real search API.
    return f"Search results for: {query}"


# 3. Create the agent

agent = create_agent(
    model=model,
    tools=[
        calculator,
        get_weather,
        get_current_date,
        search_information
    ],
    system_prompt="""
    You are a helpful AI assistant.

    You can use tools to perform tasks.

    Instructions:
    - Use calculator for mathematical calculations.
    - Use get_weather for weather queries.
    - Use get_current_date for date and time queries.
    - Use search_information for information searches.
    - Do not invent tool results.
    - Explain your answers clearly.
    """
)


# 4. Run the agent

while True:

    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    response = agent.invoke({
        "messages": [
            {"role": "user", "content": user_input}
        ]
    })

    print("\nAI:", response["messages"][-1].content)
