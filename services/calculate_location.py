import math
from sqlalchemy import func

from db_connection import session_maker, Event


def get_centroid(coordinates: list[list]) -> tuple:
    x = 0
    y = 0
    z = 0
    try:
        for lat, lon in coordinates:
            latitude = math.radians(lat)
            longitude = math.radians(lon)
            x += math.cos(latitude) * math.cos(longitude)
            y += math.cos(latitude) * math.sin(longitude)
            z += math.sin(latitude)
    except TypeError:
        return None, None

    total = len(coordinates)
    x /= total
    y /= total
    z /= total

    central_longitude = math.degrees(math.atan2(y, x))
    central_square_root = math.sqrt(x * x + y * y)
    central_latitude = math.degrees(math.atan2(z, central_square_root))

    return central_latitude, central_longitude


def get_average_by_area(model):
    with session_maker() as session:
        query = session.query(
            model.id, func.array_agg(func.json_build_array(Event.latitude, Event.longitude)).
            filter(Event.latitude.isnot(None), Event.longitude.isnot(None))) \
            .join(model.events) \
            .group_by(model.id).all()
    return {i[0]: get_centroid(i[1]) for i in query}
