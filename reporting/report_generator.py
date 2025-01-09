import logging
from typing import List

class ReportGenerator:
    def generate_report(self, data: List[dict]) -> str:
        try:
            report = "Report:\n"
            for item in data:
                report += f"{item}\n"
            logging.info("Report generated successfully.")
            return report
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            return "Error generating report."