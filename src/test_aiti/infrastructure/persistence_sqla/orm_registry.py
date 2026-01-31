from sqlalchemy import MetaData
from sqlalchemy.orm import registry

metadata: MetaData = MetaData()
mapping_registry: registry = registry(metadata=metadata)
