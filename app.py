from dotenv import load_dotenv
load_dotenv()

import streamlit as st

st.title("My First Streamlit App")

st.write("Welcome to my application!")


st.title("AI Research Paper Summarizer")

paper_input = st.selectbox(
    "Select a research paper",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Deep Residual Learning for Image Recognition",
        "ImageNet Classification with Deep Convolutional Neural Networks"
    ]
)

style_input = st.selectbox(
    "Select summary style",
    [
        "Simple Explanation",
        "Technical",
        "Bullet Points",
        "Executive Summary",
        "Beginner Friendly"
    ]
)

length_input = st.slider(
    "Select summary length (sentences)",
    1, 50, 5
)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

model=ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)
template=PromptTemplate(
    input_variables=["paper_input","style_input","length_input"],
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style:{style_input}
    Explanation Length:{length_input}
    """
)

print(template)

if st.button("Summarize"):
    prompt=template.invoke({
    "paper_input":paper_input,
    "style_input":style_input,
    "length_input":length_input
})
    print(prompt)

    with st.spinner("Generating summary..."):
        result = model.invoke(prompt)

  
    st.write(result.content[0]["text"])