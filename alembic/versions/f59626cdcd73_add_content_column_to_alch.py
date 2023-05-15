"""add content column to alch

Revision ID: f59626cdcd73
Revises: e4bec472cc58
Create Date: 2023-05-15 17:41:48.244219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f59626cdcd73'
down_revision = 'e4bec472cc58'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post_alch',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('post_alch','content')
    pass
