from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from utils.analyze import analyze_image
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

eco_score_total = 0

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    global eco_score_total
    contents = await file.read()
    result = analyze_image(contents)
    eco_score_total += result["eco_score"]
    result["total_score"] = eco_score_total
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)