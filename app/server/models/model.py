from typing import Optional

from pydantic import BaseModel, EmailStr, DirectoryPath, FilePath, Field


class ModelSchema(BaseModel):
    model_name: str = Field(...)
    image_folder: str = Field(...)
    tfrecord_folder: str = Field(...)
    contact_email: EmailStr = Field(...)
    score: float = Field(..., gt=0, le=10)

    class Config:
        schema_extra = {
            "example": {
                "model_name": "Corn Flakes",
                "image_folder": "C:/images",
                "tfrecord_folder": "C:/records",
                "contact_email": "lars.nilse@extern.sick.de",
                "score": "5.0",
            }
        }


class UpdateModelModel(BaseModel):
    model_name: Optional[str]
    image_folder: Optional[str]
    tfrecord_folder: Optional[str]
    contact_email: Optional[EmailStr]
    score: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "model_name": "Corn Flakes",
                "image_folder": "C:/images",
                "tfrecord_folder": "C:/records",
                "contact_email": "lars.nilse@extern.sick.de",
                "score": "5.0",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
