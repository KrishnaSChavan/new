"""Add foreign key to post table

Revision ID: 6784a6cb0dbc
Revises: ba969894d5ed
Create Date: 2023-05-15 19:39:15.902525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6784a6cb0dbc'
down_revision = 'ba969894d5ed'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post_alch',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',source_table='post_alch',referent_table='users',
                           local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk',table_name="post_alch")
    op.drop_column('post_alch','owner_id')
    pass
