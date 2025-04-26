# File: backend/orchestrator.py

import logging
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from agents.research_agent import ResearchAgent
from agents.drafter_agent import DraftingAgent

# --- Logging setup ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Define the shape of our graph state ---
class OrchestratorState(TypedDict, total=False):
    query: str
    search_output: str
    answer: str

def make_graph() -> StateGraph:
    """
    Build a LangGraph StateGraph that flows:
      START → ResearchNode → DraftNode → END
    """
    # Instantiate with our state schema
    graph = StateGraph(OrchestratorState)

    # Research node
    def research_node(state: OrchestratorState) -> dict:
        q = state["query"]
        logger.info(f"[ResearchNode] querying: {q!r}")
        output = ResearchAgent().run(q)
        return {"search_output": output}

    # Draft node
    def draft_node(state: OrchestratorState) -> dict:
        so = state["search_output"]
        logger.info(f"[DraftNode] drafting answer…")
        ans = DraftingAgent().draft(so)
        return {"answer": ans}

    graph.add_node("ResearchNode", research_node)
    graph.add_node("DraftNode",    draft_node)

    # Wire execution
    graph.add_edge(START,         "ResearchNode")
    graph.add_edge("ResearchNode","DraftNode")
    graph.add_edge("DraftNode",    END)

    return graph

def run(query: str) -> str:
    """
    Entry point: invoke the graph with {'query': query} and return final 'answer'.
    """
    graph = make_graph().compile()
    try:
        final_state = graph.invoke({"query": query})
        return final_state["answer"]
    except Exception as e:
        logger.error(f"Orchestrator failure: {e}")
        raise

if __name__ == "__main__":
    # Example usage
    query = "What are the latest advancements in AI?"
    try:
        answer = run(query)
        print(f"Final answer:\n{answer}")
    except Exception as e:
        print(f"Error: {e}")