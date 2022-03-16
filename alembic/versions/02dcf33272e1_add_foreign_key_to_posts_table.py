"""add foreign key to posts table

Revision ID: 02dcf33272e1
Revises: 8d8e808b360f
Create Date: 2022-03-16 12:21:47.490039

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '02dcf33272e1'
down_revision = '8d8e808b360f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table='posts', referent_table='users', local_cols=['owner_id'],
                          remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_user_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
