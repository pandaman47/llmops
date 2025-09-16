from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from agent.agentic_workflow import GraphBuilder
from utils.save_to_document import save_to_document
from starlette.responses import JSONResponse
import os
import datetime
from dotenv import load_dotenv
from pydantic import BaseModel
load_dotenv()

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_travel_agent(query:QueryRequest):
    try:
        print(query.query)
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        print(f"Graph build is saved as 'my_graph.png' in {os.getcwd()}")

        messages = {"messages": [query.query]}
        print(messages)
        output = react_app.invoke(messages)

        ## Result is dict with messages
        if isinstance(output,dict) and "messages" in output:
            print(output["messages"][-1].content)
            final_output = output["messages"][-1].content
        else:
            print("output is not a dict")
            final_output = str(output)

        print("returning answer final_output")    
        return {"answer": final_output}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})