# Python-Keycloak-API
An API implementation of Keycloak without using the UI of the Keycloak admin directly using the Python client for Keycloak


# Keycloak Integration with Python

This repository contains Python code for interacting with Keycloak, including user management and role assignment. The code uses the `keycloak` library to connect to a Keycloak server, create users, update user details, and assign roles to users.

## Prerequisites

Before you can run this code, ensure you have the following prerequisites installed:

- Python (3.6 or higher)
- `keycloak` library (install it using `pip install python-keycloak`)

## Configuration

1. Create a `config.json` file in the root directory of the project and add the following Keycloak configuration:

```
{
  "KEYCLOAK_SERVER_URL": "https://your-keycloak-server-url/auth",
  "KEYCLOAK_REALM": "your-realm-name",
  "KEYCLOAK_CLIENT_ID": "your-client-id",
  "KEYCLOAK_CLIENT_SECRET": "your-client-secret"
}
```
-Replace the placeholders with your Keycloak server URL, realm name, client ID, and client secret.
## Usage

1. Import the required libraries:

```
from keycloak import KeycloakAdmin
from keycloak import KeycloakOpenID
from keycloak import KeycloakOpenIDConnection
import json

```

2. Load the Keycloak configuration from config.json:
```
with open("config.json", "r") as config_data:
    config = json.load(config_data)

KEYCLOAK_SERVER_URL = config["KEYCLOAK_SERVER_URL"]
KEYCLOAK_REALM = config["KEYCLOAK_REALM"]
KEYCLOAK_CLIENT_ID = config["KEYCLOAK_CLIENT_ID"]
KEYCLOAK_CLIENT_SECRET = config["KEYCLOAK_CLIENT_SECRET"]

```
3. Initialize KeycloakOpenID and KeycloakOpenIDConnection objects for authentication and user management:
```
keycloak_oidc = KeycloakOpenID(
    server_url=KEYCLOAK_SERVER_URL,
    realm_name=KEYCLOAK_REALM,
    client_id=KEYCLOAK_CLIENT_ID,
    client_secret_key=KEYCLOAK_CLIENT_SECRET
)

keycloak_connection = KeycloakOpenIDConnection(
    server_url=KEYCLOAK_SERVER_URL,
    username="user-admin",
    password="pass",
    realm_name=KEYCLOAK_REALM,
    user_realm_name=KEYCLOAK_REALM,
    client_id=KEYCLOAK_CLIENT_ID,
    client_secret_key=KEYCLOAK_CLIENT_SECRET,
    verify=True
)

```

4. Initialize the KeycloakAdmin object to manage users and roles:
```
keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

```

5. Create a new user:
```
request_obj = {
    "email": "user@example.com",
    "username": "user",
    "enabled": True,
    "firstName": "User",
    "lastName": "Name",
    "credentials": [{"value": "password123", "type": "password"}]
}

new_user = keycloak_admin.create_user(request_obj, exist_ok=False)
print("Created new user with id:", new_user)

```
6. Update user details:
```request_obj = {
    "email": "newemail@example.com",
    "enabled": True,
    "firstName": "UserChanged",
    "lastName": "NameChanged",
}
user_id = keycloak_admin.get_user_id(username="user")
keycloak_admin.update_user(user_id=user_id, payload=request_obj)
```
7. Print user details:
```
print(keycloak_admin.get_user(user_id=user_id))
```
8. Assign roles to user:
```# Get a realm role (you need 'manage-realm' permission)
role = keycloak_admin.get_realm_role('user')
keycloak_admin.assign_realm_roles(user_id=user_id, roles=role)
```
9. Get the verification action for email.
```verification_action = keycloak_admin.get_required_action_by_alias('VERIFY_EMAIL') 
    # This uses a required actions method which is called with alias by it's name.
```
# Disable SSH in Docker 

## To disable SSH in docker container 
1. Access the keycloak shell and then:
```
docker exec -it ContainerID /bin/bash/

```
2. Update the realm's SSL requirements (replace http://localhost:8080/ with your Keycloak server URL):

```
./kcadm.sh update realms/master -s sslRequired=NONE --server http://localhost:8080/ --realm master --user admin
```
## Custom Themes of Keycloak

To customize themes in Keycloak, follow these steps:

1. Access the Keycloak Docker container's shell:

   ```docker exec -it keycloakContainerID /bin/bash```
2. Navigate to the Keycloak home directory:
 ```cd ..```

3. Change directory to the themes directory:
```cd themes```
4. Add your personal theme folder to the themes directory.

5. Paste your custom theme files into the theme folder.

6. Exit the container shell.

7.  Restart the Keycloak container.

## Needed Permissions
-"manage-realm" permission is required for adding roles to users.

-Ensure that port 587 with TLS is enabled for email functionality.
