from  main import app


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
