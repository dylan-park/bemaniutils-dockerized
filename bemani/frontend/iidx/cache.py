from flask_caching import Cache  # type: ignore

from bemani.data import Config, Data
from bemani.frontend.app import app
from bemani.frontend.iidx.iidx import IIDXFrontend


class IIDXCache:

    @classmethod
    def preload(cls, data: Data, config: Config) -> None:
        cache = Cache(app, config={
            'CACHE_TYPE': 'filesystem',
            'CACHE_DIR': config.cache_dir,
        })
        frontend = IIDXFrontend(data, config, cache)
        frontend.get_all_songs(force_db_load=True)
