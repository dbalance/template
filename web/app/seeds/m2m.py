from polyfactory.factories.sqlalchemy_factory import SQLAlchemyFactory
from sqlalchemy.ext.asyncio import AsyncSession

from web.app.db.models import Word, Sentence

class BaseFactory(SQLAlchemyFactory):
    __is_base_factory__ = True

class SentenceFactory(BaseFactory):
    __model__ = Sentence


class WordFactory(BaseFactory):
    __model__ = Word
    __set_relationships__ = True


    # @classmethod
    # def sentences(cls):
    #     return SentenceFactory.batch(size=5)
    #
    #
    # @classmethod
    # def compotisions(cls):
    #     return []




async def seed(session: AsyncSession):
    WordFactory.__async_session__ = session

    await WordFactory.create_batch_async(size=20)