from flask import Flask, render_template, send_file
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Generate PDF route
@app.route("/generate")
def generate_report():
    # Read CSV file
    data = pd.read_excel("student_data.xlsx")

    total_rows = len(data)
    columns = list(data.columns)

    # Create PDF
    pdf = canvas.Canvas("report.pdf", pagesize=A4)
    pdf.setFont("Helvetica", 12)

    pdf.drawString(50, 800, "Automated Report Generation")
    pdf.drawString(50, 770, f"Total Records: {total_rows}")
    pdf.drawString(50, 740, f"Columns: {', '.join(columns)}")

    y = 700
    for col in columns:
        pdf.drawString(50, y, f"{col} - Sample Value: {data[col].iloc[0]}")
        y -= 20

    pdf.save()

    return send_file("report.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
