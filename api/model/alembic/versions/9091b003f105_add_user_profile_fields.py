"""Add user profile fields

Revision ID: 9091b003f105
Revises: f46a80bc4a52
Create Date: 2018-12-22 13:38:56.388370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9091b003f105'
down_revision = 'f46a80bc4a52'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('users', sa.Column('signature', sa.Unicode(255), nullable=True))
    op.add_column('users', sa.Column('about', sa.Unicode(255), nullable=True))
    return

def downgrade():
    op.drop_column('users', 'signature')
    op.drop_column('users', 'about')
