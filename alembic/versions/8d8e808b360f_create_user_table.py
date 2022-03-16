"""create user table

Revision ID: 8d8e808b360f
Revises: 479be9cc9a3b
Create Date: 2022-03-16 12:13:56.427249

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8d8e808b360f'
down_revision = '479be9cc9a3b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),
                              nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
