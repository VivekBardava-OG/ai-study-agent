import streamlit as st

st.set_page_config(page_title="AI Study Agent")

st.title("🤖 AI Study Assistant Agent")

question = st.text_input("Ask me anything:")

if question:
    st.write("You asked:")
    st.success(question)
    st.write("✅ Agent is working properly!")
