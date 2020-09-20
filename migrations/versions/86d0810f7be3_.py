"""empty message

Revision ID: 86d0810f7be3
Revises: d4a3fe6c663e
Create Date: 2020-09-18 15:22:02.508173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86d0810f7be3'
down_revision = 'd4a3fe6c663e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('matches',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('bookmaker_id', sa.Integer(), nullable=True),
    sa.Column('match_title', sa.VARCHAR(), nullable=False),
    sa.Column('sport_kind', sa.VARCHAR(), nullable=False),
    sa.Column('championship', sa.VARCHAR(), nullable=False),
    sa.Column('k1', sa.Float(), nullable=False),
    sa.Column('k2', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['bookmaker_id'], ['bookmakers.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('forks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('major_bet', sa.Integer(), nullable=True),
    sa.Column('minor_bet', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['major_bet'], ['matches.id'], ),
    sa.ForeignKeyConstraint(['minor_bet'], ['matches.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
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
    op.drop_table('forks')
    op.drop_table('matches')
    # ### end Alembic commands ###