# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from langchain.embeddings import HuggingFaceInstructEmbeddings

embedding_model = HuggingFaceInstructEmbeddings(
    model_name="hkunlp/instructor-large",
    model_kwargs={"device": "cpu"}
)

print("Embedding model loaded successfully!")
