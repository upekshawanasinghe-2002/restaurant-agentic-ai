from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


class RestaurantSearchAgent:

    def __init__(self):

        self.embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vector_store = Chroma(
            persist_directory="chroma_db",
            embedding_function=self.embedding
        )

        self.retriever = self.vector_store.as_retriever(
            search_kwargs={"k":5}
        )

    def search(self, preferences):

        query = f"""
        Recommend restaurants for
        Food: {preferences['food']}
        Budget: {preferences['budget']}
        Location: {preferences['location']}
        """

        results = self.retriever.invoke(query)

        return results

if __name__ == "__main__":

        agent = RestaurantSearchAgent()

        preferences = {
         "food": "Seafood",
         "budget": 6000,
         "location": "Galle"
    }

        results = agent.search(preferences)

        print(results)