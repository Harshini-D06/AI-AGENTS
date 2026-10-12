from agent import TravelAgent


print("=" * 55)
print("        ✈️ MINI AUTONOMOUS TRAVEL AGENT")
print("=" * 55)

print("\nWelcome! 👋")
print("I'll help you plan your trip step by step.")


# ==========================================
# 1. DESTINATION
# ==========================================

print("\n" + "-" * 55)
print("1. 📍 DESTINATION")
print("-" * 55)

destination = input(
    "Where do you want to travel? "
)

print(
    f"\n✅ Destination selected: "
    f"{destination}"
)


# ==========================================
# 2. TRANSPORT MODE
# ==========================================

print("\n" + "-" * 55)
print("2. 🚆 TRANSPORT MODE")
print("-" * 55)

print(
    f"How would you like to travel to "
    f"{destination}?"
)

print("1. ✈️ Flight")
print("2. 🚌 Bus")
print("3. 🚆 Train")

transport_choice = input(
    "\nEnter your choice (1/2/3): "
)

if transport_choice == "1":

    transport = "Flight"

elif transport_choice == "2":

    transport = "Bus"

elif transport_choice == "3":

    transport = "Train"

else:

    print(
        "\n❌ Invalid choice. "
        "Please restart the program."
    )

    exit()

print(
    f"\n✅ {transport} selected."
)


# ==========================================
# 3. STARTING LOCATION
# ==========================================

print("\n" + "-" * 55)
print("3. 📍 STARTING LOCATION")
print("-" * 55)

starting_location = input(
    "Where are you travelling from? "
)

print(
    f"\n✅ Starting location: "
    f"{starting_location}"
)


# ==========================================
# 4. TRAVEL DATE
# ==========================================

print("\n" + "-" * 55)
print("4. 📅 TRAVEL DATE")
print("-" * 55)

travel_date = input(
    "When do you want to travel? "
    "(DD-MM-YYYY): "
)

print(
    f"\n✅ Travel date: "
    f"{travel_date}"
)


# ==========================================
# 5. NUMBER OF TRAVELERS
# ==========================================

print("\n" + "-" * 55)
print("5. 👥 TRAVELERS")
print("-" * 55)

travelers = input(
    "How many people are travelling? "
)

print(
    f"\n✅ Number of travelers: "
    f"{travelers}"
)


# ==========================================
# 6. BUDGET
# ==========================================

print("\n" + "-" * 55)
print("6. 💰 BUDGET")
print("-" * 55)

budget = input(
    "What is your total trip budget? ₹"
)

print(
    f"\n✅ Budget: ₹{budget}"
)


# ==========================================
# 7. HOTEL PREFERENCE
# ==========================================

print("\n" + "-" * 55)
print("7. 🏨 HOTEL PREFERENCE")
print("-" * 55)

print(
    "What type of accommodation do you prefer?"
)

print("1. 🏠 Budget")
print("2. 🏨 Standard")
print("3. ⭐ Luxury")

hotel_choice = input(
    "\nEnter your choice (1/2/3): "
)

if hotel_choice == "1":

    hotel_preference = "Budget"

elif hotel_choice == "2":

    hotel_preference = "Standard"

elif hotel_choice == "3":

    hotel_preference = "Luxury"

else:

    print(
        "\n❌ Invalid choice. "
        "Please restart."
    )

    exit()

print(
    f"\n✅ {hotel_preference} "
    f"accommodation selected."
)


# ==========================================
# 8. INTERESTS
# ==========================================

print("\n" + "-" * 55)
print("8. ❤️ INTERESTS")
print("-" * 55)

print(
    "What would you like to explore?"
)

print("1. 🏖️ Beaches")
print("2. 🏛️ Historical Places")
print("3. 🍴 Food")
print("4. 🌳 Nature")
print("5. 🎯 Everything")

interest_choice = input(
    "\nEnter your choice (1/2/3/4/5): "
)

if interest_choice == "1":

    interest = "Beaches"

elif interest_choice == "2":

    interest = "Historical Places"

elif interest_choice == "3":

    interest = "Food"

elif interest_choice == "4":

    interest = "Nature"

elif interest_choice == "5":

    interest = "Everything"

else:

    print(
        "\n❌ Invalid choice. "
        "Please restart."
    )

    exit()

print(
    f"\n✅ Interest selected: "
    f"{interest}"
)


# ==========================================
# CREATE TRAVEL AGENT
# ==========================================

agent = TravelAgent(
    destination=destination,
    transport=transport,
    starting_location=starting_location,
    travel_date=travel_date,
    travelers=travelers,
    budget=budget,
    hotel_preference=hotel_preference,
    interest=interest
)


# ==========================================
# RUN AGENT
# ==========================================

success = agent.run()


# ==========================================
# CHECK AGENT RESULT
# ==========================================

if not success:

    print(
        "\n❌ Unable to create "
        "a travel plan."
    )

    exit()


# ==========================================
# HUMAN APPROVAL
# ==========================================

print("\n" + "=" * 55)
print("          👤 HUMAN APPROVAL REQUIRED")
print("=" * 55)

print(
    "\nThe AI agent has created "
    "the travel plan above."
)

print(
    "\n⚠️ No booking or payment will "
    "happen without your approval."
)

approval = input(
    "\nDo you approve this travel plan? "
    "(yes/no): "
).strip().lower()


# ==========================================
# APPROVAL RESULT
# ==========================================

if approval == "yes":

    print("\n" + "=" * 55)
    print("          ✅ TRIP APPROVED")
    print("=" * 55)

    print(
        "\n🎉 Your travel plan has been approved!"
    )

    print(
        "The agent can now proceed to "
        "the next step."
    )

    print(
        "\n⚠️ Note: This demo does not "
        "perform real bookings or payments."
    )

elif approval == "no":

    print("\n" + "=" * 55)
    print("          ❌ TRIP NOT APPROVED")
    print("=" * 55)

    print(
        "\nThe agent will not proceed "
        "with booking or payment."
    )

else:

    print("\n⚠️ Invalid approval response.")

    print(
        "No booking or payment will be performed."
    )