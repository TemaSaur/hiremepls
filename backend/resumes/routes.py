from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import StreamingResponse
from db.models.resume import Resume
from auth.depends import get_user

from peewee import DoesNotExist
import io


router = APIRouter()


@router.post("/")
async def upload(file: UploadFile = File(), _=Depends(get_user)) -> str:
    filename = file.filename
    filedata = await file.read()

    resume = Resume(filename=filename, filedata=filedata)
    resume.save()

    return resume.slug


@router.get("/{slug}")
async def download(slug):
    try:
        resume_db = Resume.get(Resume.slug == slug)
    except DoesNotExist:
        raise HTTPException(400, "No such resume")

    file_stream = io.BytesIO(resume_db.filedata)
    file_stream.seek(0)

    return StreamingResponse(
        file_stream,
        media_type="application/octet-stream",
        headers={
            "Content-Disposition":
            f"attachment; filename={resume_db.filename}"
        }
    )
