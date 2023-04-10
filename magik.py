#!/usr/bin/env python3
from typing import List

from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools import AIPluginTool
from dotenv import load_dotenv

# Load default environment variables (.env)
load_dotenv()

klarna_tool = AIPluginTool.from_plugin_url("https://www.klarna.com/.well-known/ai-plugin.json")

def decompose_tasks(task: str) -> bool
    prompt = f'Complete the following task: {task}. Context: {task}'
    prompt = (
        f'Write me a painfully detailed discretized list of tasks for the following objective:'
        f'Objective: {objective}'
        f'Tasks should be simple and self-contained enough that it only takes one action to complete. List the tool you would use next to the task. An example of an ultimately discretized task that takes one action to complete would be "Purchase a plane ticket using Kayak" because that requires one API call or action from a user. An an example of a task that is too generic, is one that would need to be broken down further, like "plan a birthday party" because that involves picking a date (a discretized task), inviting people via email (a discretized task), picking a theme etc.'
        f'Tools you have access to: WolframAlpha (useful for computation), General Human Knowledge (ask the user for things like dates, preferences), the internet (for answers to current events), OpenTable (for reserving and finding restaurants), Kayak (for planning and finding flights), LLM\'s as a tool (for natural language reasoning, generating text, code snippets, poems/"copy" and more), Shop - the web app (for purchasing goods like clothing, party supplies), Instacart (for purchasing food and drinks), Zapier (for sending emails, creating excel databases and more).'
    )
    llm = ChatOpenAI(temperature=0.5)
    tools = load_tools(["requests"])
    tools += [klarna_tool]

    agent_chain = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    agent_chain.run(prompt)
    # task_completed = "Task completed!" in response
    # if task_completed:
    #     print(f"Completed the following task: {task}")
    # else:
    #     print(f"Decomposing the following task further: {task}")

def complete_task(task: str):
    task_completed = ask_agent_to_complete_task(task)
    if task_completed:
        return
    else:
        subtasks = decompose_task(task)
        for task in subtasks:
            complete_task(task)


def decompose_task(task: str) -> List[str]:
    prompt = "Develop a task list"
    pass
