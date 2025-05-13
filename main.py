from fastapi import FastAPI

app = FastAPI()

@app.get("/calc")
def calc(op: str, a: float, b: float):
    if op == "+":
        return {"result": a + b}
    if op == "-":
        return {"result": a - b}
    return {"error": 404}