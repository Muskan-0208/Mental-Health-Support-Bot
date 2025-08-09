from crewai import Task
from Agents import mood_analyzer, companion, self_care_bot

task = Task(
    description="Provide emotional support and a self-care suggestion based on the user's message.",
    expected_output="An empathetic response followed by a relevant self-care recommendation.",
    agent=companion
)

# Task 1: Empathetic Response
companion_task = Task(
    description=(
        "Using the mood detected by the Mood Analyzer, write a supportive and empathetic message "
        "to comfort the user, based on the user's message. Your response should be kind, friendly, and encouraging."
        "Use self-care recommender to recommend an activity"
    ),
    expected_output=(
        "Donot tell the mood. A short paragraph showing emotional support. Make the user feel heard, understood, and not alone.Followed by a relevant self-care recommendation."
    ),
    agent=companion
)

# Task 2: Mood Detection
mood_detection_task = Task(
    description=(
        "Read the user's message and classify their emotional state into one of the following moods: "
        "Sad, Anxious, Angry, Happy, or Neutral. Use your knowledge of emotional cues in language."
    ),
    expected_output=(
        "One of the following mood labels only: Sad, Anxious, Angry, Happy, Neutral."
    ),
    agent=mood_analyzer
)

# Task 3: Self-Care Suggestion
self_care_task = Task(
    description=(
        "Based on the detected mood, recommend a simple and effective self-care activity "
        "the user can do right now to improve their emotional well-being. Suggestions can include meditation, "
        "walking, journaling, breathing exercises, or digital detox."
    ),
    expected_output=(
        "One self-care tip or activity with 1-2 lines explaining why it helps in the current mood."
    ),
    agent=self_care_bot
)
