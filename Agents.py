import os
from crewai import Agent,LLM
from dotenv import load_dotenv
load_dotenv()

# Load Gemini API key from environment variable
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini 2.5 Pro model with deterministic behavior
gemini_llm = LLM(
    model='gemini/gemini-2.5-pro',
    api_key=gemini_api_key,
    temperature=0.0
)

# Mood Analyzer: 
mood_analyzer = Agent(
    role='Mood Analyzer',
    goal="Understand and classify the user's emotional state from a message into one of: Sad, Anxious, Angry, Happy, Neutral.",
    backstory="You are an expert at emotional intelligence and NLP. You specialize in detecting emotional states based on text.",
    allow_delegation=False,
    llm=gemini_llm
)


# ✅ Companion: Delegates to both support agents and combines the response
companion = Agent(
    role='Companion',
    goal="""
    Use the Mood Analyzer to determine the user's emotional state.
    Based on the emotion, craft an empathetic response to the user.
    Then, ask the Self-Care Recommender for a mental wellness activity suitable to that mood,
    and append it at the end of your response as a helpful suggestion.
    Combine both into a single, coherent message.
    """,
    backstory="""
    You are a kind and emotionally intelligent virtual companion.
    You respond with warmth, care, and understanding.
    Your job is to emotionally support the user and gently recommend a self-care activity.
    """,
    allow_delegation=True,
    llm=gemini_llm
)


# Self-Care Recommender: 
self_care_bot = Agent(
    role='Self-Care Recommender',
    goal="Suggest simple self-care activities based on a given mood such as journaling, deep breathing, nature walk, or screen breaks.",
    backstory="You are a wellness coach who understands how to improve someone's mental well-being through simple daily actions.",
    allow_delegation=False,
    llm=gemini_llm
)

