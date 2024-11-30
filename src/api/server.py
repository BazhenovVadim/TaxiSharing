from fastapi import FastAPI
from .api_controllers import   address

app = FastAPI(docs_url="/")
app.include_router(address)

