
import json
import os
from logic.opening import Opening

DATA_FILE = "openings.json"

def get_local_storage():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return data
    except:
        return []

def save_local_storage(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_to_local_storage(opening_obj):
    # Convert opening object to dict structure that matches what constructors expect
    # or just raw data.
    # The JS app stored raw data: {width, height, serie, ...}
    
    data_list = get_local_storage()
    new_item = {
        "width": opening_obj.width,
        "height": opening_obj.height,
        "serie": opening_obj.serie,
        "color": opening_obj.color,
        "dvh": opening_obj.dvh,
        "preframe": opening_obj.preframe,
        "quantity": opening_obj.quantity
    }
    # Unshift (insert at beginning)
    data_list.insert(0, new_item)
    save_local_storage(data_list)


def clear_local_storage():
    save_local_storage([])

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(filename, title, content_text):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph(title, styles['Title']))
    story.append(Spacer(1, 12))

    # Content - splitting by newline to handle paragraphs
    for line in content_text.split('\n'):
        if line.strip():
            story.append(Paragraph(line, styles['BodyText']))
        else:
            story.append(Spacer(1, 6))

    doc.build(story)
