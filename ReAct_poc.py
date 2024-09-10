from llama_index.core.tools import FunctionTool
from llama_index.llms.ollama import Ollama
from llama_index.core.agent import ReActAgent, AgentRunner


def multiply(a: int, b: int, **kwargs) -> int:
    """
    Multiple two integers and returns the result integer
    :arg a: int
    :arg b: int

    """
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)

llm = Ollama(model='llama3.1')

agent = ReActAgent.from_tools([multiply_tool], llm=llm, verbose=True)
# agent = AgentRunner.from_llm([multiply_tool], llm=llm, verbose=True)


if __name__ == '__main__':
    agent.chat("What is 5 * 6")

