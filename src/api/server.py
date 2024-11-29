from fastapi import FastAPI
from .api_controllers import from_location, to_location

app = FastAPI(docs_url="/")
app.include_router(from_location)
app.include_router(to_location)
