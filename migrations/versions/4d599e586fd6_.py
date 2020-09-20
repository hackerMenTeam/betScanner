"""empty message

Revision ID: 4d599e586fd6
Revises: 652462ba52fa
Create Date: 2020-09-18 16:26:22.097224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d599e586fd6'
down_revision = '652462ba52fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookmakers', 'is_enabled',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('bookmakers', 'url',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('bookmakers', 'vpn_required',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.create_unique_constraint(None, 'bookmakers', ['url'])
    op.create_unique_constraint(None, 'bookmakers', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'bookmakers', type_='unique')
    op.drop_constraint(None, 'bookmakers', type_='unique')
    op.alter_column('bookmakers', 'vpn_required',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('bookmakers', 'url',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('bookmakers', 'is_enabled',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###