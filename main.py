from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import driver, history, calculate

# import uvicorn


app = FastAPI()
app.include_router(driver.router)
app.include_router(history.router)
app.include_router(calculate.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

