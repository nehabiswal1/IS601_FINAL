"""
File: test_database_operations.py

Overview:
This Python test file utilizes pytest to manage database states and HTTP clients for testing a web application built with FastAPI and SQLAlchemy. It includes detailed fixtures to mock the testing environment, ensuring each test is run in isolation with a consistent setup.

Fixtures:
- `async_client`: Manages an asynchronous HTTP client for testing interactions with the FastAPI application.
- `db_session`: Handles database transactions to ensure a clean database state for each test.
- User fixtures (`user`, `locked_user`, `verified_user`, etc.): Set up various user states to test different behaviors under diverse conditions.
- `token`: Generates an authentication token for testing secured endpoints.
- `initialize_database`: Prepares the database at the session start.
- `setup_database`: Sets up and tears down the database before and after each test.
"""

# Standard library imports
from builtins import Exception, range, str
from datetime import timedelta
from unittest.mock import AsyncMock, patch
from uuid import uuid4

# Third-party imports
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, scoped_session
from faker import Faker

# Application-specific imports
import pytest
from datetime import timedelta
from uuid import uuid4
from unittest.mock import AsyncMock
from faker import Faker
from app.models.user_model import User, UserRole
from app.services.jwt_service import create_access_token
from app.utils.security import hash_password

fake = Faker()

@pytest.fixture(scope="function")
async def user(db_session):
    user_data = {
        "nickname": fake.user_name(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "hashed_password": hash_password("MySuperPassword$1234"),
        "role": UserRole.AUTHENTICATED,
        "email_verified": False,
        "is_locked": False,
    }
    user = User(**user_data)
    db_session.add(user)
    await db_session.commit()
    return user

@pytest.fixture(scope="function")
async def admin_user(db_session):
    admin_data = {
        "nickname": "admin_user",
        "email": "admin@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "hashed_password": hash_password("securepassword"),
        "role": UserRole.ADMIN,
        "is_locked": False,
    }
    admin_user = User(**admin_data)
    db_session.add(admin_user)
    await db_session.commit()
    return admin_user

@pytest.fixture(scope="function")
async def manager_user(db_session):
    manager_data = {
        "nickname": "manager_user",
        "email": "manager@example.com",
        "first_name": "Jane",
        "last_name": "Doe",
        "hashed_password": hash_password("securepassword"),
        "role": UserRole.MANAGER,
        "is_locked": False,
    }
    manager_user = User(**manager_data)
    db_session.add(manager_user)
    await db_session.commit()
    return manager_user

# Updated token fixtures to handle async user fixtures
@pytest.fixture(scope="function")
async def admin_token(admin_user):
    admin_user = await admin_user  # Await the admin_user fixture
    token_data = {"sub": str(admin_user.id), "role": admin_user.role.name}
    return create_access_token(data=token_data, expires_delta=timedelta(minutes=30))

@pytest.fixture(scope="function")
async def manager_token(manager_user):
    manager_user = await manager_user  # Await the manager_user fixture
    token_data = {"sub": str(manager_user.id), "role": manager_user.role.name}
    return create_access_token(data=token_data, expires_delta=timedelta(minutes=30))

@pytest.fixture(scope="function")
async def user_token(user):
    user = await user  # Await the user fixture
    token_data = {"sub": str(user.id), "role": user.role.name}
    return create_access_token(data=token_data, expires_delta=timedelta(minutes=30))

@pytest.fixture
def email_service():
    if settings.send_real_mail == "true":
        # Return the real email service when testing email functionality
        return EmailService()
    else:
        # Otherwise, use a mock to prevent actual email sending
        mock_service = AsyncMock(spec=EmailService)
        mock_service.send_verification_email.return_value = None
        mock_service.send_user_email.return_value = None
        return mock_service

