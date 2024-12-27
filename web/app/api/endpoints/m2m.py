from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_sqlalchemy_toolkit import ModelManager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from ...db.models import Word, Sentence, Composition
from ...schemas import WordCreate, WordRead, SentenceRead, SentenceCreate, CompositionRead, CompositionCreate, \
    WordReadCompositions, SentenceCompositionRead
from ...dependencies import get_async_session
from ...schemas.m2m import WordReadSentence

r = APIRouter()

word_manager = ModelManager(Word)
sentence_manager = ModelManager(Sentence)
composition_manager = ModelManager(Composition)


@r.post('/', response_model=WordRead)
async def word(obj: WordCreate,
               session: AsyncSession = Depends(get_async_session)):
    return await word_manager.create(session, obj)


@r.get('/', response_model=list[WordReadCompositions])
async def words(
        text: str,
        session: AsyncSession = Depends(get_async_session),

):
    return await word_manager.list(session, filter_expressions={Sentence.text: text},
                                   options=[joinedload(Word.compositions).subqueryload(Composition.sentence)],
                                   unique=True)


@r.get('another/', response_model=list[WordReadSentence])
async def words(
        text: str,
        session: AsyncSession = Depends(get_async_session),

):
    return await word_manager.list(session, filter_expressions={Sentence.text: text},
                                   options=[joinedload(Word.sentences)],
                                   unique=True)



@r.post('/sentence', response_model=SentenceRead)
async def sentences(obj: SentenceCreate,
                    session: AsyncSession = Depends(get_async_session)):
    return await sentence_manager.create(session, obj)


@r.get('/sentence', response_model=list[SentenceCompositionRead])
async def sentence(
        session: AsyncSession = Depends(get_async_session)
):
    return await sentence_manager.list(session,
                                       options=[joinedload(Sentence.compositions).subqueryload(Composition.word)],
                                       unique=True)


@r.get('/composition', response_model=list[CompositionRead])
async def composition(
        session: AsyncSession = Depends(get_async_session)
):
    return await composition_manager.list(session,
                                          options=[joinedload(Composition.word), joinedload(Composition.sentence)],
                                          unique=True)


@r.post('/composition', response_model=CompositionRead)
async def composition(
        obj: CompositionCreate,
        session: AsyncSession = Depends(get_async_session)
):
    return await composition_manager.create(session, obj, refresh_attribute_names=['sentence', 'word'])
