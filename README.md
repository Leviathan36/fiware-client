# CRUD operations for Fiware platform

**Easy usage**:
- create the client instance by setting the url and authentication token
- create the entity to upload or modify one you already have (you can use json format or a pydantic object)
- performs the operation (Create, Read, Update, Delete). PS For simplicity, the read function is called get.


```python
base_url = 'http://localhost:1026/v2/'
auth_token = '97c97c49-6013-4ca7-847b-ff88c4b720b4'

fiware = FiwareClient(base_url, auth_token=auth_token)

# Create an entity using the Pydantic model
response = fiware.create_entity(entity_room)
print('Create Entity with Pydantic Model:', response)


# Retrieve the entity
response = fiware.get_entity(entity_room.id)
print('Get Entity:', response)


# Update the entity using a dictionary
entity_room.temperature["value"] = 27
response = fiware.update_entity(entity_room)
print('Update Entity with Dictionary:', response)


# Delete the entity
response = fiware.delete_entity(entity_room.id)
print('Delete Entity:', response)
```