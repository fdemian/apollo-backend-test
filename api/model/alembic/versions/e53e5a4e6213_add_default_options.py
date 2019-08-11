"""Add default options

Revision ID: e53e5a4e6213
Revises: fe8905a69c8c
Create Date: 2019-06-09 22:46:55.028111

"""
from alembic import op
from sqlalchemy import orm, Column, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Redefine class
class GlobalConfiguration(Base):
    __tablename__ = 'global_configuration'

    key = Column(Text, primary_key=True, nullable=False)
    value = Column(Text, nullable=False)

# revision identifiers, used by Alembic.
revision = 'e53e5a4e6213'
down_revision = 'fe8905a69c8c'
branch_labels = None
depends_on = None

def upgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    # No comments allowed by default.
    config = GlobalConfiguration()
    config.key = "comments"
    config.value = "OFF"

    session.add(config)
    session.commit()


def downgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    all_configurations = session.query(GlobalConfiguration).all()
    for config in all_configurations:
        session.delete(config)

    session.commit()



