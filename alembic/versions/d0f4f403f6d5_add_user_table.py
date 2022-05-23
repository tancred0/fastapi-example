"""add user table

Revision ID: d0f4f403f6d5
Revises: 8d53128f7c85
Create Date: 2022-05-22 16:11:09.508061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0f4f403f6d5'
down_revision = '8d53128f7c85'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'),nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')        
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
