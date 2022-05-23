"""create content column to posts table

Revision ID: 8d53128f7c85
Revises: a36b1153d071
Create Date: 2022-05-22 16:06:43.517844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d53128f7c85'
down_revision = 'a36b1153d071'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
