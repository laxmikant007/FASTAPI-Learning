from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Laxmikant!! How are you ???? "}



@app.get("/about")
def about():
    return {"data" : {"page" : "About page is here !!!!"}}


@app.get("/contact")
def contact():
    return {"data" : {"page" : "Contact page is here !!!!"}}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
