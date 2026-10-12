from study_assistant import ask_gemini


# ==========================================
# ZERO-SHOT PROMPTING
# ==========================================

def zero_shot_prompt():

    print("\n--- ZERO-SHOT PROMPTING ---")

    prompt = """
    Explain linked lists in Python using simple language.
    Give one example.
    """

    print("\nPrompt:")
    print(prompt)

    answer = ask_gemini(prompt)

    print("\nAI Response:")
    print(answer)


# ==========================================
# FEW-SHOT PROMPTING
# ==========================================

def few_shot_prompt():

    print("\n--- FEW-SHOT PROMPTING ---")

    prompt = """
    Follow the format shown in these examples.

    Example 1:
    Question: What is Python?
    Answer: Python is a programming language.

    Example 2:
    Question: What is SQL?
    Answer: SQL is a database query language.

    Now answer this question in the same style.

    Question: What is Java?
    Answer:
    """

    print("\nPrompt:")
    print(prompt)

    answer = ask_gemini(prompt)

    print("\nAI Response:")
    print(answer)


# ==========================================
# ROLE PROMPTING
# ==========================================

def role_prompting():

    print("\n--- ROLE PROMPTING ---")

    prompt = """
    Explain recursion with a simple Python example.
    """

    role = """
    You are an experienced Python teacher.
    Teach beginners using simple words and practical examples.
    """

    print("\nRole: Python Teacher")
    print("Task: Explain recursion with an example.")

    answer = ask_gemini(prompt, role=role)

    print("\nAI Response:")
    print(answer)


# ==========================================
# PROMPT ENGINEERING MENU
# ==========================================

def main():

    while True:

        print("\n================================")
        print("       PROMPT ENGINEERING")
        print("================================")
        print("1. Zero-Shot Prompting")
        print("2. Few-Shot Prompting")
        print("3. Role Prompting")
        print("4. Run All Demonstrations")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            zero_shot_prompt()

        elif choice == "2":
            few_shot_prompt()

        elif choice == "3":
            role_prompting()

        elif choice == "4":
            zero_shot_prompt()
            few_shot_prompt()
            role_prompting()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()