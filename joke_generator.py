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

HUGGING_FACE_TOKEN = os.getenv('HF_TOKEN')


class JokeEvent(Event):
    joke: str


class JokeFlow(Workflow):
    # llm = HuggingFaceLLM(model_name='meta-llama/Meta-Llama-3.1-8B',
    #                      tokenizer_name='meta-llama/Meta-Llama-3.1-8B', device_map='auto')
    # model = AutoModelForCausalLM.from_pretrained(pretrained_model_name_or_path='StabilityAI/stablelm-tuned-alpha-3b', torch_dtype=torch.float16).to('mps')
    # tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path='StabilityAI/stablelm-tuned-alpha-3b').to('mps')
    # hf_pipeline = pipeline(task='text-generation', model=model, tokenizer=tokenizer, torch_dtype=torch.float16,
    #                        device='mps')
    # llm = HuggingFacePipeline(pipeline=hf_pipeline)
    llm = Ollama(model='llama2')

    @step
    async def generate_joke(self, ev: StartEvent) -> JokeEvent:
        topic = ev.topic

        prompt = f"Write your best joke about {topic}."
        response = await self.llm.acomplete(prompt)
        return JokeEvent(joke=str(response))

    @step
    async def critique_joke(self, ev: JokeEvent) -> StopEvent:
        joke = ev.joke

        prompt = f"Give a thorough analysis and critique of the following joke: {joke}"
        response = await self.llm.acomplete(prompt)
        return StopEvent(result=str(response))


async def main():
    w = JokeFlow(timeout=60, verbose=False)
    result = await w.run(topic="pirates")
    print(str(result))


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
