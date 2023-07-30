from keycloak import KeycloakAdmin
from keycloak import KeycloakOpenID
from keycloak import KeycloakOpenIDConnection
import json

with open("config.json", "r") as config_data:
    config = json.load(config_data)

KEYCLOAK_SERVER_URL = config["KEYCLOAK_SERVER_URL"]
KEYCLOAK_REALM = config["KEYCLOAK_REALM"]
KEYCLOAK_CLIENT_ID = config["KEYCLOAK_CLIENT_ID"]
KEYCLOAK_CLIENT_SECRET = config["KEYCLOAK_CLIENT_SECRET"]

keycloak_oidc = KeycloakOpenID(
    server_url=KEYCLOAK_SERVER_URL,  # server url
    realm_name=KEYCLOAK_REALM,  # your realm name
    client_id=KEYCLOAK_CLIENT_ID,  # your client id
    client_secret_key=KEYCLOAK_CLIENT_SECRET,  # your client secret id
)
# To get the keycloak public key we use
KEYCLOAK_PUBLIC_KEY = (
    "-----BEGIN PUBLIC KEY-----\n"
    + keycloak_oidc.public_key()
    + "\n-----END PUBLIC KEY-----"
)
# To create an openID Connection
keycloak_connection = KeycloakOpenIDConnection(
    server_url=KEYCLOAK_SERVER_URL,  # server url
    username="user-admin",  # server admin username
    password="pass",  # server admin password
    realm_name=KEYCLOAK_REALM,  # realm where the client which is creating the new user is located
    user_realm_name=KEYCLOAK_REALM,  # realm where the client in which the new user is to be created is located
    client_id=KEYCLOAK_CLIENT_ID,  # client id of the client which is creating the new user
    client_secret_key=KEYCLOAK_CLIENT_SECRET,  # client secret of the client which is creating the new user
    verify=True,
)

keycloak_admin = KeycloakAdmin(connection=keycloak_connection)


request_obj = {
    "email": "youremail@email.com",
    "username": "user",
    "enabled": True,
    "firstName": "User",  # For creating a user in a realm
    "lastName": "Name",
    "credentials": [{"value": "pass", "type": "password"}],
}

new_user = keycloak_admin.create_user(
    request_obj, exist_ok=False
)  # For printing the userinfo
print("Created new user with id:", new_user)  # To update existing user

request_obj = {
    "email": "youremail@email.com",
    "enabled": True,
    "firstName": "UserChanged",
    "lastName": "NameChanged",
}
id = keycloak_admin.get_user_id(username="user")
keycloak_admin.update_user(user_id=id, payload=request_obj)

# To print all the user Details we use the following function
print(keycloak_admin.get_user(user_id=id))

# To assign or create a role in keycloak we use the RoleRepresentation of the Keycloak....
# RoleRepresenataion consists of all the roles with their detals in a json format

role = keycloak_admin.get_realm_role('user') # Need to have the Realm-management permission

keycloak_admin.assign_realm_roles(user_id=id, roles=role)  # adding roles to the user