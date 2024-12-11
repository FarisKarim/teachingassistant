"""Update User table

Revision ID: a152a6d48f23
Revises: 
Create Date: 2024-12-10 21:18:15.019224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a152a6d48f23'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_id', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_table('users')
    op.drop_index('ix_lessonplans_id', table_name='lessonplans')
    op.drop_table('lessonplans')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lessonplans',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('teacher_id', sa.INTEGER(), nullable=False),
    sa.Column('month', sa.INTEGER(), nullable=False),
    sa.Column('day', sa.INTEGER(), nullable=False),
    sa.Column('year', sa.INTEGER(), nullable=False),
    sa.Column('plan', sa.VARCHAR(), nullable=False),
    sa.ForeignKeyConstraint(['teacher_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_lessonplans_id', 'lessonplans', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), nullable=False),
    sa.Column('password', sa.VARCHAR(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_users_username', 'users', ['username'], unique=1)
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    # ### end Alembic commands ###