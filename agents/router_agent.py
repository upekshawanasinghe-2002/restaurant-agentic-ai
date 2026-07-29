from agents.preference_agent import PreferenceAgent
from agents.restaurant_agent import RestaurantSearchAgent
from agents.review_agent import ReviewAgent
from agents.planner_agent import PlannerAgent


class RouterAgent:

    def __init__(self):

        self.preference_agent = PreferenceAgent()
        self.restaurant_agent = RestaurantSearchAgent()
        self.review_agent = ReviewAgent()
        self.planner_agent = PlannerAgent()


    def run(self, user_input):

        # 1. Extract preferences
        preferences = self.preference_agent.extract_preferences(user_input)

        print("\nExtracted Preferences:")
        print(preferences)


        # 2. Retrieve restaurants using RAG
        restaurants = self.restaurant_agent.search(preferences)


        # 3. Generate AI summaries
        summaries = self.review_agent.summarize(restaurants)


        # 4. Create dining plan
        final_plan = self.planner_agent.create_plan(
            preferences,
            summaries
        )


        return final_plan



if __name__ == "__main__":

    router = RouterAgent()


    user_input = input(
        "\nEnter your request: "
    )


    result = router.run(user_input)


    print("\n==============================")
    print("AI Restaurant Dining Plan")
    print("==============================\n")

    print(result)