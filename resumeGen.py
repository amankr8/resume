import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Step 1: Load JSON data from file
def load_resume_data():
    with open('resume.json', 'r') as file:
        return json.load(file)

# Step 2: Create the PDF from the JSON data
def create_resume(data):
    file_name = "resume.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Set up the title and personal info
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, height - 30, f"Resume: {data['basics']['name']}")
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 50, f"Email: {data['basics']['email']}")
    c.drawString(30, height - 70, f"Phone: {data['basics']['phone']}")
    c.drawString(30, height - 90, f"Location: {data['basics']['location']['address']}")
    c.drawString(30, height - 110, f"LinkedIn: {data['basics']['website']}")

    # Work Experience
    y_position = height - 150
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y_position, data['headings']['work'])
    y_position -= 20

    c.setFont("Helvetica", 12)
    for work in data['work']:
        c.drawString(30, y_position, f"{work['company']} ({work['location']})")
        y_position -= 15
        c.drawString(30, y_position, f"Position: {work['position']} | {work['startDate']} - {work['endDate']}")
        y_position -= 15
        for highlight in work['highlights']:
            c.drawString(30, y_position, f"- {highlight}")
            y_position -= 15

    # Education
    y_position -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y_position, data['headings']['education'])
    y_position -= 20

    c.setFont("Helvetica", 12)
    for edu in data['education']:
        c.drawString(30, y_position, f"{edu['institution']} ({edu['location']})")
        y_position -= 15
        c.drawString(30, y_position, f"{edu['studyType']} in {edu['area']} | GPA: {edu['gpa']}")
        y_position -= 15
        c.drawString(30, y_position, f"Duration: {edu['startDate']} - {edu['endDate']}")
        y_position -= 20

    # Skills
    y_position -= 10
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, y_position, data['headings']['skills'])
    y_position -= 20

    c.setFont("Helvetica", 12)
    for skill in data['skills']:
        c.drawString(30, y_position, f"{skill['name']}: {', '.join(skill['keywords'])}")
        y_position -= 15

    # Save the PDF
    c.save()

# Step 3: Load data and generate the resume
data = load_resume_data()
create_resume(data)
