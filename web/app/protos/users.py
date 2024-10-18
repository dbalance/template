from fastapi_users.models import UserProtocol as Proto


class UserProtocol(Proto):
    """User protocol that ORM model should follow."""

    id: int
    username: str
    email: str | None
