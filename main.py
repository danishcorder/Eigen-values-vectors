from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np

app = FastAPI(
    title="Eigen API",
    description="Compute eigenvalues and eigenvectors of a square matrix",
)

class EigenRequest(BaseModel):
    matrix: List[List[float]]  # Example: [[2, 1], [1, 2]]

def compute_eigen(matrix_np: np.ndarray):
    """Compute eigenvalues and eigenvectors using NumPy."""
    try:
        vals, vecs = np.linalg.eig(matrix_np)
        return vals.tolist(), vecs.tolist()
    except Exception as e:
        raise RuntimeError(str(e))

@app.post("/eigen")
async def eigen_post(req: EigenRequest):
    """POST request: accepts matrix as JSON"""
    mat = np.array(req.matrix, dtype=float)
    if mat.ndim != 2 or mat.shape[0] != mat.shape[1]:
        raise HTTPException(status_code=400, detail="Matrix must be square (n x n).")
    try:
        vals, vecs = compute_eigen(mat)
        return {"eigenvalues": vals, "eigenvectors": vecs}
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/eigen")
async def eigen_get(
    matrix: str = Query(..., description="Comma-separated entries row-wise, e.g. 2,1,1,2"),
    n: int = Query(..., description="Matrix size n for n×n matrix")
):
    """GET request: works directly in browser or with URL parameters"""
    try:
        entries = [float(x) for x in matrix.split(",")]
    except ValueError:
        raise HTTPException(status_code=400, detail="Matrix entries must be numeric.")

    if len(entries) != n * n:
        raise HTTPException(
            status_code=400,
            detail=f"Expected {n*n} entries for n={n}, got {len(entries)}."
        )

    mat = np.array(entries).reshape((n, n))
    try:
        vals, vecs = compute_eigen(mat)
        return {
            "eigenvalues": vals,
            "eigenvectors": vecs,
            "Service": "CASPAM Compute Services"
        }
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
