"""remove vote

Revision ID: 5bcc397b5fac
Revises: 01c00b25ee10
Create Date: 2023-09-26 13:27:50.560910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bcc397b5fac'
down_revision = '01c00b25ee10'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post_alch.id'], name='votes_post_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='votes_user_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id', name='votes_pkey')
    )
    # ### end Alembic commands ###
