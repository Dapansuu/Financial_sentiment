from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import requests
import uvicorn

app = FastAPI(title="Sentiment API")

# CORS must be added before requests from browser will work properly
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

TF_SERVING_URL = "http://localhost:8502/v1/models/sentiment:predict"

IDX_TO_LABEL = {
    0: "neutral",
    1: "positive",
    2: "negative"
}

class PredictRequest(BaseModel):
    text: Optional[str] = None
    texts: Optional[List[str]] = None

@app.get("/")
def root():
    return {"message": "Sentiment backend is running"}

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.post("/predict")
def predict(request: PredictRequest):
    input_texts = []

    if request.text and request.text.strip():
        input_texts = [request.text.strip()]
    elif request.texts:
        input_texts = [t.strip() for t in request.texts if isinstance(t, str) and t.strip()]

    if not input_texts:
        raise HTTPException(status_code=400, detail="Provide either 'text' or 'texts'")

    try:
        payload = {
            "instances": [[text] for text in input_texts]
        }

        response = requests.post(TF_SERVING_URL, json=payload, timeout=20)

        if response.status_code != 200:
            fallback_payload = {
                "instances": input_texts
            }
            response = requests.post(TF_SERVING_URL, json=fallback_payload, timeout=20)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"TF Serving error: {response.text}")

        data = response.json()

        if "predictions" not in data:
            raise HTTPException(status_code=500, detail=f"Unexpected TF Serving response: {data}")

        results = []

        for text, pred in zip(input_texts, data["predictions"]):
            if isinstance(pred, list) and len(pred) > 1:
                pred_idx = max(range(len(pred)), key=lambda i: pred[i])
                results.append({
                    "text": text,
                    "label": IDX_TO_LABEL.get(pred_idx, str(pred_idx)),
                    "confidence": float(pred[pred_idx]),
                    "scores": [float(x) for x in pred]
                })
            else:
                score = pred[0] if isinstance(pred, list) else pred
                score = float(score)
                label = "positive" if score >= 0.5 else "negative"
                confidence = score if score >= 0.5 else 1.0 - score

                results.append({
                    "text": text,
                    "label": label,
                    "confidence": confidence,
                    "score": score
                })

        return {"predictions": results}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Connection error: {str(e)}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)