"""Add failed login attempts column.

Revision ID: f46a80bc4a52
Revises: 4ad692fa8fe9
Create Date: 2018-05-01 21:35:40.082452

"""
from alembic import op
from sqlalchemy import Column, Integer, DateTime


# revision identifiers, used by Alembic.
revision = 'f46a80bc4a52'
down_revision = '4ad692fa8fe9'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('users', Column('failed_attempts', Integer, nullable=False, server_default='0'))
    op.add_column('users', Column('lockout_time', DateTime, nullable=True))

def downgrade():
    op.drop_column('users', 'failed_attempts')
    op.drop_column('users', 'lockout_time')