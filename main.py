from fastapi import FastAPI, Query
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="Eigen Value & Vector API")

# ---------- POST REQUEST ----------
class MatrixRequest(BaseModel):
    a11: float
    a12: float
    a13: float
    a21: float
    a22: float
    a23: float
    a31: float
    a32: float
    a33: float

@app.post("/eigen")
async def eigen_post(req: MatrixRequest):
    matrix = np.array([
        [req.a11, req.a12, req.a13],
        [req.a21, req.a22, req.a23],
        [req.a31, req.a32, req.a33]
    ])
    values, vectors = np.linalg.eig(matrix)
    return {
        "matrix": matrix.tolist(),
        "eigenvalues": values.tolist(),
        "eigenvectors": vectors.tolist()
    }


# ---------- GET REQUEST ----------
@app.get("/eigen")
async def eigen_get(
    a11: float = Query(...),
    a12: float = Query(...),
    a13: float = Query(...),
    a21: float = Query(...),
    a22: float = Query(...),
    a23: float = Query(...),
    a31: float = Query(...),
    a32: float = Query(...),
    a33: float = Query(...)
):
    matrix = np.array([
        [a11, a12, a13],
        [a21, a22, a23],
        [a31, a32, a33]
    ])
    values, vectors = np.linalg.eig(matrix)
    return {
        "matrix": matrix.tolist(),
        "eigenvalues": values.tolist(),
        "eigenvectors": vectors.tolist(),
        "Service": "CASPAM Compute Services"
    }
