# Python-Keycloak-API
An API implementation of Keycloak without using the UI of the Keycloak admin directly using the Python client for Keycloak
This README provides a brief overview of how to use the Keycloak Python Client to interact with Keycloak's Admin API and OpenID Connect (OIDC) functionality. The client allows you to create users, update user details, manage roles, and more.

## Requirements

- Python 3.x
- Keycloak Server with Admin access and an existing realm

## Installation

1. Install the required packages:

```bash
pip install python-keycloak
```
## Configuration

1. Create a `config.json` file in the same directory as your Python script.
2. Populate the `config.json` file with the following information:

```json
{
    "KEYCLOAK_SERVER_URL": "https://your-keycloak-server/",
    "KEYCLOAK_REALM": "your-realm",
    "KEYCLOAK_CLIENT_ID": "your-client-id",
    "KEYCLOAK_CLIENT_SECRET": "your-client-secret"
}
```
## Implementation 

1. The implementation of the API is in the [`api.py`](https:github.com/S4tvik/Python-Keycloak-API/api.py) file in the same directory.
