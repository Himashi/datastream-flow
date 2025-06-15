import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class DatabaseQueryOptimizer:
    def __init__(self, table_name: str):
        self.table_name = table_name

    def generate_optimized_index(self, column_name: str) -> str:
        index_query = f"CREATE INDEX CONCURRENTLY idx_{self.table_name}_{column_name} ON {self.table_name} ({column_name});"
        logging.info("Generated execution index query for table '%s'", self.table_name)
        return index_query

if __name__ == "__main__":
    optimizer = DatabaseQueryOptimizer("operational_logs")
    optimizer.generate_optimized_index("timestamp")