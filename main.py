from fastapi import FastAPI, Path, Query

app = FastAPI()

# Завдання №1
@app.get("/users/{user_id}")
def get_user(user_id: int = Path(..., description="ID користувача")):
    return {"user_id": user_id}

# Завдання №2
@app.get("/profile")
def get_profile(
    age: int = Query(0, description="Вік (за замовчуванням 0)"),
    nickname: str = Query(..., description="Нікнейм")
):
    return {"age": age, "nickname": nickname}

# Завдання №3
@app.get("/products/{product_id}")
def get_product_with_discount(
    product_id: int = Path(..., description="ID продукту"),
    discount: float = Query(..., description="Знижка у %")
):
    return {"product_id": product_id, "discount": discount}
