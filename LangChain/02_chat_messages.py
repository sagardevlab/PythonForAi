from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from llm_setup import llm

# System + human message
msg = llm.invoke([
    SystemMessage(content = "You are a helpful AI bot that assists a user in choosing a perfect book to read, in one short sentences."),
    HumanMessage(content = "I enjoy mystery novels, what should I read?"),
])

print(msg.content)

# Pass an entire chat history, including previous AI turns
msg = llm.invoke([
    SystemMessage(content="You are a supportive AI bot that suggests fitness activities in one short sentence."),
    HumanMessage(content="I like high-intensity workouts, what should I do?"),
    AIMessage(content="You should try a CrossFit class."),
    HumanMessage(content="How often should I attend?"),
])
print(msg.content)

# System message is optional
print(llm.invoke([HumanMessage(content="What month follows June?")]).content)
