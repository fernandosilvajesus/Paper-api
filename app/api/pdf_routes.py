from fastapi import APIRouter, UploadFile, File
from app.services.pdf_utils import merge_pdfs
from fastapi.responses import FileResponse
import tempfile

router = APIRouter()


@router.post("/merge")
async def merge_files(files: list[UploadFile] = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_output:
        await merge_pdfs(files, temp_output.name)
        return FileResponse(
            temp_output.name, media_type="application/pdf", filename="merged.pdf"
        )
