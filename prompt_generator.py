from langchain_core.prompts import PromptTemplate


template=PromptTemplate(
    input_variables=["paper_input","style_input","length_input"],
    template="""
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style:{style_input}
    Explanation Length:{length_input}
    """
)

template.save("template.json")