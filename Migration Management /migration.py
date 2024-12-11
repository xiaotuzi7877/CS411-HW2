from typing import Any
from wildlife_tracker.migration_management.migration_path import MigrationPath


class Migration:
    def __init__(
        self,
        migration_id: int,
        migration_path: 'MigrationPath',
        current_date: str,
        current_location: str,
        status: str = "Scheduled"
    ) -> None:
        self.migration_id = migration_id
        self.migration_path = migration_path
        self.current_date = current_date
        self.current_location = current_location
        self.status = status

    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass
   
    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass
    