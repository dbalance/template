from pydantic import BaseModel


class WordBase(BaseModel):
    cost: int


class WordModel(WordBase):
    id: int


class WordRead(WordModel):
    pass





class WordReadSentence(WordRead):
    sentences: list['SentenceRead']


class WordCreate(WordBase):
    pass


class SentenceBase(BaseModel):
    text: str


class SentenceModel(SentenceBase):
    id: int


class SentenceRead(SentenceModel):
    pass





class SentenceCreate(SentenceBase):
    pass


class CompositionBase(BaseModel):
    freqs: int


class WordComposition(CompositionBase):
    id: int
    sentence: SentenceRead


class WordReadCompositions(WordRead):
    compositions: list[WordComposition]


class SentenceComposition(CompositionBase):
    id: int
    word: WordRead


class CompositionRead(CompositionBase):
    id: int
    word: WordRead
    sentence: SentenceRead


class CompositionCreate(CompositionBase):
    sentence_id: int
    word_id: int


class SentenceCompositionRead(SentenceRead):
    compositions: list[SentenceComposition]