"""initial migration

Revision ID: 7f046f80f6c9
Revises: 
Create Date: 2018-03-15 19:10:41.263566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f046f80f6c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('PersonalGifCollection_user_id_fkey', 'PersonalGifCollection', type_='foreignkey')
    op.drop_column('PersonalGifCollection', 'user_id')
    op.drop_constraint('user_collection_user_id_fkey', 'user_collection', type_='foreignkey')
    op.create_foreign_key(None, 'user_collection', 'PersonalGifCollection', ['user_id'], ['id'])
    op.add_column('users', sa.Column('gifs', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'PersonalGifCollection', ['gifs'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'gifs')
    op.drop_constraint(None, 'user_collection', type_='foreignkey')
    op.create_foreign_key('user_collection_user_id_fkey', 'user_collection', 'users', ['user_id'], ['id'])
    op.add_column('PersonalGifCollection', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('PersonalGifCollection_user_id_fkey', 'PersonalGifCollection', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###
