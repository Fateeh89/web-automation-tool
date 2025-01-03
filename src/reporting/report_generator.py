from typing import Any
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import logging

logging.basicConfig(level=logging.INFO)

class ReportGenerator:
    """Generates reports in various formats."""

    def generate_xlsx_report(self, data: Any, template_path: str) -> None:
        """Generates an .xlsx report."""
        try:
            df = pd.DataFrame(data)
            df.to_excel(template_path, index=False)
            logging.info(f"XLSX report generated at {template_path}.")
        except Exception as e:
            logging.error(f"Failed to generate XLSX report: {e}")

    def generate_pdf_report(self, data: Any, output_path: str) -> None:
        """Generates a PDF report."""
        try:
            c = canvas.Canvas(output_path, pagesize=letter)
            width, height = letter
            c.drawString(100, height - 100, "Report")
            c.drawString(100, height - 120, str(data))
            c.save()
            logging.info(f"PDF report generated at {output_path}.")
        except Exception as e:
            logging.error(f"Failed to generate PDF report: {e}")