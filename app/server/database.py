import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.models

model_collection = database.get_collection("models_collection")


# helpers
def model_helper(model) -> dict:
    return {
        "id": str(model["_id"]),
        "model_name": model["model_name"],
        "image_folder": model["image_folder"],
        "tfrecord_folder": model["tfrecord_folder"],
        "contact_email": model["contact_email"],
        "score": model["score"],
    }


# Retrieve all models present in the database
async def retrieve_models():
    model = []
    async for model in model_collection.find():
        model.append(model_helper(model))
    return model


# Add a new model into to the database
async def create_model(model_data: dict) -> dict:
    model = await model_collection.insert_one(model_data)
    new_model = await model_collection.find_one({"_id": model.inserted_id})
    return model_helper(new_model)


# Retrieve a model with a matching ID
async def retrieve_model(id: str) -> dict:
    model = await model_collection.find_one({"_id": ObjectId(id)})
    if model:
        return model_helper(model)


# Update a model with a matching ID
async def update_model(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    model = await model_collection.find_one({"_id": ObjectId(id)})
    if model:
        updated_model = await model_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_model:
            return True
        return False


# Delete a model from the database
async def delete_model(id: str):
    model = await model_collection.find_one({"_id": ObjectId(id)})
    if model:
        await model_collection.delete_one({"_id": ObjectId(id)})
        return True
