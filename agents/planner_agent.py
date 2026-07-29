class PlannerAgent:

    def create_plan(self, preferences, summaries):

        plan = []

        plan.append("========== DINING PLAN ==========")
        plan.append(f"Location : {preferences['location']}")
        plan.append(f"Cuisine  : {preferences['food']}")
        plan.append(f"Budget   : LKR {preferences['budget']}")
        plan.append("")

        for i, summary in enumerate(summaries, start=1):
            plan.append(f"Stop {i}")
            plan.append(summary)
            plan.append("-" * 50)

        return "\n".join(plan)


if __name__ == "__main__":

    planner = PlannerAgent()

    preferences = {
        "food": "Seafood",
        "budget": 6000,
        "location": "Galle"
    }

    summaries = [
        "Church Street Social - Fine dining restaurant.",
        "Pedlar's Inn Café - Breakfast, Lunch & Dinner.",
        "Hoppa Galle Fort - Famous Sri Lankan Hoppers."
    ]

    print(planner.create_plan(preferences, summaries))