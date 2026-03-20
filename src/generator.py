import requests

def generate_answer(query, context):
    prompt = f"""
You are an AI assistant.

Use ONLY the context below to answer.
Give a clear and structured answer.

Answer the question ONLY using the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query}

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]

# import requests

# def generate_answer(query, context):
#     prompt = f"""
#     Answer the question based only on the context below.

#     Context:
#     {context}

#     Question:
#     {query}
#     """

#     response = requests.post(
#         "http://localhost:11434/api/generate",
#         json={
#             "model": "llama3",
#             "prompt": prompt,
#             "stream": False
#         }
#     )

#     return response.json()["response"]
