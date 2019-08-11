"""create notifications table

Revision ID: b2e218bdc6a2
Revises: f65b7be13efa
Create Date: 2017-03-31 20:44:45.212045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2e218bdc6a2'
down_revision = 'f65b7be13efa'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'notifications',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('type', sa.Text, nullable=False),
        sa.Column('text', sa.Text, nullable=False),
        sa.Column('link', sa.Text, nullable=False),
        sa.Column('read', sa.Boolean, nullable=False)
    )


def downgrade():

    op.drop_table('notifications')
