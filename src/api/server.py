from fastapi import FastAPI
from .api_controllers import from_location, to_location, coordinate

app = FastAPI(docs_url="/")
app.include_router(from_location)
app.include_router(to_location)
app.include_router(coordinate)
