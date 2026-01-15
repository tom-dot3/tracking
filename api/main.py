import json
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# Mount static nếu cần (nên dùng public/ thay vì mount cho Vercel)
# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index.html", encoding="utf-8") as f:  # hoặc public/index.html
        return f.read()

# Catch-all cho mọi path khác (nếu cần serve từ FastAPI)
@app.get("/{path:path}", response_class=HTMLResponse)
@app.post("/{path:path}")
async def catch_all(path: str, request: Request = None):
    if request.method == "POST" and path == "collect":
        data = await request.json()
        print("==== NEW VISITOR ====")
        print(json.dumps(data, indent=2))
        print("=====================")
        return {"status": "ok"}
    # Hoặc fallback 404 nếu không match
    return HTMLResponse(content="<h1>404 Not Found</h1>", status_code=404)

# Hoặc giữ nguyên @app.post("/collect") riêng và dùng catch-all chỉ cho GET nếu cần
