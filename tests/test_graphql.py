import app
from app.graphql import schema


def test_server_version_query():
    result = schema.execute_sync("query { serverVersion }")
    assert result.data == {"serverVersion": app.__version__}
