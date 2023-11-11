import pandas as pd
from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
    for _ in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10, 21, 200, 21)


pdf.output("output.pdf")
