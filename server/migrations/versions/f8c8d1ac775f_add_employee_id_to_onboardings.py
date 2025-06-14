"""Add employee_id to onboardings

Revision ID: f8c8d1ac775f
Revises: 14d5ac444aac
Create Date: 2025-06-14 06:16:57.056648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8c8d1ac775f'
down_revision = '14d5ac444aac'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            None,
            'employees',
            ['employee_id'],
            ['id']
        )



def downgrade():
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('employee_id')
