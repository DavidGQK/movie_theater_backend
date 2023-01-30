import abc
import json
import datetime
from typing import Any, Optional

from redis import Redis


class BaseStorage:
    @abc.abstractmethod
    def save_state(self, state: dict) -> None:
        """Save the state in constant storage"""
        pass

    @abc.abstractmethod
    def retrieve_state(self) -> dict:
        """Download the state localy from storage"""
        pass


class RedisStorage(BaseStorage):
    def __init__(self, redis_adapter: Redis, redis_db: str) -> None:
        self.redis_adapter = redis_adapter
        self.redis_db = redis_db

    def save_state(self, state: dict) -> None:
        self.redis_adapter.set(self.redis_db, json.dumps(state))

    def retrieve_state(self) -> dict:
        state = self.redis_adapter.get(self.redis_db)
        state = json.loads(state) if state else {}
        return state


class State:
    def __init__(self, storage: BaseStorage):
        self.storage = storage

    def set_state(self, key: str, value: Any) -> None:
        """Set the state by the key"""
        state = self.storage.retrieve_state()
        state[key] = value.isoformat()
        self.storage.save_state(state)

    def get_state(self, key: str) -> Any:
        """Get the state by the key"""
        state = self.storage.retrieve_state()
        state = state.get(key)
        if state:
            state = datetime.datetime.fromisoformat(state)
        return state
