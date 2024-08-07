from fastapi import FastAPI
from app.api.endpoints import users, items
from app.database.database import engine
from app.core.config import settings

# Initialize FastAPI application
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=settings.OPENAPI_URL,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
)

# Import database models
from app.api.models import *  # noqa

# Create database tables
Base.metadata.create_all(bind=engine)

# Include API routers
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])
