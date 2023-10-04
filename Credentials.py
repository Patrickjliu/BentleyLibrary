import os

#Credentials
os.environ['DB_HOST'] = 'localhost'
os.environ['DB_USER'] = 'root'
os.environ['DB_PASSWORD'] = 'Bentley2023'
os.environ['DB_NAME'] = 'BentleyLibrary'

db_config = {
    'user': 'root',
    'password': 'Bentley2023',
    'host': 'localhost',
    'database': 'BentleyLibrary',
    'auth_plugin': 'caching_sha2_password',
}