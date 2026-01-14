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
        
        # Force print + flush để đảm bảo xuất hiện
        print("==== NEW VISITOR START ====", flush=True)
        print(json.dumps(data, indent=2), flush=True)
        print("==== NEW VISITOR END ====", flush=True)
        import sys
        sys.stdout.flush()  # Double force
        
        return {"status": "ok"}
    except Exception as e:
        print(f"ERROR OCCURRED: {str(e)}", flush=True)
        sys.stdout.flush()
        import traceback
        traceback.print_exc(file=sys.stdout)  # In traceback đầy đủ nếu crash
        raise  # Để Vercel capture nếu có
