"""empty message

Revision ID: efca1cd4f2a1
Revises: 
Create Date: 2017-12-08 15:52:46.390446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efca1cd4f2a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entry', sa.Column('status', sa.SmallInteger(), server_default='0'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('entry', 'status')
    # ### end Alembic commands ###
