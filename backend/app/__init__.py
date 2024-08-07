from fastapi import FastAPI

from app.api.routers import api_router
from app.database.database import engine
from app.core.config import settings
from app.core.events import startup_event, shutdown_event

def create_application() -> FastAPI:
    """
    Create the FastAPI application.
    """
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=settings.OPENAPI_URL,
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOC_URL,
    )

    # Import database models to create tables
    from app.api.models import Base  # noqa

    # Create database tables
    Base.metadata.create_all(bind=engine)

    # Include API routers
    app.include_router(api_router)

    # Event handlers for startup and shutdown
    app.add_event_handler("startup", startup_event)
    app.add_event_handler("shutdown", shutdown_event)

    return app

app = create_application()

