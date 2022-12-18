"""Create posts tables

Revision ID: 078c16d50d46
Revises: 
Create Date: 2022-12-18 18:18:29.440495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '078c16d50d46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts", referent_table="users", local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
