from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.routes.health import router as health_router


app = FastAPI(
    title="new-test-m-argo",
    description="FastAPI microservice",
    version="0.1.0",
)


@app.get("/", tags=["service"])
def service_info():
    return {
        "service": "new-test-m-argo",
        "status": "running",
        "version": "0.1.0",
    }


app.include_router(health_router)

Instrumentator(
    should_group_status_codes=False,
    excluded_handlers=["/metrics", "/health"],
).instrument(app).expose(app, endpoint="/metrics", include_in_schema=False)
