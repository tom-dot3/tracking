import sys
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
    try:
        data = await request.json()
        print("==== NEW VISITOR START ====", flush=True)
        print(json.dumps(data, indent=2), flush=True)
        print("==== NEW VISITOR END ====", flush=True)
        sys.stdout.flush()  # Force gửi log ngay lập tức
        return {"status": "ok"}
    except Exception as e:
        print(f"ERROR in /collect: {str(e)}", flush=True)
        sys.stdout.flush()
        raise  # Để Vercel capture traceback nếu crash
