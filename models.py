from peewee import *
import datetime
import config

db = SqliteDatabase(config.db_file)

class BaseModel(Model):
    class Meta:
        database = db


class Point(BaseModel):
    lat = FloatField(null=True, unique=False, default=0)
    lon = FloatField(null=True, unique=False, default=0)
    alt = FloatField(null=True, unique=False, default=0)
    speed = FloatField(null=True, unique=False, default=0)
    new_field = FloatField(null=True, unique=False, default=0)

    token = CharField(unique=False, null=False, default="test")
    created_at = DateTimeField(default=datetime.datetime.now())

    @property
    def time_str(self):
        return self.created_at.strftime("%d.%m.%Y, %H:%M:%S")

    @property
    def json(self):
        return {'lat': self.lat, 'lon': self.lon, 'created_at': self.time_str}

    @property
    def json_map(self):
        return [self.lat, self.lon]
    