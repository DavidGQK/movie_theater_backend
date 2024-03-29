import uuid
from datetime import datetime
from typing import List, Type, Union
from dataclasses import field, fields, dataclass

from dateutil import parser


@dataclass
class FilmWork:
    title: str
    description: str = None
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    creation_date: str = None
    certificate: str = None
    file_path: str = None
    rating: float = field(default=0.0)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    type: str = field(default="movie")


@dataclass
class Genre:
    name: str
    description: str = None
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


@dataclass
class Person:
    full_name: str
    birth_date: str = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class FilmWorkPerson:
    film_work_id: uuid.UUID
    person_id: uuid.UUID
    role: str = None
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class FilmWorkGenre:
    film_work_id: uuid.UUID
    genre_id: uuid.UUID
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = field(default_factory=datetime.now)


fields_types: List[Type[Union[str, float, datetime, uuid.UUID]]] = [
    str,
    float,
    datetime,
    uuid.UUID,
]


def sanitize_field(field_type: fields_types, field_value: str) -> fields_types:
    dict_type_function = {
        float: float,
        uuid.UUID: uuid.UUID,
        str: lambda x: x.replace("'", "''"),
        datetime: parser.isoparse,
    }
    return dict_type_function[field_type](field_value)
