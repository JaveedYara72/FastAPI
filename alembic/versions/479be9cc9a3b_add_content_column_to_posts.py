"""add content column to posts

Revision ID: 479be9cc9a3b
Revises: 7f79eff0501e
Create Date: 2022-03-10 19:21:18.281088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '479be9cc9a3b'
down_revision = '7f79eff0501e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
