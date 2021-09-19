from wsgi import app
from core import db
from models import *
import pandas as pd
import random
from geoalchemy2 import func
with app.app_context():
    # data_ = pd.read_csv('sample_locations2.csv')
    # df = pd.DataFrame(data_)
    # names = ["John", "Fin", "Einstein"]
    # for index, row in df.iterrows():
    #     new_user = User(
    #         name=names[random.randint(0,2)],
    #         lon=row.X,
    #         lat=row.Y,
    #         is_handyman=bool(random.randint(0,1)),
    #         geometry='SRID=4269;POINT(%.8f %.8f)'%(row.X, row.Y)
    #     )
    #     db.session.add(new_user)
    # db.session.commit()
    lng, lat = 148.523, -35.40
    geo_wkb = func.Make

    new_point = db.session.query(User).filter(
        func.PtDistWithin(
            User.geometry,
            geo_wkb,
            10000
        )
    ).one()
    print(new_point)
