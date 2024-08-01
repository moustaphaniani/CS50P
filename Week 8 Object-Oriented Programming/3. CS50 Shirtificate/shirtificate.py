from fpdf import FPDF

def main():
    # Ask user for name
    name = input("Name: ")
    # Logic of the program
    pdf = FPDF()
    pdf.add_page(orientation='P', format='a4')
    pdf.image('shirtificate.png', x=10, y=60, w=190)
    pdf.set_font('helvetica', 'B', size=42)
    pdf.cell(w=190, h=40, text='CS50 Shirtificate', center=True, align='C')
    pdf.set_font('helvetica', 'B', size=24)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(w=190, h=230, text=f"{name} took CS50", center=True, align='C')
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
