import pickle
from pathlib import Path
from typing import Literal
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# ---------- Schemas ----------
class Customer(BaseModel):
    gender: Literal["male", "female"]
    seniorcitizen: Literal[0, 1]
    partner: Literal["yes", "no"]
    dependents: Literal["yes", "no"]
    phoneservice: Literal["yes", "no"]
    multiplelines: Literal["no", "yes", "no_phone_service"]
    internetservice: Literal["dsl", "fiber_optic", "no"]
    onlinesecurity: Literal["no", "yes", "no_internet_service"]
    onlinebackup: Literal["no", "yes", "no_internet_service"]
    deviceprotection: Literal["no", "yes", "no_internet_service"]
    techsupport: Literal["no", "yes", "no_internet_service"]
    streamingtv: Literal["no", "yes", "no_internet_service"]
    streamingmovies: Literal["no", "yes", "no_internet_service"]
    contract: Literal["month-to-month", "one_year", "two_year"]
    paperlessbilling: Literal["yes", "no"]
    paymentmethod: Literal[
        "electronic_check",
        "mailed_check",
        "bank_transfer_(automatic)",
        "credit_card_(automatic)",
    ]
    tenure: int = Field(..., ge=0)
    monthlycharges: float = Field(..., ge=0.0)
    totalcharges: float = Field(..., ge=0.0)

class PredictResponse(BaseModel):
    churn_probability: float
    will_churn: bool

app = FastAPI(title="customer-churn-prediction")

# ---------- Model loading ----------
C = 1.0
dv = None
model = None

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"
MODEL_FILE = MODELS_DIR / f"churn_model_C={C}.bin"

try:
    with open(MODEL_FILE, "rb") as f_in:
        dv, model = pickle.load(f_in)
        print("Loaded model from", MODEL_FILE)
except FileNotFoundError:
    # Let container start, but return 503 on predict until the model file is present.
    print(f"Model file not found at {MODEL_FILE}. Train first or mount the file.")

@app.get("/health")
def health():
    ok = dv is not None and model is not None
    return {"status": "ok" if ok else "model_missing"}

@app.post("/predict")
def predict(customer: Customer) -> PredictResponse:
    if dv is None or model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")

    X = dv.transform([customer.model_dump()])
    prob = model.predict_proba(X)[0, 1]
    churn = prob >= 0.5

    return PredictResponse(
        churn_probability=float(prob),
        will_churn=bool(churn)
    )
