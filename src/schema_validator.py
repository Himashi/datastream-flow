import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class SchemaValidator:
    def __init__(self):
        # Mandatory fields required for relational persistence
        self.required_fields = {"timestamp", "level", "message"}

    def validate_payload(self, payload: Dict[str, Any]) -> bool:
        missing = self.required_fields - payload.keys()
        if missing:
            logging.error("Schema validation failed. Missing mandatory fields: %s", missing)
            return False
        
        if not isinstance(payload.get("level"), str) or not payload.get("message"):
            logging.error("Schema validation failed. Invalid data types or empty payload content.")
            return False
            
        logging.info("Schema validation passed successfully for record.")
        return True

if __name__ == "__main__":
    validator = SchemaValidator()
    sample_payload = {"timestamp": "2025-08-02 08:30:00", "level": "INFO", "message": "Data stream validated."}
    validator.validate_payload(sample_payload)