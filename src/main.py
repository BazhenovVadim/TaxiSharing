import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.api.server:app", reload=True)