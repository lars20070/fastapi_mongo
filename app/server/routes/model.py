from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    create_model,
    delete_model,
    retrieve_model,
    retrieve_models,
    update_model,
)
from app.server.models.model import (
    ErrorResponseModel,
    ResponseModel,
    ModelSchema,
    UpdateModelModel,
)

router = APIRouter()


@router.post("/", response_description="Model data added into the database")
async def add_model_data(model: ModelSchema = Body(...)):
    model = jsonable_encoder(model)
    new_model = await create_model(model)
    return ResponseModel(new_model, "Model added successfully.")


@router.get("/", response_description="Models retrieved")
async def get_models():
    models = await retrieve_models()
    if models:
        return ResponseModel(models, "Models data retrieved successfully")
    return ResponseModel(models, "Empty list returned")


@router.get("/{id}", response_description="Model data retrieved")
async def get_model_data(id):
    model = await retrieve_model(id)
    if model:
        return ResponseModel(model, "Model data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Model doesn't exist.")


@router.put("/{id}")
async def update_model_data(id: str, req: UpdateModelModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_model = await update_model(id, req)
    if updated_model:
        return ResponseModel(
            "Model with ID: {} name update is successful".format(id),
            "Model name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the model data.",
    )


@router.delete("/{id}", response_description="Model data deleted from the database")
async def delete_model_data(id: str):
    deleted_model = await delete_model(id)
    if deleted_model:
        return ResponseModel(
            "Model with ID: {} removed".format(id), "Model deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Model with id {0} doesn't exist".format(id)
    )
