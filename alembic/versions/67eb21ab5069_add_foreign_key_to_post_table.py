"""add foreign key to post table

Revision ID: 67eb21ab5069
Revises: d0f4f403f6d5
Create Date: 2022-05-22 16:17:33.143743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67eb21ab5069'
down_revision = 'd0f4f403f6d5'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts', 
        sa.Column('owner_id', sa.Integer(), nullable=False)
    )
    op.create_foreign_key(
        'posts_users_fk', 
        source_table="posts",
        referent_table="users",

        local_cols=['owner_id'],
        remote_cols=['id'],

        ondelete='CASCADE'
    )

    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column("posts", "owner_id")
    pass
