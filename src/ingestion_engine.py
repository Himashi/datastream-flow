import logging
import re
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class LogIngestionEngine:
    def __init__(self):
        # Standard pattern matching for enterprise server logs
        self.log_pattern = re.compile(
            r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(?P<level>\w+)\s+(?P<message>.*)'
        )

    def parse_raw_log(self, raw_line: str) -> Dict[Any, Any]:
        match = self.log_pattern.match(raw_line.strip())
        if match:
            parsed = match.groupdict()
            logging.info("Successfully parsed log level: %s", parsed['level'])
            return parsed
        logging.warning("Failed to parse raw log line structure.")
        return {"timestamp": None, "level": "UNKNOWN", "message": raw_line}

if __name__ == "__main__":
    engine = LogIngestionEngine()
    sample_log = "2025-06-15 14:22:10 INFO Database connection pool established successfully."
    engine.parse_raw_log(sample_log)