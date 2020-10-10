"""empty message

Revision ID: 53d0fad22d78
Revises: c76ac69798ed
Create Date: 2020-10-10 18:26:12.488286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53d0fad22d78'
down_revision = 'c76ac69798ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'matches', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'matches', type_='unique')
    # ### end Alembic commands ###
