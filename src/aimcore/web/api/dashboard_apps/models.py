import uuid
import sqlalchemy as sa

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr

from aimcore.web.api.db import Base
from aim._sdk.utils import utc_now


class AppMixin(object):
    uuid = sa.Column(sa.Text, primary_key=True)

    created_at = sa.Column(sa.DateTime, default=utc_now)
    updated_at = sa.Column(sa.DateTime, default=utc_now, onupdate=utc_now)
    is_archived = sa.Column(sa.Boolean, default=False)

    @declared_attr
    def dashboard_id(cls):
        return sa.Column('dashboard_id', sa.ForeignKey('dashboards.uuid'))

    @declared_attr
    def dashboard(cls):
        return relationship("Dashboard")


class ExploreState(AppMixin, Base):
    __tablename__ = 'explore_states'

    type = sa.Column(sa.Text, nullable=False)
    state = sa.Column(sa.Text)

    def __init__(self):
        self.uuid = str(uuid.uuid1())
        self.is_archived = False
