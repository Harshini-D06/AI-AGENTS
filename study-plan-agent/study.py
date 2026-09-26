# ==========================================
# STUDY PLAN MANAGEMENT AGENT
# ==========================================

print("===== STUDY PLAN MANAGEMENT AGENT =====")

# ------------------------------------------
# USER INPUT
# ------------------------------------------

name = input("Enter your name: ")
days = int(input("How many days do you have to study? "))
hours = int(input("How many hours can you study per day? "))
chosen_subject = input("What subject do you want to study? ")


# ------------------------------------------
# SUBJECTS AND TOPICS
# ------------------------------------------

subjects = {

    "Python": [
        "Introduction to Python",
        "Variables and Data Types",
        "Conditional Statements",
        "Loops",
        "Functions",
        "Lists and Tuples",
        "Dictionaries and Sets",
        "Object-Oriented Programming",
        "Exception Handling"
    ],

    "DBMS": [
        "Introduction to DBMS",
        "ER Model",
        "Relational Model",
        "SQL",
        "Normalization",
        "Transactions",
        "Concurrency Control",
        "Indexing"
    ],

    "Operating Systems": [
        "Introduction to OS",
        "Process Management",
        "CPU Scheduling",
        "Deadlocks",
        "Memory Management",
        "Virtual Memory",
        "File Systems",
        "I/O Management"
    ],

    "Computer Networks": [
        "Introduction to Networks",
        "OSI Model",
        "TCP/IP Model",
        "IP Addressing",
        "Routing",
        "Transport Layer",
        "Network Security",
        "Network Protocols"
    ]
}


# ------------------------------------------
# PREVIOUS YEAR QUESTION PAPERS
# ------------------------------------------

previous_year_questions = {

    "Python": [
        "Python Previous Year Question Paper 2025",
        "Python Previous Year Question Paper 2024",
        "Python Previous Year Question Paper 2023"
    ],

    "DBMS": [
        "DBMS Previous Year Question Paper 2025",
        "DBMS Previous Year Question Paper 2024",
        "DBMS Previous Year Question Paper 2023"
    ],

    "Operating Systems": [
        "Operating Systems Previous Year Question Paper 2025",
        "Operating Systems Previous Year Question Paper 2024",
        "Operating Systems Previous Year Question Paper 2023"
    ],

    "Computer Networks": [
        "Computer Networks Previous Year Question Paper 2025",
        "Computer Networks Previous Year Question Paper 2024",
        "Computer Networks Previous Year Question Paper 2023"
    ]
}


# ------------------------------------------
# CHECK INPUT
# ------------------------------------------

if chosen_subject not in subjects:

    print("\nSorry, that subject is not available.")

elif days < 2:

    print("\nPlease enter at least 2 days.")

elif hours <= 0:

    print("\nPlease enter valid study hours.")

