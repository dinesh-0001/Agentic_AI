import streamlit as st
import os
from crewai_tools import PDFSearchTool
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from crewai import Agent, Task, Crew
from crewai_tools import tool

# Set your API keys
os.environ["GROQ_API_KEY"] = "GROQ_API_KEY"
os.environ["TAVILY_API_KEY"] = "TAVILY_API_KEY"

# Initialize LLM
llm = ChatOpenAI(
    openai_api_base="https://api.groq.com/openai/v1",
    openai_api_key=os.environ['GROQ_API_KEY'],
    model_name="llama3-8b-8192",
    temperature=0.1,
    max_tokens=1000,
)

# Streamlit UI
st.title("Ask Your PDF - Powered by CrewAI Agents")

uploaded_pdf = st.file_uploader("Upload a PDF", type=["pdf"])
user_question = st.text_input("Ask your question here:")

if uploaded_pdf and user_question:
    # Save PDF
    pdf_path = "uploaded_temp.pdf"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_pdf.read())

    # Setup Tools
    rag_tool = PDFSearchTool(
        pdf=pdf_path,
        config=dict(
            llm=dict(
                provider="groq",
                config=dict(model="llama3-8b-8192"),
            ),
            embedder=dict(
                provider="huggingface",
                config=dict(model="BAAI/bge-small-en-v1.5"),
            ),
        )
    )

    web_tool = TavilySearchResults(k=3)

    # Define routing tool
    @tool
    def router_tool(question):
        """Router Function"""
        if 'self-attention' in question.lower() or 'transformer' in question.lower():
            return 'vectorstore'
        else:
            return 'web_search'

    # Agents
    router = Agent(
        role='Router',
        goal='Decide the best tool (PDF or web) to answer user questions',
        backstory='An expert system designed to decide whether a question is best answered via uploaded documents or the web.',
        verbose=True,
        allow_delegation=False,
        tools=[router_tool],
        llm=llm
    )

    researcher = Agent(
        role='Researcher',
        goal='Research and gather relevant information',
        backstory='An AI expert in finding relevant content from either PDFs or the internet.',
        verbose=True,
        allow_delegation=False,
        tools=[rag_tool, web_tool],
        llm=llm
    )

    analyst = Agent(
        role='Analyst',
        goal='Summarize and explain the information to the user',
        backstory='An expert in turning raw information into simple and helpful summaries.',
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

    # Tasks
    routing_task = Task(
        description=f"Decide whether the question '{user_question}' should be answered using the PDF or a web search.",
        expected_output="Return either 'vectorstore' or 'web_search'.",
        agent=router
    )

    research_task = Task(
        description=f"Based on the route selected, search for the answer to the question: '{user_question}' using the appropriate tool.",
        expected_output="A detailed response to the user's question using the selected source.",
        agent=researcher
    )

    analysis_task = Task(
        description="Summarize the research results in a clear, concise answer suitable for the user.",
        expected_output="Final summary answer to the user's question.",
        agent=analyst
    )

    # Define Crew
    crew = Crew(
        agents=[router, researcher, analyst],
        tasks=[routing_task, research_task, analysis_task],
        verbose=True
    )

    # Run Crew
    with st.spinner("Agents are working on your question..."):
        result = crew.kickoff()

    st.subheader("Final Answer:")
    st.write(result)

elif uploaded_pdf:
    st.info("Please enter a question.")
elif user_question:
    st.info("Please upload a PDF file.")
else:
    st.info("Upload a PDF and enter a question to get started.")
