import logging
import os

from crewai import LLM, Agent, Task, Crew
from dotenv import load_dotenv

load_dotenv()
logging.getLogger("crewai").setLevel(logging.ERROR)

llm = LLM(
    model="openrouter/qwen/qwen3.8-27b",
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1",
)

researcher = Agent(
    role="Researcher",
    goal="Answer the user's question accurately",
    backstory="A meticulous analyst who cites reliable sources.",
    verbose=False,
    llm=llm
)

answer = Task(
    description="Research and answer: {question}",
    expected_output="A concise, well-supported answer.",
    agent=researcher,
)

crew = Crew(agents=[researcher], tasks=[answer],verbose=False,tracing=False)
result = crew.kickoff(inputs={"question": "Why sky is blue ?"})

print("-------")
print(result)