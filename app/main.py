from fastapi import FastAPI
from app.api.pdf_routes import router as pdf_router

app = FastAPI(
    title="Paper API",
    description="API local para manipulação de PDFs com privacidade",
    version="0.1.0"
)


app.include_router(pdf_router,prefix="/pdf",tags=['PDF Tools'])