class ReviewAgent:

    def summarize(self, documents):

        summaries = []

        for doc in documents:

            text = doc.page_content

            summary = text[:300] + "..."

            summaries.append(summary)

        return summaries


if __name__ == "__main__":

    class DummyDocument:
        def __init__(self, content):
            self.page_content = content

    docs = [
        DummyDocument(
            "Church Street Social is a fine dining restaurant in Galle Fort. "
            "It offers breakfast, lunch, and dinner in a refined atmosphere."
        )
    ]

    agent = ReviewAgent()

    summaries = agent.summarize(docs)

    for summary in summaries:
        print(summary)