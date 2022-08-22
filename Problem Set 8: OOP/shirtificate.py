from fpdf import FPDF

class PDF():
    def __init__(self, name):
        # Set the pdf format to A4, which is 210mm wide by 297mm tall.
        self.pdf = FPDF(format = 'A4')

        self.pdf.add_page()

        # Position the header text, "CS50 Shirtificate", above the t-shirt in the pdf, center it, bold it, and set its font.
        self.pdf.set_font("helvetica", "B", 50)
        self.pdf.cell(0, 50, 'CS50 Shirtificate', new_x = 'LMARGIN', new_y= 'NEXT', align = 'c' )

        # Add the t-shirt png.
        self.pdf.image('shirtificate.png', w=self.pdf.epw)

        # Add text onto the front of the t-shirt in the pdf. Make this text white.
        self.pdf.set_text_color(255)
        self.pdf.set_font_size(28)
        self.pdf.text(x = 42, y = 125, txt = f'{name} took CS50')

    def save(self, name):
        self.pdf.output(name)


name = input('Name: ')
pdf = PDF(name)
pdf.save('shirtificate.pdf')
