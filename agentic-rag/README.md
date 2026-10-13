# Agentic RAG – Intelligent Document Retrieval Assistant

## Project Overview
Agentic RAG is an AI-powered document retrieval assistant that searches information from PDF documents and answers user questions. It uses an AI agent to select the appropriate tool for document searching or mathematical calculations.

## Features
- Extracts text from PDF documents.
- Splits documents into smaller text chunks.
- Generates embeddings using Sentence Transformers.
- Stores embeddings in ChromaDB for semantic search.
- Uses an AI agent to select and execute tools.
- Answers mathematical questions using a calculator tool.
- Generates responses using a local language model.

## Technologies Used
- Python
- Ollama
- Qwen3:1.7b
- Sentence Transformers
- ChromaDB
- PyPDF

## Project Structure
```text
agentic-rag/
├── agent.py
├── tools.py
├── create_database.py
├── requirements.txt
├── documents/
│   └── research_paper.pdf
└── chroma_db/
```

## Installation and Setup

1. Install Python and Ollama.
2. Download the language model:
   ```bash
   ollama pull qwen3:1.7b
   ```
3. Create and activate a virtual environment.
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Place your PDF file inside the `documents` folder.
6. Build the vector database:
   ```bash
   python create_database.py
   ```
7. Start the AI assistant:
   ```bash
   python agent.py
   ```

## Example Questions
- What is artificial intelligence?
- What are the main topics discussed in the research paper?
- What is 25 * 8?

## Expected Result
The agent selects an appropriate tool, retrieves document information or performs a calculation, and generates a response.

## Conclusion
This project demonstrates how Retrieval-Augmented Generation (RAG), vector databases, embeddings, and AI tool calling can be combined to build an intelligent document assistant.