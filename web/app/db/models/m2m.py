from .base import Base, IDMixin
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

class Sentence(IDMixin, Base):
    __tablename__ = 'sentences'
    text: Mapped[str] = mapped_column(String())
    compositions: Mapped[list['Composition']] = relationship(back_populates='sentence')
    words: Mapped[list['Word']] = relationship(back_populates='sentences', secondary='compositions')


class Word(IDMixin, Base):
    __tablename__ = 'words'
    cost: Mapped[int] = mapped_column(Integer)
    compositions: Mapped[list['Composition']] = relationship(back_populates='word')
    sentences: Mapped[list['Sentence']] = relationship(back_populates='words', secondary='compositions')


class Composition(IDMixin, Base):
    __tablename__ = 'compositions'
    sentence_id: Mapped[int] = mapped_column(ForeignKey('sentences.id'))
    word_id: Mapped[int] = mapped_column(ForeignKey('words.id'))
    freqs: Mapped[int] = mapped_column(Integer)
    sentence: Mapped['Sentence'] = relationship(back_populates='compositions')
    word: Mapped['Word'] = relationship(back_populates='compositions')