from fastapi import FastAPI
import pickle
import sklearn
import pickle

from pydantic import BaseModel
import pandas as pd

class VaccinationData(BaseModel):
    Administered_Dose1_Recip: int
    Administered_Dose1_Pop_Pct: float
    Administered_Dose1_Recip_12PlusPop_Pct: float
    Administered_Dose1_Recip_18PlusPop_Pct: float
    Administered_Dose1_Recip_65PlusPop_Pct: float
    Series_Complete_Pop_Pct: float
    Series_Complete_12PlusPop_Pct: float
    Series_Complete_18PlusPop_Pct: float
    Series_Complete_65PlusPop_Pct: float
    Booster_Doses_Vax_Pct: float
    Booster_Doses_5Plus_Vax_Pct: float
    Booster_Doses_12Plus_Vax_Pct: float
    Booster_Doses_18Plus_Vax_Pct: float
    Booster_Doses_50Plus_Vax_Pct: float
    Booster_Doses_65Plus_Vax_Pct: float
    Second_Booster_50Plus_Vax_Pct: float
    Second_Booster_65Plus_Vax_Pct: float
    Series_Complete_Pop_Pct_SVI: int
    Series_Complete_12PlusPop_Pct_SVI: int
    Series_Complete_18PlusPop_Pct_SVI: int
    Series_Complete_65PlusPop_Pct_SVI: int
    Series_Complete_Pop_Pct_UR_Equity: int
    Series_Complete_12PlusPop_Pct_UR_Equity: int
    Series_Complete_18PlusPop_Pct_UR_Equity: int
    Series_Complete_65PlusPop_Pct_UR_Equity: int
    Booster_Doses_Vax_Pct_SVI: int
    Booster_Doses_12PlusVax_Pct_SVI: int
    Booster_Doses_18PlusVax_Pct_SVI: int
    Booster_Doses_65PlusVax_Pct_SVI: int
    Booster_Doses_Vax_Pct_UR_Equity: int
    Booster_Doses_12PlusVax_Pct_UR_Equity: int
    Booster_Doses_18PlusVax_Pct_UR_Equity: int
    Booster_Doses_65PlusVax_Pct_UR_Equity: int
    Pop_Size_Medium: int
    Pop_Size_Large: int
    Metro_status_Non_metro: int
    SVI_CTGY_B: int
    SVI_CTGY_C: int
    SVI_CTGY_D: int


app = FastAPI()
model = pickle.load(open("model.pkl", "rb"))

@app.post("/")


def read_root(data: VaccinationData):
    # Convert data to a pandas DataFrame with a single row
    df = pd.DataFrame([data.dict()])

    # Rename the column
    df.rename(columns={"Metro_status_Non_metro": "Metro_status_Non-metro"}, inplace=True)

    # Predict using the model
    prediction = model.predict(df)
    

    return {"Prediction %": str(prediction.tolist()[0] * 100) + " %"}
