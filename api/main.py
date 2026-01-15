import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

# Route cho trang chủ - đọc file từ public/
@app.get("/", response_class=HTMLResponse)
async def index():
    file_path = os.path.join("public", "index.html")  # hoặc "static/index.html" nếu bạn giữ tên static
    if not os.path.exists(file_path):
        return HTMLResponse(content="<h1>index.html not found in public/</h1>", status_code=404)
    
    with open(file_path, encoding="utf-8") as f:
        return f.read()

# (Tùy chọn) Nếu cần serve các file tĩnh khác (css, js, images...) thủ công
@app.get("/static/{path:path}")
async def static_files(path: str):
    file_path = os.path.join("public", path)  # hoặc "static", tùy bạn
    if not os.path.exists(file_path):
        return FileResponse(status_code=404)
    return FileResponse(file_path)

# Endpoint collect giữ nguyên
@app.post("/collect")
async def collect(request: Request):
    data = await request.json()

    print("==== NEW VISITOR ====")
    print(json.dumps(data, indent=2))
    print("=====================")

    return {"status": "ok"}
