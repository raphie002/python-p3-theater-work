# lib/models.py
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, MetaData # type: ignore
from sqlalchemy.orm import relationship, backref # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

# --- Role Model ---
class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    character_name = Column(String())

    # Relationship to Audition (One Role to Many Auditions)
    auditions = relationship('Audition', backref=backref('role'))

    def __repr__(self):
        return f"Role(id={self.id}, " + \
            f"character_name='{self.character_name}')"

    @property
    def actors(self):
        """Returns a list of names from the actors associated with this role."""
        return [audition.actor for audition in self.auditions]

    @property
    def locations(self):
        """Returns a list of locations from the auditions associated with this role."""
        return [audition.location for audition in self.auditions]

    def lead(self):
        """
        Returns the first instance of the audition that was hired for this role
        or returns a string 'no actor has been hired for this role'.
        """
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        if hired_auditions:
            return hired_auditions[0]
        else:
            return 'no actor has been hired for this role'

    def understudy(self):
        """
        Returns the second instance of the audition that was hired for this role
        or returns a string 'no actor has been hired for understudy for this role'.
        """
        hired_auditions = [audition for audition in self.auditions if audition.hired]
        if len(hired_auditions) >= 2:
            return hired_auditions[1]
        else:
            return 'no actor has been hired for understudy for this role'

# --- Audition Model ---
class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean())
    # Foreign Key
    role_id = Column(Integer, ForeignKey('roles.id'))

    def __repr__(self):
        return f"Audition(id={self.id}, " + \
            f"actor='{self.actor}', " + \
            f"location='{self.location}', " + \
            f"phone={self.phone}, " + \
            f"hired={self.hired}, " + \
            f"role_id={self.role_id})"

    def call_back(self):
        """Changes the hired attribute to True."""
        self.hired = True