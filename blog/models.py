import uuid
from django.db import models
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
from datetime import datetime

# Create your models here.
class PostModel(DjangoCassandraModel):
    id =columns.UUID(primary_key=True, default=uuid.uuid4)
    title =columns.Text(required=True)
    body =columns.Text(required=True)
    created_at =columns.DateTime(default=datetime.now)
