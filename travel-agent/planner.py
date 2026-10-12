# ==============================
# TRAVEL AGENT PLANNER
# ==============================

class TravelPlanner:

    def __init__(self):
        self.steps = []

    def create_plan(self):
        """Create the travel planning sequence."""

        self.steps = [
            "Understand travel goal",
            "Search transportation",
            "Evaluate transportation options",
            "Search hotels",
            "Check weather",
            "Find places to visit",
            "Calculate total cost",
            "Generate final itinerary",
            "Request human approval"
        ]

        return self.steps

    def show_plan(self):
        """Display the current plan."""

        print("\n📋 AGENT PLAN")
        print("-" * 45)

        for number, step in enumerate(
            self.steps,
            start=1
        ):
            print(f"{number}. {step}")