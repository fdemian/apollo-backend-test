"""add tags support

Revision ID: 8573e754d7a5
Revises: b2e218bdc6a2
Create Date: 2017-04-11 13:46:57.091655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8573e754d7a5'
down_revision = 'b2e218bdc6a2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('stories', sa.Column('tags', sa.Text, nullable=True))


def downgrade():
    op.drop_column('stories', 'tags')
