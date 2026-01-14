import json
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    return open("static/index.html", encoding="utf-8").read()

@app.post("/collect")
async def collect(request: Request):
    data = await request.json()

    print("==== NEW VISITOR ====")
    print(json.dumps(data, indent=2))
    print("=====================")

    return {"status": "ok"}
