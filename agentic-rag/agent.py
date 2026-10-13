
import ollama
from tools import search_documents, calculator

model = "qwen3:1.7b"

# Register the available tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_documents",
            "description": "Search the PDF document for relevant information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The question to search for in the document."
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to calculate."
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

print("Agent loaded successfully!")

# Ask the user a question
question = input("\nAsk the Agent: ")

# Let the model choose a tool
response = ollama.chat(
    model=model,
    messages=[
        {
            "role": "system",
            "content": (
                "You are an Agentic RAG assistant. "
                "For questions about the PDF, use search_documents. "
                "For mathematical calculations, use calculator. "
                "Use the appropriate tool before answering."
            )
        },
        {"role": "user", "content": question}
    ],
    tools=tools
)

# Execute the selected tool
tool_calls = response["message"].get("tool_calls", [])

if tool_calls:
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        arguments = tool_call.function.arguments

        print("\nTool selected:", tool_name)

        if tool_name == "search_documents":
            result = search_documents(arguments["query"])
        elif tool_name == "calculator":
            result = calculator(arguments["expression"])
        else:
            result = "Unknown tool."

        print("\nTool Result:")
        print(result)

        # Generate the final answer using the tool result
        final_response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Answer the user's question using the tool result. "
                        "For document questions, use only the retrieved information. "
                        "Explain clearly and simply."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Question: {question}\n"
                        f"Tool result: {result}"
                    )
                }
            ]
        )

        print("\nFinal Answer:")
        print(final_response["message"]["content"])
else:
    print("\nAnswer:")
    print(response["message"]["content"])
