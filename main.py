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
        
        # Print với flush=True để buộc gửi ngay từng dòng
        print("==== NEW VISITOR START ====", flush=True)
        
        # In JSON từng phần để tránh gộp/cắt
        json_str = json.dumps(data, indent=2)
        for line in json_str.splitlines():
            print(line, flush=True)
        
        print("==== NEW VISITOR END ====", flush=True)
        
        sys.stdout.flush()  # Double force
        
        return {"status": "ok"}
    except Exception as e:
        print(f"ERROR: {str(e)}", flush=True)
        sys.stdout.flush()
        import traceback
        traceback.print_exc(file=sys.stdout)
        raise
