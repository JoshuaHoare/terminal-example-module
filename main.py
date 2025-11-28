from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/module/metadata")
async def metadata():
    return {
        "id": "example-module",
        "name": "Example Module",
        "description": "An example FastAPI module",
        "version": "0.1.0",
    }


@app.get("/health")
async def health():
    return {"status": "ok"}


class ConfigurationPayload(BaseModel):
    id: str
    name: str
    port: int


@app.post("/module/configuration")
async def configuration(payload: ConfigurationPayload):
    # In a real module this would persist or apply the configuration.
    # For now we just acknowledge it so Terminal can keep the table in sync.
    return {"ok": True}
