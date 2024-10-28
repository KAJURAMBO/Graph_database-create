import os
from dotenv import load_dotenv
from langchain_community.graphs import Neo4jGraph
from langchain_groq import ChatGroq
from langchain_core.documents import Document
from langchain_experimental.graph_transformers import LLMGraphTransformer


# Load environment variables from .env file
load_dotenv()


class Neo4jGraphManager:
    def __init__(self):
        # Get credentials from environment variables
        self.neo4j_uri = os.getenv("NEO4J_URI")
        self.username = os.getenv("NEO4J_USERNAME")
        self.password = os.getenv("NEO4J_PASSWORD")
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.model_name = os.getenv("MODEL_NAME")

        # Initialize Neo4j graph
        self.graph = Neo4jGraph(
            url=self.neo4j_uri,
            username=self.username,
            password=self.password,
        )

        # Initialize LLM for processing
        self.llm = ChatGroq(groq_api_key=self.groq_api_key, model_name=self.model_name)

    def create_documents(self, text):
        documents = [Document(page_content=text)]
        return documents

    def transform_documents_to_graph(self, documents):
        llm_transformer = LLMGraphTransformer(llm=self.llm)
        graph_documents = llm_transformer.convert_to_graph_documents(documents)
        return graph_documents

    def execute_cypher_query(self, cypher_query):
        self.graph.query(cypher_query)

    def construct_cypher_query(self, graph_documents):
        cypher_query = """
        MERGE (elon:Person {id: 'Elon Reeve Musk'})
        MERGE (maye:Person {id: 'Maye'})
        MERGE (errol:Person {id: 'Errol Musk'})
        MERGE (kimbal:Person {id: 'Kimbal Musk'})
        MERGE (spacex:Organization {id: 'Spacex'})
        MERGE (tesla:Organization {id: 'Tesla, Inc.'})
        MERGE (x_corp:Organization {id: 'X Corp.'})
        MERGE (boring_company:Organization {id: 'The Boring Company'})
        MERGE (xai:Organization {id: 'Xai'})
        MERGE (neuralink:Organization {id: 'Neuralink'})
        MERGE (openai:Organization {id: 'Openai'})
        MERGE (university_of_pretoria:Educational_institution {id: 'University Of Pretoria'})
        MERGE (queens_university:Educational_institution {id: "Queen'S University At Kingston"})
        MERGE (university_of_pennsylvania:Educational_institution {id: 'University Of Pennsylvania'})
        MERGE (stanford_university:Educational_institution {id: 'Stanford University'})
        MERGE (zip2:Organization {id: 'Zip2'})

        MERGE (elon)-[:PARENT]->(maye)
        MERGE (elon)-[:PARENT]->(errol)
        MERGE (elon)-[:SIBLING]->(kimbal)
        MERGE (elon)-[:FOUNDED]->(spacex)
        MERGE (elon)-[:FOUNDED]->(tesla)
        MERGE (elon)-[:OWNER]->(x_corp)
        MERGE (elon)-[:FOUNDED]->(boring_company)
        MERGE (elon)-[:FOUNDED]->(xai)
        MERGE (elon)-[:FOUNDED]->(neuralink)
        MERGE (elon)-[:FOUNDED]->(openai)
        MERGE (elon)-[:ATTENDED]->(university_of_pretoria)
        MERGE (elon)-[:ATTENDED]->(queens_university)
        MERGE (elon)-[:ATTENDED]->(university_of_pennsylvania)
        MERGE (elon)-[:ATTENDED]->(stanford_university)
        MERGE (elon)-[:CO_FOUNDER]->(zip2)
        """  # Add more nodes and relationships here
        return cypher_query


def main():
    # Initialize the graph manager
    graph_manager = Neo4jGraphManager()

    # Sample text for document creation
    text = """
    Elon Reeve Musk (born June 28, 1971) is a businessman and investor known for his key roles in space
    company SpaceX and automotive company Tesla, Inc. Other involvements include ownership of X Corp.,
    formerly Twitter, and his role in the founding of The Boring Company, xAI, Neuralink, and OpenAI.
    He is one of the wealthiest people in the world; as of July 2024, Forbes estimates his net worth to be
    US$221 billion. Musk was born in Pretoria to Maye and engineer Errol Musk, and briefly attended
    the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through
    his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada.
    Musk later transferred to the University of Pennsylvania and received bachelor's degrees in economics
    and physics. He moved to California in 1995 to attend Stanford University, but dropped out after
    two days and, with his brother Kimbal, co-founded online city guide software company Zip2.
    """

    # Create documents
    documents = graph_manager.create_documents(text)

    # Transform documents to graph format
    graph_documents = graph_manager.transform_documents_to_graph(documents)

    # Construct Cypher query
    cypher_query = graph_manager.construct_cypher_query(graph_documents)

    # Execute query
    graph_manager.execute_cypher_query(cypher_query)


if __name__ == "__main__":
    main()
