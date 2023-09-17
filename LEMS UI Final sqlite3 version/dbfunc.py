import oracledb
from env import user, password, dsn
# oracledb.init_oracle_client()


def create_connection(user, password, dsn):
    connection = oracledb.connect(
        user=user,
        password=password,
        dsn=dsn)
    return connection

