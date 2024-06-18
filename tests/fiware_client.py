class Room(BaseModel):
    id: str
    type: str
    temperature: Optional[Dict[str, Any]]
    pressure: Optional[Dict[str, Any]]


base_url = None  # set this
auth_token = None  # set this

fiware = FiwareClient(base_url, auth_token=auth_token)

# Using Pydantic model for attributes
entity_room = Room(
    id="urn:ngsi-ld:test:t:tt-01:Room:Room3",
    type="Product",
    temperature={"value": 23, "type": "Property"},
    pressure={"value": 720, "type": "Property"}
)


def test_create_entity():
    # Create an entity using the Pydantic model
    response = fiware.create_entity(entity_room)
    print('Create Entity with Pydantic Model:', response)


def test_get_entity():
    # Retrieve the entity
    response = fiware.get_entity(entity_room.id)
    print('Get Entity:', response)


def test_update_entity():
    # Update the entity using a dictionary
    entity_room.temperature["value"] = 27
    response = fiware.update_entity(entity_room)
    print('Update Entity with Dictionary:', response)


def test_delete_entity():
    # Delete the entity
    response = fiware.delete_entity(entity_room.id)
    print('Delete Entity:', response)
