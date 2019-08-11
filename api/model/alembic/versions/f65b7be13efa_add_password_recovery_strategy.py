"""Add password recovery strategy.

Revision ID: f65b7be13efa
Revises: b8d72266fa5a
Create Date: 2017-02-23 20:56:46.422122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f65b7be13efa'
down_revision = 'b8d72266fa5a'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'password_change_requests',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('reset_token', sa.Text, nullable=False),
        sa.Column('time', sa.DateTime),
        sa.Column('user_id',  sa.Integer, sa.ForeignKey('users.id'), nullable=False)
    )


def downgrade():

    op.drop_table('password_change_requests')
