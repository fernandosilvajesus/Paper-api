from pypdf import PdfReader, PdfWriter
from fastapi import UploadFile
from typing import List
import io


async def merge_pdfs(files: List[UploadFile], output_path: str) -> None:
    writer = PdfWriter()

    for file in files:
        content = await file.read()
        reader = PdfReader(io.BytesIO(content))
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as f_out:
        writer.write(f_out)
