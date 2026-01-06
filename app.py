def load_policy(file_path):
    with open(file_path, "r") as file:
        return file.read()

def ask_question(policy_text, question):
    prompt = f"""
You are an insurance policy assistant.
Explain policy terms in simple language.
Avoid legal advice.
If the answer is not present, say so clearly.

Policy Document:
{policy_text}

Question:
{question}
"""
    return prompt  # Placeholder for LLM response

if __name__ == "__main__":
    policy = load_policy("sample_policy.txt")
    question = input("Enter your question: ")
    response = ask_question(policy, question)
    print("LLM Response:")
    print(response)
