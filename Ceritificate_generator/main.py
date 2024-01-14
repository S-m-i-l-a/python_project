from PIL import Image, ImageDraw, ImageFont

def generate_signature_line(draw, position):
    # Generate a simple line as a signature
    draw.line([position, (position[0] + 100, position[1])], fill="white", width=2)

def generate_certificate(template_path, output_path):
    # Get user input
    participant_name = input("Enter Participant's Name: ")
    course_name = input("Enter Course Name: ")
    completion_date = input("Enter Date of Completion: ")

    authority_name = "Authority Name\nDr. Smith"
    instructor_name = "Instructor Name\nProf. Johnson"

    # Open the template image
    template = Image.open(template_path)

    # Set the font sizes
    participant_name_font_size = 30
    other_text_font_size = 18
    signature_font_size = 20
    congrats_font_size = 24

    # Load fonts with specified sizes
    participant_name_font = ImageFont.load_default().font_variant(size=participant_name_font_size)
    other_text_font = ImageFont.load_default().font_variant(size=other_text_font_size)
    signature_font = ImageFont.load_default().font_variant(size=signature_font_size)
    congrats_font = ImageFont.load_default().font_variant(size=congrats_font_size)

    # Create a drawing object
    draw = ImageDraw.Draw(template)

    # Calculate text positions (adjust as needed)
    congrats_position = (400, 140)
    participant_name_position = (420, 260)
    course_name_position = (370, 310)
    completion_date_position = (350, 360)
    authority_signature_position = (170, 460)
    instructor_signature_position = (600, 460)

    # Add "Congratulations" section
    draw.text(congrats_position, "Congratulations!", fill="white", font=congrats_font)

    # Add participant name, course name, and completion date to the certificate
    draw.text(participant_name_position, participant_name, fill="white", font=participant_name_font)
    draw.text(course_name_position, f"Course: {course_name}", fill="white", font=other_text_font)
    draw.text(completion_date_position, f"Completion Date: {completion_date}", fill="white", font=other_text_font)

    # Add signature lines for authority and instructor
    generate_signature_line(draw, authority_signature_position)
    generate_signature_line(draw, instructor_signature_position)

    # Add signature labels with newlines
    draw.text((170, 480), f"{authority_name}", fill="white", font=other_text_font)
    draw.text((590, 480), f"{instructor_name}", fill="white", font=other_text_font)

    # Add declaration text
    declaration_text = "This is to certify that"
    declaration_position = (400, 220)
    draw.text(declaration_position, declaration_text, fill="white", font=other_text_font)

    # Save the generated certificate
    template.save(output_path)


if __name__ == "__main__":
    # Example usage
    template_path = "certificate_template.png"
    output_path = "output_certificate.png"

    generate_certificate(template_path, output_path)
