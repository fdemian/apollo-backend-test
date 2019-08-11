"""Add configuration options for the application

Revision ID: fe8905a69c8c
Revises: 9091b003f105
Create Date: 2019-03-05 20:25:07.610987

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe8905a69c8c'
down_revision = '9091b003f105'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'global_configuration',
        sa.Column('key', sa.Text, primary_key=True, nullable=False),
        sa.Column('value', sa.Text, nullable=False)
    )


def downgrade():
    op.drop_table('global_configuration')

