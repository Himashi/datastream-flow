import time
import logging
from src.ingestion_engine import LogIngestionEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class BenchmarkProfiler:
    def __init__(self, total_records: int = 1000):
        self.total_records = total_records
        self.engine = LogIngestionEngine()

    def run_throughput_benchmark(self):
        logging.info("Starting ingestion throughput benchmark for %d records...", self.total_records)
        sample_log = "2025-07-25 10:00:00 INFO Benchmark record payload processing test."
        
        start_time = time.time()
        for _ in range(self.total_records):
            self.engine.parse_raw_log(sample_log)
        duration = time.time() - start_time
        
        throughput = self.total_records / duration if duration > 0 else 0
        logging.info("Benchmark complete. Processed %d records in %.4f seconds (%.2f logs/sec).", 
                     self.total_records, duration, throughput)
        return throughput

if __name__ == "__main__":
    profiler = BenchmarkProfiler(total_records=5000)
    profiler.run_throughput_benchmark()