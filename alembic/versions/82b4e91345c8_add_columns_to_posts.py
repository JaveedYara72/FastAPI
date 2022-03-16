"""add columns to posts

Revision ID: 82b4e91345c8
Revises: 02dcf33272e1
Create Date: 2022-03-16 12:26:07.659460

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '82b4e91345c8'
down_revision = '02dcf33272e1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
