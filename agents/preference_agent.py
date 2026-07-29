import re

class PreferenceAgent:

    def extract_preferences(self, user_input):

        preferences = {
            "food": None,
            "budget": None,
            "location": None
        }

        # Budget
        budget = re.search(r"\d+", user_input)
        if budget:
            preferences["budget"] = int(budget.group())

        # Food
        foods = [
            "seafood",
            "kottu",
            "rice",
            "hoppers",
            "lamprais",
            "vegetarian"
        ]

        for food in foods:
            if food.lower() in user_input.lower():
                preferences["food"] = food.title()

        # Location
        locations = [
            "Colombo",
            "Galle",
            "Kandy",
            "Ella",
            "Sigiriya",
            "Mirissa"
        ]

        for location in locations:
            if location.lower() in user_input.lower():
                preferences["location"] = location

        return preferences


if __name__ == "__main__":

    agent = PreferenceAgent()

    user_input = input("Enter your preferences: ")

    result = agent.extract_preferences(user_input)

    print("\nExtracted Preferences")
    print(result)