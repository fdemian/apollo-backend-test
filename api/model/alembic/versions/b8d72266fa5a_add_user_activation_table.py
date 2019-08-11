"""Add user activation table

Revision ID: b8d72266fa5a
Revises: c047d52c6402
Create Date: 2017-02-21 21:25:39.251796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8d72266fa5a'
down_revision = 'c047d52c6402'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'user_activation',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('code', sa.Text, nullable=False),
    )


def downgrade():

    op.drop_table('user_activation')
