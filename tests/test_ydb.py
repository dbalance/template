import asyncio

import sqlalchemy as sa
from sqlalchemy.util.concurrency import greenlet_spawn
from sqlalchemy.dialects import registry
from sqlalchemy.pool import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from logging import basicConfig, DEBUG


async def ydb():
    registry.register('sql.asyncydb', 'tests.dialect', 'Dialect')
    basicConfig(level=DEBUG)
    engine = create_async_engine("sql+asyncydb://localhost:2136/local", poolclass=AsyncAdaptedQueuePool, echo=True)
    #
    # engine = create_async_engine("yql+ydb_async://localhost:2136/local", poolclass=AsyncAdaptedQueuePool, echo=True)
    maker = async_sessionmaker(engine, expire_on_commit=False)
    async with maker() as session:
        res = await session.scalar(sa.text("SELECT 1 AS value"))

    print(res)




if __name__ == '__main__':
    asyncio.run(ydb())