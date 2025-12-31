from fastapi import APIRouter, HTTPException, Query
from app.services.calculator import add, subtract, multiply, divide, modulo

router = APIRouter(tags=["calculator"])

@router.get("/add")
def add_route(a: float = Query(...), b: float = Query(...)):
    return {"operation": "add", "a": a, "b": b, "result": add(a, b)}

@router.get("/subtract")
def subtract_route(a: float = Query(...), b: float = Query(...)):
    return {"operation": "subtract", "a": a, "b": b, "result": subtract(a, b)}

@router.get("/multiply")
def multiply_route(a: float = Query(...), b: float = Query(...)):
    return {"operation": "multiply", "a": a, "b": b, "result": multiply(a, b)}

@router.get("/divide")
def divide_route(a: float = Query(...), b: float = Query(...)):
    try:
        result = divide(a, b)
    except ZeroDivisionError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"operation": "divide", "a": a, "b": b, "result": result}

@router.get("/modulo")
def divide_route(a: float = Query(...), b: float = Query(...)):
    try:
        result = modulo(a, b)
    except ZeroDivisionError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"operation": "modulo", "a": a, "b": b, "result": result}

