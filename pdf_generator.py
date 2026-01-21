from fpdf import FPDF
from datetime import datetime


def generate_pdf(summary, action_items, sentiment, output_path="Minutes_of_Meeting.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Minutes of Meeting", ln=True)

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 8, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    pdf.ln(5)

    # Summary
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Summary", ln=True)

    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, summary)

    pdf.ln(3)

    # Action Items
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Action Items", ln=True)

    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, action_items)

    pdf.ln(3)

    # Sentiment
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Sentiment & Emotion Analysis", ln=True)

    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, sentiment)

    pdf.output(output_path)
    return output_path
