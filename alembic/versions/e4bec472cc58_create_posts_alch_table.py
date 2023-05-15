"""create posts_alch table

Revision ID: e4bec472cc58
Revises: 
Create Date: 2023-05-14 17:09:31.424712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4bec472cc58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("post_alch",sa.Column("id",sa.Integer(),nullable=False,primary_key=True),
                    sa.Column("title", sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("post_alch")
    pass
