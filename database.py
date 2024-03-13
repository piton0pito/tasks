from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engion = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)
new_session = async_sessionmaker(engion, expire_on_commit=False)

class Model(DeclarativeBase):
    pass


class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


async def create_tables():
    async with engion.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_tables():
    async with engion.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)