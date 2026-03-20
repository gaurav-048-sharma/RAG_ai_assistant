import streamlit as st
import sys
import os

# Fix import
sys.path.append(os.path.abspath("src"))

from vectorstore import load_index
from retriever import retrieve
from generator import generate_answer

st.title("🧠 RAG AI Assistant")

# Load index
index, texts = load_index()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

query = st.chat_input("Ask something...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            results = retrieve(query, index, texts)
            context = "\n".join(results)
            answer = generate_answer(query, context)

            st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

# import streamlit as st
# import sys
# import os

# # Fix import path
# sys.path.append(os.path.abspath("src"))

# # Import modules (NO 'src.' here)
# from vectorstore import load_index
# from retriever import retrieve
# from generator import generate_answer

# st.set_page_config(page_title="RAG Chat Assistant", layout="wide")

# st.title("🧠 RAG AI Assistant")
# st.write("Chat with your documents using RAG")

# # Load FAISS index
# index, texts = load_index()

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display previous messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.write(msg["content"])

# # Chat input
# query = st.chat_input("Ask something...")

# if query:
#     # Store user message
#     st.session_state.messages.append({"role": "user", "content": query})

#     with st.chat_message("user"):
#         st.write(query)

#     # Generate response
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             results = retrieve(query, index, texts)
#             context = "\n".join(results)

#             answer = generate_answer(query, context)

#             st.write(answer)

#     # Store assistant response
#     st.session_state.messages.append({"role": "assistant", "content": answer})