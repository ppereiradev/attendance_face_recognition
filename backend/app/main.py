import uvicorn

from typing import Union
from fastapi import FastAPI, File, UploadFile
from deepface import DeepFace
import json

app = FastAPI()


@app.get("/")
def read_root():
    verification = DeepFace.verify(img1_path = "img1.jpeg", img2_path = "img2.jpeg")
    verification['verified'] = "true" if verification['verified'] else "false"
    return verification


@app.post("/uploadfile")
def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
