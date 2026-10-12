import os
from google import genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Check your .env file."
    )

# Connect to Gemini
client = genai.Client(api_key=API_KEY)

MODEL = "gemini-3.8-flash"


# ==========================================
# GEMINI AI RESPONSE FUNCTION
# ==========================================

def ask_gemini(prompt, role=None):

    try:
        config = {}

        if role:
            config["system_instruction"] = role

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config=config if config else None
        )

        return response.text or "No response generated."

    except Exception as error:
        return (
            f"Unable to get an AI response: {error}\n"
            "Check your internet connection, API key, "
            "model availability, and usage limits."
        )


# ==========================================
# AI STUDY ASSISTANT
# ==========================================

def study_assistant():

    print("\n--- AI STUDY ASSISTANT ---")
    print("Ask any study-related question.")
    print("Type 'back' to return to the menu.")

    while True:

        question = input("\nYou: ").strip()

        if question.lower() == "back":
            break

        prompt = f"""
        Answer the student's question clearly.

        Explain difficult concepts in simple language.
        Include examples wherever useful.
        Use headings or bullet points when appropriate.

        Student's question: {question}
        """

        answer = ask_gemini(
            prompt,
            role="You are a friendly and helpful study tutor."
        )

        print("\nAI Assistant:", answer)


# ==========================================
# INTELLIGENT FAQ ASSISTANT
# ==========================================

def faq_assistant():

    print("\n--- INTELLIGENT FAQ ASSISTANT ---")
    print("Ask a question about computer science.")
    print("Type 'back' to return to the menu.")

    faq_data = """
    Python: A programming language.
    SQL: A language for managing relational databases.
    Database: An organized collection of data.
    Artificial Intelligence: Technology that enables
    machines to perform tasks requiring human intelligence.
    Linked List: A data structure consisting of connected nodes.
    """

    while True:

        question = input("\nYour question: ").strip()

        if question.lower() == "back":
            break

        prompt = f"""
        Answer the user's question using the FAQ information
        below whenever it is relevant.

        FAQ INFORMATION:
        {faq_data}

        If the answer is not covered in the FAQ, explain that
        the information is not in the FAQ, then provide a
        brief general explanation if you can.

        User question: {question}
        """

        answer = ask_gemini(
            prompt,
            role="You are an intelligent FAQ assistant for students."
        )

        print("\nFAQ Assistant:", answer)


# ==========================================
# AI QUIZ GENERATOR
# ==========================================

def quiz_generator():

    print("\n--- AI QUIZ GENERATOR ---")

    subject = input("Enter the subject: ").strip()

    if not subject:
        print("Please enter a subject.")
        return

    prompt = f"""
    Create 5 multiple-choice questions about {subject}.

    For every question:
    1. Give four options.
    2. Identify the correct answer.
    3. Briefly explain why it is correct.

    Present the questions clearly for a student.
    Put the answer key after all five questions.
    """

    answer = ask_gemini(
        prompt,
        role="You are a teacher who creates educational quizzes."
    )

    print("\nGenerated Quiz:\n")
    print(answer)


# ==========================================
# AI STUDY PLAN GENERATOR
# ==========================================

def study_plan_generator():

    print("\n--- AI STUDY PLAN GENERATOR ---")

    subject = input("Enter the subject: ").strip()

    if not subject:
        print("Please enter a subject.")
        return

    try:
        days = int(input("Enter the number of days: "))

        if days <= 0:
            print("Enter a positive number of days.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    prompt = f"""
    Create a practical {days}-day study plan for {subject}.

    Include:
    1. Topics to study each day.
    2. Practice exercises.
    3. Revision time.
    4. A final revision and self-assessment.

    Keep the plan suitable for a student.
    """

    answer = ask_gemini(
        prompt,
        role="You are an experienced academic study planner."
    )

    print("\nYour Personalized Study Plan:\n")
    print(answer)


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n====================================")
        print("       GEMINI STUDY ASSISTANT")
        print("====================================")
        print("1. AI Study Assistant")
        print("2. Intelligent FAQ Assistant")
        print("3. AI Quiz Generator")
        print("4. AI Study Plan Generator")
        print("5. Prompt Engineering")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            study_assistant()

        elif choice == "2":
            faq_assistant()

        elif choice == "3":
            quiz_generator()

        elif choice == "4":
            study_plan_generator()

        elif choice == "5":
            from prompt_engineering import main as prompt_main
            prompt_main()

        elif choice == "6":
            print("Goodbye! Keep learning!")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 6.")


if __name__ == "__main__":
    main()