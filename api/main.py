import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path

app = FastAPI()

# Tắt mount StaticFiles vì không ổn định trên Vercel → dùng FileResponse thủ công
STATIC_DIR = Path("static")

@app.get("/", response_class=HTMLResponse)
async def index():
    index_path = STATIC_DIR / "index.html"
    if not index_path.exists():
        return HTMLResponse("<h1>index.html not found</h1>", status_code=404)
    return index_path.read_text(encoding="utf-8")

# Serve static files (css, js, images...) thủ công
@app.get("/static/{path:path}")
async def static_files(path: str):
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

# (Tùy chọn) Catch-all fallback cho các path khác (nếu cần)
@app.get("/{path:path}")
async def fallback(path: str):
    return HTMLResponse("<h1>404 - Not Found</h1>", status_code=404)
