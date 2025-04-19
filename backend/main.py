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

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    result = analyze_image(contents)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)