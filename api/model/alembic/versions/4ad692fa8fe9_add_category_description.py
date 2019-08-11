"""add category description

Revision ID: 4ad692fa8fe9
Revises: 8573e754d7a5
Create Date: 2017-08-27 20:42:15.102230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ad692fa8fe9'
down_revision = '8573e754d7a5'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('categories', sa.Column('description', sa.Text))

def downgrade():
    op.drop_column('categories', 'description')