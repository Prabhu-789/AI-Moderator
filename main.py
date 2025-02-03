from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import threading

from fastApiProject.ModeratorService.auth.config.logging import configure_logging
import logging
import fastApiProject.ModeratorService.auth.models as auth_models
from fastApiProject.ModeratorService.auth.config.database import engine
from fastApiProject.ModeratorService.auth.controllers import user_controller as auth_controller


configure_logging()
logger = logging.getLogger(__name__)
app = FastAPI(title="AI-Moderator",
              docs_url="/api/docs",  # Swagger UI
              redoc_url="/api/redoc",  # ReDoc UI
              openapi_url="/api/openapi.json",  # OpenAPI schema
              # lifespan=lifespan
              )


app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],  # Allow all origins
	allow_credentials=True,
	allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
	allow_headers=["*"],  # Allow all headers
)

auth_models.Base.metadata.create_all(bind=engine)
app.include_router(auth_controller.router)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
	logger.error("Unhandled exception: %s", str(exc), exc_info=True)
	return JSONResponse(
		status_code=500,
		content={"detail": "An unexpected error occurred."},
	)