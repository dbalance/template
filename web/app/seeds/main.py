import asyncio
from web.app.conf import async_session_maker, engine
from web.app.db.setup import create_db_and_tables
from m2m import seed


async def main():
    await create_db_and_tables(engine)
    async with async_session_maker() as session:
        await seed(session)




if __name__ == '__main__':
    asyncio.run(main())