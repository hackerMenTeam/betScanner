"""empty message

Revision ID: c7beb3cfb6ff
Revises: a05ead4a194e
Create Date: 2020-09-19 11:30:44.322649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7beb3cfb6ff'
down_revision = 'a05ead4a194e'
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
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('forks')
    op.drop_table('matches')
    # ### end Alembic commands ###