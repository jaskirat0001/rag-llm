# import os #this library helps us in interacting with the operating systems in accessing and manipulating files
# from dotenv import load_dotenv #load_env is used to load the environmental variables
# from pathway.stdlib.ml.index import KNNIndex#it is used to finds the k nearest vectors to a query vector as measured by a similarity metric like product recommendations
# from common.openaiapi_helper import openai_embedder#used to add new tags to a file and it runs in an automanaged cloud stack.

# load_dotenv()

# embedding_dimension = int(os.environ.get("EMBEDDING_DIMENSION", 1536))


# def embeddings(context, data_to_embed):
#     return context + context.select(vector=openai_embedder(data_to_embed))


# def index_embeddings(embedded_data):
#     return KNNIndex(embedded_data.vector, embedded_data, n_dimensions=embedding_dimension)
import os
from dotenv import load_dotenv
from pathway.stdlib.ml.index import KNNIndex
from common.openaiapi_helper import openai_embedder

load_dotenv()

embedding_dimension = int(os.environ.get("EMBEDDING_DIMENSION", 1536))


def embeddings(context, flight_data):
    return context + context.select(vector=openai_embedder(flight_data))


def index_embeddings(embedded_data):
    return KNNIndex(embedded_data.vector, embedded_data, n_dimensions=embedding_dimension)
