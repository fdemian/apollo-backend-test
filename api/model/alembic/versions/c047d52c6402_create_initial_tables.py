"""create initial tables

Revision ID: c047d52c6402
Revises: 
Create Date: 2016-11-10 12:29:49.727398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c047d52c6402'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('avatar', sa.Text, nullable=False),
        sa.Column('username', sa.Unicode(100), nullable=False),
        sa.Column('fullname', sa.Unicode(255), nullable=False),
        sa.Column('email', sa.Unicode(255), nullable=False),
        sa.Column('password', sa.Text, nullable=True),
        sa.Column('valid', sa.Boolean, nullable=True),
    )

    op.create_table(
        'oauth_account',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('oauth_id', sa.Unicode(100), nullable=True),
        sa.Column('provider', sa.Unicode(30), nullable=False),
        sa.Column('user_id',  sa.Integer, sa.ForeignKey('users.id'))
    )

    op.create_table(
        'categories',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('name', sa.Unicode(50), nullable=False)
    )
              
    op.create_table(
        'stories',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('title', sa.Unicode(100), nullable=False),
        sa.Column('content', sa.Text, nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('category_id', sa.Integer, sa.ForeignKey('categories.id'))
    )
 
    op.create_table(
        'comments',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('author', sa.Unicode(100), nullable=True),
        sa.Column('content', sa.Text, nullable=False),
        sa.Column('avatar', sa.Text, nullable=False),
        sa.Column('url', sa.Text, nullable=False),
        sa.Column('story_id', sa.Integer, sa.ForeignKey('stories.id'))
    )


def downgrade():

    op.drop_table('comments')
    op.drop_table('categories')
    op.drop_table('stories')
    op.drop_table('oauth_account')
    op.drop_table('users')




