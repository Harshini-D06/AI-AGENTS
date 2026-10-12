# ==============================
# TRAVEL AGENT TOOLS
# ==============================

def search_trains(source, destination, date):
    """Search available trains."""

    trains = [
        {
            "name": f"{destination} Express",
            "departure": "07:30 AM",
            "arrival": "06:00 PM",
            "price": 1200,
            "status": "Available"
        },
        {
            "name": "Superfast Express",
            "departure": "09:00 AM",
            "arrival": "07:30 PM",
            "price": 1400,
            "status": "Available"
        },
        {
            "name": "Night Express",
            "departure": "10:30 PM",
            "arrival": "08:30 AM",
            "price": 1300,
            "status": "Available"
        }
    ]

    return trains


def search_flights(source, destination, date):
    """Search available flights."""

    flights = [
        {
            "name": "Air India",
            "departure": "08:00 AM",
            "arrival": "09:15 AM",
            "price": 3500,
            "status": "Available"
        },
        {
            "name": "IndiGo",
            "departure": "11:30 AM",
            "arrival": "12:45 PM",
            "price": 3800,
            "status": "Available"
        }
    ]

    return flights


def search_buses(source, destination, date):
    """Search available buses."""

    buses = [
        {
            "name": f"{destination} Sleeper",
            "departure": "08:00 PM",
            "arrival": "07:00 AM",
            "price": 900,
            "status": "Available"
        },
        {
            "name": "VRL Travels",
            "departure": "09:30 PM",
            "arrival": "08:00 AM",
            "price": 1100,
            "status": "Available"
        }
    ]

    return buses


def search_hotels(destination, preference):
    """Search hotels based on destination and preference."""

    hotels = [
        {
            "name": f"{destination} Budget Stay",
            "price_per_night": 1800,
            "rating": 4.1,
            "type": "Budget"
        },
        {
            "name": f"{destination} Comfort Hotel",
            "price_per_night": 2500,
            "rating": 4.4,
            "type": "Standard"
        },
        {
            "name": f"{destination} Luxury Resort",
            "price_per_night": 6000,
            "rating": 4.8,
            "type": "Luxury"
        }
    ]

    return [
        hotel
        for hotel in hotels
        if hotel["type"].lower() == preference.lower()
    ]


def check_weather(destination):
    """Check weather conditions."""

    return {
        "temperature": "28°C",
        "condition": "Sunny",
        "rain_probability": "20%"
    }


def find_places(destination, interest):
    """Find places based on destination and interest."""

    places = [
        f"Popular {interest} spot in {destination}",
        f"Famous tourist attraction in {destination}",
        f"Local sightseeing area in {destination}"
    ]

    return places