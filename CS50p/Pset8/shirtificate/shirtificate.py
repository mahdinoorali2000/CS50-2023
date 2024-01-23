from fpdf import FPDF

class took(FPDF):
    def a(self):
        self.image("shirtificate.png", x=20, y=60)
        self.set_font("Times", "B", size=36)
        self.text(45, 45, "CS50 shirtificate")

    def b(self):
        self.set_font("Times", "B", size=36)
        self.set_text_color(255,255,255)
        self.text(45, 45, x + "I took CS50")

x = input("What's your name? ")
file = took()
file.add_page()
file.output("shirtificate.pdf")
