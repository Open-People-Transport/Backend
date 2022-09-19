import strawberry

import app


@strawberry.type
class Query:
    @strawberry.field
    def server_version(self) -> str:
        return app.__version__


schema = strawberry.Schema(query=Query)
