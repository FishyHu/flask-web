"""empty message

Revision ID: 6d53a665a35d
Revises: a7a335f37d3d
Create Date: 2020-10-30 15:07:37.102196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d53a665a35d'
down_revision = 'a7a335f37d3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('posts_writer_id_fkey', 'posts', type_='foreignkey')
    op.drop_column('posts', 'writer_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('writer_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('posts_writer_id_fkey', 'posts', 'writer', ['writer_id'], ['id'])
    # ### end Alembic commands ###