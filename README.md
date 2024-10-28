# Neo4j Graph Manager

## Overview
The Neo4j Graph Manager is a Python application designed to create and manage graph structures in a Neo4j database using data extracted from textual information. It utilizes the Langchain library for document processing and Groq API for language model interactions.

## Features
- Load environment variables from a `.env` file for secure credential management.
- Create graph structures in Neo4j from text documents.
- Use LLM (Language Model) transformers to convert documents into graph formats.
- Execute Cypher queries to interact with the Neo4j database.

## Requirements
To run this project, ensure you have the following dependencies installed:

- Python 3.7 or higher
- `langchain_community`
- `langchain_groq`
- `langchain_core`
- `langchain_experimental`
- `python-dotenv`
- Neo4j database running (local or remote)

You can install the required packages using pip:


Create a .env file in the root directory of the project and add your Neo4j credentials and API keys:

NEO4J_URI="neo4j+s://your_neo4j_instance"
NEO4J_USERNAME="your_username"
NEO4J_PASSWORD="your_password"
GROQ_API_KEY="your_groq_api_key"
MODEL_NAME="your_model_name"

![Visualization](https://raw.githubusercontent.com/KAJURAMBO/Graph_database-create/main/visualisation.png)

