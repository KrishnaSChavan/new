"""Add published and time post table

Revision ID: 4669334e8e78
Revises: 6784a6cb0dbc
Create Date: 2023-05-15 19:56:48.297163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4669334e8e78'
down_revision = '6784a6cb0dbc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post_alch', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE') ,)
    op.add_column('post_alch', sa.Column('created_at', sa.TIMESTAMP (timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('post_alch','published')
    op.drop_column('post_alch','created_at')
    
    pass
