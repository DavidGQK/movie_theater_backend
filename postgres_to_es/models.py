from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Set
from uuid import UUID


@dataclass(frozen=True)
class Person:
    uuid: UUID
    full_name: str
    role: str = None
    birth_date: date = None
    updated_at: datetime = None


@dataclass(frozen=True)
class Genre:
    uuid: UUID
    name: str
    updated_at: datetime = None


@dataclass
class FilmWork:
    uuid: UUID
    title: str
    description: str = None
    rating: float = field(default=0.0)
    type: str = None
    created_at: datetime = None
    updated_at: datetime = None
    actors: set[Person] = field(default_factory=set)
    directors: set[Person] = field(default_factory=set)
    writers: set[Person] = field(default_factory=set)
    genres: set[Genre] = field(default_factory=set)
