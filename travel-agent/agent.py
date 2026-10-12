from tools import (
    search_trains,
    search_flights,
    search_buses,
    search_hotels,
    check_weather,
    find_places
)


class TravelAgent:

    def __init__(
        self,
        destination,
        transport,
        starting_location,
        travel_date,
        travelers,
        budget,
        hotel_preference,
        interest
    ):
        self.destination = destination
        self.transport = transport
        self.starting_location = starting_location
        self.travel_date = travel_date
        self.travelers = int(travelers)
        self.budget = float(budget)
        self.hotel_preference = hotel_preference
        self.interest = interest

        self.transport_options = []
        self.selected_transport = None
        self.selected_hotel = None
        self.weather = None
        self.places = []

    # --------------------------------
    # SEARCH TRANSPORT
    # --------------------------------

    def search_transport(self):

        print("\n🔎 Searching transportation...")

        if self.transport == "Train":

            self.transport_options = search_trains(
                self.starting_location,
                self.destination,
                self.travel_date
            )

        elif self.transport == "Flight":

            self.transport_options = search_flights(
                self.starting_location,
                self.destination,
                self.travel_date
            )

        elif self.transport == "Bus":

            self.transport_options = search_buses(
                self.starting_location,
                self.destination,
                self.travel_date
            )

        print("✅ Transportation search completed.")

    # --------------------------------
    # SELECT TRANSPORT
    # --------------------------------

    def select_transport(self):

        print("\n🧠 Agent is evaluating transportation options...")

        available = [
            option
            for option in self.transport_options
            if option["status"] == "Available"
        ]

        if not available:

            print("❌ No transportation available.")

            return False

        self.selected_transport = min(
            available,
            key=lambda option: option["price"]
        )

        print(
            f"✅ Selected: "
            f"{self.selected_transport['name']} "
            f"₹{self.selected_transport['price']}"
        )

        return True

    # --------------------------------
    # SEARCH HOTEL
    # --------------------------------

    def search_hotel(self):

        print("\n🏨 Searching hotels...")

        hotels = search_hotels(
            self.destination,
            self.hotel_preference
        )

        if hotels:

            self.selected_hotel = hotels[0]

            print(
                f"✅ Hotel found: "
                f"{self.selected_hotel['name']}"
            )

        else:

            print("❌ No matching hotel found.")

    # --------------------------------
    # WEATHER
    # --------------------------------

    def get_weather(self):

        print("\n🌤️ Checking weather...")

        self.weather = check_weather(
            self.destination
        )

        print(
            f"✅ Weather: "
            f"{self.weather['temperature']}, "
            f"{self.weather['condition']}"
        )

    # --------------------------------
    # PLACES
    # --------------------------------

    def get_places(self):

        print("\n🏖️ Finding places to visit...")

        self.places = find_places(
            self.destination,
            self.interest
        )

        print("✅ Places found.")

    # --------------------------------
    # RE-PLANNING
    # --------------------------------

    def replan(self):

        print("\n🔄 RE-PLANNING")
        print("-" * 55)

        available = [
            option
            for option in self.transport_options
            if option["status"] == "Available"
        ]

        if available:

            self.selected_transport = min(
                available,
                key=lambda option: option["price"]
            )

            print(
                "✅ Alternative transportation selected:"
            )

            print(
                f"{self.selected_transport['name']} "
                f"- ₹{self.selected_transport['price']}"
            )

            return True

        print(
            "❌ No alternative transportation found."
        )

        return False

    # --------------------------------
    # CALCULATE COST
    # --------------------------------

    def calculate_cost(self):

        transport_cost = (
            self.selected_transport["price"]
            * self.travelers
        )

        hotel_cost = (
            self.selected_hotel["price_per_night"]
            * self.travelers
        )

        total_cost = (
            transport_cost
            + hotel_cost
        )

        return (
            transport_cost,
            hotel_cost,
            total_cost
        )

    # --------------------------------
    # SHOW FINAL ITINERARY
    # --------------------------------

    def show_itinerary(self):

        transport_cost, hotel_cost, total_cost = (
            self.calculate_cost()
        )

        print("\n" + "=" * 55)
        print("          ✈️ FINAL TRAVEL ITINERARY")
        print("=" * 55)

        print(
            f"\n📍 Destination: "
            f"{self.destination}"
        )

        print(
            f"📍 Starting From: "
            f"{self.starting_location}"
        )

        print(
            f"📅 Travel Date: "
            f"{self.travel_date}"
        )

        print(
            f"👥 Travelers: "
            f"{self.travelers}"
        )

        # TRANSPORT

        print("\n🚆 TRANSPORT")

        print(
            f"   {self.selected_transport['name']}"
        )

        print(
            f"   Departure: "
            f"{self.selected_transport['departure']}"
        )

        print(
            f"   Arrival: "
            f"{self.selected_transport['arrival']}"
        )

        print(
            f"   Cost: ₹{transport_cost}"
        )

        # HOTEL

        print("\n🏨 HOTEL")

        print(
            f"   {self.selected_hotel['name']}"
        )

        print(
            f"   Rating: "
            f"{self.selected_hotel['rating']}"
        )

        print(
            f"   Cost: ₹{hotel_cost}"
        )

        # WEATHER

        print("\n🌤️ WEATHER")

        print(
            f"   {self.weather['temperature']}, "
            f"{self.weather['condition']}"
        )

        # PLACES

        print("\n📸 PLACES TO VISIT")

        for place in self.places:

            print(
                f"   • {place}"
            )

        # COST

        print("\n" + "-" * 55)

        print(
            f"💰 TOTAL ESTIMATED COST: "
            f"₹{total_cost}"
        )

        print(
            f"💰 YOUR BUDGET: "
            f"₹{self.budget}"
        )

        if total_cost <= self.budget:

            print(
                "✅ Trip is within your budget."
            )

        else:

            print(
                "⚠️ Trip exceeds your budget."
            )

        print("-" * 55)

    # --------------------------------
    # RUN AGENT
    # --------------------------------

    def run(self):

        print("\n" + "=" * 55)
        print("          🧠 AI AGENT STARTING")
        print("=" * 55)

        print("\n🎯 Goal:")

        print(
            f"Plan a trip from "
            f"{self.starting_location} "
            f"to {self.destination}"
        )

        print(
            f"👥 Travelers: "
            f"{self.travelers}"
        )

        print(
            f"💰 Budget: "
            f"₹{self.budget}"
        )

        print(
            f"🚆 Transport: "
            f"{self.transport}"
        )

        # STEP 1: SEARCH TRANSPORT

        self.search_transport()

        # STEP 2: SELECT TRANSPORT

        success = self.select_transport()

        # STEP 3: REPLAN IF NEEDED

        if not success:

            print(
                "\n❌ Initial transportation failed."
            )

            if not self.replan():

                return False

        # STEP 4: SEARCH HOTEL

        self.search_hotel()

        if not self.selected_hotel:

            print(
                "\n❌ Unable to find hotel."
            )

            return False

        # STEP 5: WEATHER

        self.get_weather()

        # STEP 6: PLACES

        self.get_places()

        # STEP 7: OBSERVATION

        print(
            "\n👀 Agent has observed all results."
        )

        # STEP 8: FINAL ITINERARY

        self.show_itinerary()

        return True