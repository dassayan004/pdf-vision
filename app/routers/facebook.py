from typing import Optional

from fastapi import APIRouter, File, HTTPException, Path, UploadFile

# from app.dto.facebook_dto import FacebookResponse
from app.services.facebook_service import FacebookService

router = APIRouter(tags=["facebook"], prefix="/facebook")
service = FacebookService()


@router.get("/posts")
def extract_facebook_data():
    # Placeholder implementation
    # In a real implementation, you would call the service to extract data from Facebook
    return service.extract_facebook_data()


@router.get("/posts/{post_id}")
def extract_facebook_post(
    post_id: int = Path(..., title="The ID of the post to get"),
    include_desc: bool = True,
    q: Optional[str] = None,
):

    result = service.extract_facebook_post(post_id, include_desc, q)
    if not result:
        raise HTTPException(status_code=404, detail="Post not found")

    return result
