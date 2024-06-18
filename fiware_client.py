from typing import Any, Dict, Optional, Union

import requests
from pydantic import BaseModel


class FiwareClient:
    def __init__(self, base_url: str, auth_token: Optional[str] = None, headers: Optional[Dict[str, str]] = None):

        self.base_url = base_url

        if headers is None:
            self.headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        else:
            self.headers = headers

        if auth_token is not None:
            self.headers['Authorization'] = f'Bearer {auth_token}'

    def http_req(self, url, data: Optional[Dict] = None, params: Optional[Dict] = None):
        print(f"[*] Sending {data}...")
        if data is not None:
            response = requests.post(url, json=data, headers=self.headers)
        elif params is not None:
            response = requests.get(url, params=params, headers=self.headers)
        else:
            response = requests.delete(url, headers=self.headers)
        print(response.text)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response
    
    def create_entity(self, entity: Union[Dict[str, Any], BaseModel]) -> Dict[str, Any]:
        """Create a new entity."""
        url = f'{self.base_url}/entities'
        
        if isinstance(entity, BaseModel):
            data = entity.model_dump()
        elif isinstance(entity, Dict):
            data = entity
        else:
            raise TypeError(f"Entity must be a Dict or BaseModel type")
        if not (data['id'] and data['type']):
            raise ValueError(f"id and type must be specified")
        return self.http_req(url, data=data)
    
    def get_entity(self, entity_id: str, entity_type: Optional[str] = None) -> Dict[str, Any]:
        """Retrieve an entity by its ID and type."""
        url = f'{self.base_url}/entities/{entity_id}'
        params = {'type': entity_type} if entity_type else {}
        return self.http_req(url, params=params)
    
    def update_entity(self, entity: Union[Dict[str, Any], BaseModel]) -> Dict[str, Any]:
        """Update an entity's attributes."""
        if isinstance(entity, BaseModel):
            data = entity.model_dump()
        elif isinstance(entity, Dict):
            data = entity
        else:
            raise TypeError(f"Entity must be a Dict or BaseModel type")
        if not (data['id'] and data['type']):
            raise ValueError(f"id and type must be specified")
        
        url = f'{self.base_url}/entities/{data["id"]}/attrs'
        return self.http_req(url, data=data)
    
    def delete_entity(self, entity_id: str) -> Dict[str, Any]:
        """Delete an entity."""
        url = f'{self.base_url}/entities/{entity_id}'
        return self.http_req(url)
