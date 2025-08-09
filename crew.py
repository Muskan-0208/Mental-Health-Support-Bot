from crewai import Crew, Process
from Agents import mood_analyzer, companion, self_care_bot
from tasks import task
import gradio as gr

mental_health_crew = Crew(
    agents=[companion, mood_analyzer, self_care_bot],
    tasks=[task],
    # tasks=[companion_task, mood_detection_task, self_care_task],
    process=Process.sequential,  # Tasks will run one after another
    verbose=True  # Show thought process of each agent
)

# Define a function that uses the Crew to process input
def mental_health_bot(user_input):
    result = mental_health_crew.kickoff(inputs={"input": user_input})
    return result

# Launch Gradio UI
interface = gr.Interface(
    fn=mental_health_bot,
    inputs=gr.Textbox(lines=4, placeholder="How are you feeling today?", label="Your Message"),
    outputs=gr.Textbox(label="Mental Health Bot Response"),
    title="🧠 Mental Health Support Bot",
    description="Talk to the bot to get emotional support and a self-care suggestion."
)

interface.launch()