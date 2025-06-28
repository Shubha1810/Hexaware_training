import os
import mysql.connector
from util.db_property_util import get_property_string

class DBConnUtil:
    @staticmethod
    def get_connection():
        # Dynamically resolve the absolute path to db_config.properties
        base_path = os.path.dirname(os.path.dirname(__file__))  # goes up one level to project root
        config_path = os.path.join(base_path, 'db_config.properties')

        props = get_property_string(config_path)

        return mysql.connector.connect(
            host=props['host'],
            user=props['user'],
            password=props['password'],
            database=props['database']
        )
