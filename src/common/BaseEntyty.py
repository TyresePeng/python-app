import datetime

class BaseEntyty:
    def model_to_dict(self):
        """Convert SQLAlchemy model instance to dictionary."""
        result = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            if isinstance(value, datetime.datetime):
                result[column.name] = value.isoformat()  # Convert datetime to ISO format string
            else:
                result[column.name] = value
        return result
