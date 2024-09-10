import os

import torch
from llama_index.core.workflow import (
    Event,
    StartEvent,
    StopEvent,
    Workflow,
    step,
)

# `pip install llama-index-llms-openai` if you don't already have it
# from llama_index.llms.openai import OpenAI
from llama_index.llms.huggingface import HuggingFaceLLM
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_huggingface.llms.huggingface_pipeline import HuggingFacePipeline
from llama_index.llms.ollama import Ollama

from llama_index.utils.workflow import (
    draw_all_possible_flows,
    draw_most_recent_execution,
)


HUGGING_FACE_TOKEN = os.getenv('HF_TOKEN')


class JokeEvent(Event):
    joke: str


class JokeFlow(Workflow):

    llm = Ollama(model='llama2')

    @step
    async def generate_joke(self, ev: StartEvent) -> JokeEvent:
        topic = ev.topic

        prompt = f"Write a Python code to perform {topic}."
        response = await self.llm.acomplete(prompt)
        return JokeEvent(joke=str(response))

    @step
    async def critique_joke(self, ev: JokeEvent) -> StopEvent:
        joke = ev.joke

        prompt = f"Can you check the following code and give response in only code {joke}"
        response = await self.llm.acomplete(prompt)
        return StopEvent(result=str(response))


async def main():
    w = JokeFlow(timeout=60, verbose=False)
    result = await w.run(topic="create ec2 instances using boto3")
    print(str(result))


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
