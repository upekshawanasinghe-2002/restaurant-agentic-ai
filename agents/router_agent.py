from preference_agent import PreferenceAgent
from restaurant_agent import RestaurantSearchAgent
from review_agent import ReviewAgent


class RouterAgent:

    def __init__(self):
        self.preference_agent = PreferenceAgent()
        self.restaurant_agent = RestaurantSearchAgent()
        self.review_agent = ReviewAgent()

    def run(self, user_input):

        # Step 1: Extract user preferences from natural language
        preferences = self.preference_agent.extract_preferences(user_input)

        print("\nExtracted Preferences:")
        print(preferences)

        # Check whether required preferences were found
        if not preferences["food"] or not preferences["location"]:
            print("\nCould not understand your request completely.")
            return []

        # Step 2: Search restaurants
        restaurants = self.restaurant_agent.search(preferences)

        # Step 3: Summarize search results
        summaries = self.review_agent.summarize(restaurants)

        return summaries


if __name__ == "__main__":

    router = RouterAgent()

    # Natural language input
    user_input = input("Enter your request: ")

    results = router.run(user_input)

    if results:
        print("\nRestaurant Recommendations\n")

        for i, result in enumerate(results, start=1):
            print("=" * 60)
            print(f"Recommendation {i}")
            print("=" * 60)
            print(result)
            print()