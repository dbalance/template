from ydb_sqlalchemy.sqlalchemy import AsyncYqlDialect, AdaptedAsyncConnection
from ydb_sqlalchemy.sqlalchemy.dbapi_adapter import AdaptedAsyncCursor
from sqlalchemy.util import await_only
from ydb_dbapi.utils import CursorStatus


class AsyncCursor(AdaptedAsyncCursor):
    def fetchone(self):
        return self._cursor._fetchone_from_buffer()

    def fetchmany(self, size=None):
        size = size or self.arraysize
        return self._cursor._fetchmany_from_buffer(size)

    def fetchall(self):
        return self._cursor._fetchall_from_buffer()

    def close(self):
        self._cursor._state = CursorStatus.closed


class AsyncConnection(AdaptedAsyncConnection):
    def cursor(self):
        return AsyncCursor(self._connection.cursor())


class Dialect(AsyncYqlDialect):
    driver = 'asyncydb'

    def connect(self, *cargs, **cparams):
        return AsyncConnection(await_only(self.dbapi.async_connect(*cargs, **cparams)))