else:

    topics = subjects[chosen_subject]
    pyqs = previous_year_questions[chosen_subject]

    # --------------------------------------
    # LAST DAY = PYQs + FULL REVISION
    # --------------------------------------

    study_days = days - 1

    # 30 minutes for daily revision
    daily_revision_minutes = 30

    # Time available for topics
    topic_study_minutes = (hours * 60) - daily_revision_minutes

    # --------------------------------------
    # DISPLAY PLAN DETAILS
    # --------------------------------------

    print("\n====================================")
    print("       PERSONALIZED STUDY PLAN")
    print("====================================")

    print("Student:", name)
    print("Subject:", chosen_subject)
    print("Days Available:", days)
    print("Study Hours Per Day:", hours)

    print("\n====================================")
    print("           DAILY SCHEDULE")
    print("====================================")


    # --------------------------------------
    # TOPIC COUNTER
    # --------------------------------------

    topic_number = 0


    # --------------------------------------
    # CREATE DAILY PLAN
    # --------------------------------------

    for day in range(1, days + 1):

        print("\nDay", day)

        # Start every day at 6:00 PM
        current_minutes = 18 * 60


        # ==================================
        # DAYS 1 TO LAST-1
        # STUDY TOPICS + REVISION
        # ==================================

        if day <= study_days:

            # Find remaining topics
            remaining_topics = len(topics) - topic_number

            # Find remaining study days
            remaining_days = study_days - day + 1

            # Distribute topics evenly
            today_topics = (
                remaining_topics + remaining_days - 1
            ) // remaining_days


            # Time for each topic
            topic_minutes = topic_study_minutes // today_topics


            # --------------------------------
            # SCHEDULE TOPICS
            # --------------------------------

            for i in range(today_topics):

                if topic_number < len(topics):

                    start_hour = current_minutes // 60
                    start_minute = current_minutes % 60


                    end_minutes = current_minutes + topic_minutes

                    end_hour = end_minutes // 60
                    end_minute = end_minutes % 60


                    # Convert to AM / PM
                    start_period = (
                        "AM" if start_hour < 12 else "PM"
                    )

                    end_period = (
                        "AM" if end_hour < 12 else "PM"
                    )


                    display_start_hour = start_hour % 12

                    if display_start_hour == 0:
                        display_start_hour = 12


                    display_end_hour = end_hour % 12

                    if display_end_hour == 0:
                        display_end_hour = 12


                    print(
                        f"{display_start_hour:02d}:"
                        f"{start_minute:02d} "
                        f"{start_period} - "
                        f"{display_end_hour:02d}:"
                        f"{end_minute:02d} "
                        f"{end_period} | "
                        f"{topics[topic_number]}"
                    )


                    current_minutes = end_minutes

                    topic_number += 1


            # --------------------------------
            # DAILY REVISION
            # --------------------------------

            start_hour = current_minutes // 60
            start_minute = current_minutes % 60


            end_minutes = (
                current_minutes + daily_revision_minutes
            )

            end_hour = end_minutes // 60
            end_minute = end_minutes % 60


            start_period = (
                "AM" if start_hour < 12 else "PM"
            )

            end_period = (
                "AM" if end_hour < 12 else "PM"
            )


            display_start_hour = start_hour % 12

            if display_start_hour == 0:
                display_start_hour = 12


            display_end_hour = end_hour % 12

            if display_end_hour == 0:
                display_end_hour = 12


            print(
                f"{display_start_hour:02d}:"
                f"{start_minute:02d} "
                f"{start_period} - "
                f"{display_end_hour:02d}:"
                f"{end_minute:02d} "
                f"{end_period} | Revision"
            )


        # ==================================
        # LAST DAY
        # PYQs + FULL REVISION
        # ==================================

        else:

            # Total time for PYQs
            total_pyq_minutes = 180

            # Divide PYQ time equally
            pyq_minutes = (
                total_pyq_minutes // len(pyqs)
            )


            # --------------------------------
            # SCHEDULE EACH PYQ
            # --------------------------------

            for pyq in pyqs:

                start_hour = current_minutes // 60
                start_minute = current_minutes % 60


                end_minutes = (
                    current_minutes + pyq_minutes
                )

                end_hour = end_minutes // 60
                end_minute = end_minutes % 60


                start_period = (
                    "AM" if start_hour < 12 else "PM"
                )

                end_period = (
                    "AM" if end_hour < 12 else "PM"
                )


                display_start_hour = start_hour % 12

                if display_start_hour == 0:
                    display_start_hour = 12


                display_end_hour = end_hour % 12

                if display_end_hour == 0:
                    display_end_hour = 12


                print(
                    f"{display_start_hour:02d}:"
                    f"{start_minute:02d} "
                    f"{start_period} - "
                    f"{display_end_hour:02d}:"
                    f"{end_minute:02d} "
                    f"{end_period} | "
                    f"{pyq}"
                )


                current_minutes = end_minutes


            # --------------------------------
            # FULL REVISION
            # --------------------------------

            full_revision_minutes = (
                (hours * 60) - total_pyq_minutes
            )


            start_hour = current_minutes // 60
            start_minute = current_minutes % 60


            end_minutes = (
                current_minutes +
                full_revision_minutes
            )

            end_hour = end_minutes // 60
            end_minute = end_minutes % 60


            start_period = (
                "AM" if start_hour < 12 else "PM"
            )

            end_period = (
                "AM" if end_hour < 12 else "PM"
            )


            display_start_hour = start_hour % 12

            if display_start_hour == 0:
                display_start_hour = 12


            display_end_hour = end_hour % 12

            if display_end_hour == 0:
                display_end_hour = 12


            print(
                f"{display_start_hour:02d}:"
                f"{start_minute:02d} "
                f"{start_period} - "
                f"{display_end_hour:02d}:"
                f"{end_minute:02d} "
                f"{end_period} | "
                f"Full Revision - All Topics Studied"
            )


    # --------------------------------------
    # FINAL MESSAGE
    # --------------------------------------

    print("\n====================================")
    print("       STUDY PLAN COMPLETED")
    print("====================================")

    print("All topics, PYQs and revision are scheduled!")
    print("Good luck,", name, "!")