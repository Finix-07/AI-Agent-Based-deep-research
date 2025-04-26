from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from worker_main import run  # your orchestrator entrypoint

# Request schema
class QueryRequest(BaseModel):
    query: str

# App initv
app = FastAPI(title="Deep Research Agent API")

# Allow your frontend origin (adjust port if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

@app.post("/query")
async def query_agent(req: QueryRequest):
    """
    Accepts {"query": "..."} and returns {"answer": "..."}.
    """
    try:
        answer = run(req.query)
        return {"answer": answer}
    except Exception as e:
        # Log error (optional)
        raise HTTPException(status_code=500, detail=str(e))
