import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path

app = FastAPI()

STATIC_DIR = Path("static")  # Đảm bảo folder static được commit & bundle

@app.get("/", response_class=HTMLResponse)
async def index():
    index_path = STATIC_DIR / "index.html"
    if not index_path.exists():
        return HTMLResponse(content="<h1>index.html not found in static/</h1>", status_code=404)
    return index_path.read_text(encoding="utf-8")

@app.get("/static/{path:path}")
async def serve_static(path: str):
    file_path = STATIC_DIR / path
    if not file_path.exists() or not file_path.is_file():
        return FileResponse(status_code=404)
    return FileResponse(file_path)

@app.post("/collect")
async def collect(request: Request):
    data = await request.json()

    print("==== NEW VISITOR ====")
    print(json.dumps(data, indent=2))
    print("=====================")

    return {"status": "ok"}
