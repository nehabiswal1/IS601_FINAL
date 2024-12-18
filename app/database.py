# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import declarative_base, sessionmaker
# from contextlib import asynccontextmanager
# import logging

# Base = declarative_base()

# class Database:
#     """Handles database connections and sessions."""
#     _engine = None
#     _session_factory = None
#     logger = logging.getLogger("database")

#     @classmethod
#     def initialize(cls, database_url: str, echo: bool = False):
#         """Initialize the async engine and sessionmaker."""
#         if cls._engine is None:
#             cls.logger.info("Initializing database engine...")
#             cls._engine = create_async_engine(database_url, echo=echo, future=True)
#             cls._session_factory = sessionmaker(
#                 bind=cls._engine, class_=AsyncSession, expire_on_commit=False, future=True
#             )
#             cls.logger.info("Database engine initialized.")
#         else:
#             cls.logger.warning("Database engine already initialized.")

#     @classmethod
#     async def dispose_engine(cls):
#         """Dispose of the engine to release database resources."""
#         if cls._engine:
#             cls.logger.info("Disposing database engine...")
#             await cls._engine.dispose()
#             cls.logger.info("Database engine disposed.")

#     @classmethod
#     def get_session_factory(cls):
#         """Returns the session factory, ensuring it's initialized."""
#         if cls._session_factory is None:
#             raise ValueError("Database not initialized. Call `initialize()` first.")
#         return cls._session_factory

#     @classmethod
#     @asynccontextmanager
#     async def get_session(cls):
#         """Provides an async session as a context manager."""
#         session_factory = cls.get_session_factory()
#         async with session_factory() as session:
#             yield session

#     @classmethod
#     def initialize_for_testing(cls, echo: bool = False):
#         """Initialize the database for testing using SQLite in-memory."""
#         cls.initialize("sqlite+aiosqlite:///:memory:", echo=echo)




from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Database:
    """Handles database connections and sessions."""
    _engine = None
    _session_factory = None

    @classmethod
    def initialize(cls, database_url: str, echo: bool = False):
        """Initialize the async engine and sessionmaker."""
        if cls._engine is None:  # Ensure engine is created once
            cls._engine = create_async_engine(database_url, echo=echo, future=True)
            cls._session_factory = sessionmaker(
                bind=cls._engine, class_=AsyncSession, expire_on_commit=False, future=True
            )

    @classmethod
    def get_session_factory(cls):
        """Returns the session factory, ensuring it's initialized."""
        if cls._session_factory is None:
            raise ValueError("Database not initialized. Call `initialize()` first.")
        return cls._session_factory
