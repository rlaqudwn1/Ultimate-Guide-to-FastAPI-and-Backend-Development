from fastapi import FastAPI, Path
from typing import Any

app = FastAPI()



@app.get("/users/{user_id}/items/{item_name}")
def test_param(
    user_id : int = Path(gt=0),
    item_name : str= "default") -> dict[str , Any] :
    return{
        "user_id": user_id,
        "item_name": item_name,
        "messeage": "성공"
    }