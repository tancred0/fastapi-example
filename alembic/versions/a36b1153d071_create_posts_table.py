"""create posts table

Revision ID: a36b1153d071
Revises: 
Create Date: 2022-05-22 15:59:08.778516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a36b1153d071'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", 
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('tile', sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
