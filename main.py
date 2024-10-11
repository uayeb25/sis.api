import json
import uvicorn
from typing import Union

from fastapi import FastAPI, HTTPException

from utils.database import fetch_query_as_json

app = FastAPI()


@app.get("/")
async def read_root():
    query = "select * from e10.hello"
    try:
        result = await fetch_query_as_json(query)
        result_dict = json.loads(result)
        return { "data": result_dict, "version": "0.0.3" }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)