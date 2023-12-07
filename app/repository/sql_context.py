from app.models import DB


class SqlContext(object):
    def __init__(self, auto_commit=True):
        self.session = DB.session
        self.auto_commit = auto_commit

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self.session and self.auto_commit:
            try:
                self.session.commit()
            except Exception as ex:
                self.session.rollback()
                raise ex
