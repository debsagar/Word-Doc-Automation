from docx import Document
from docx.shared import Pt
import openai
from datetime import datetime
import os
from context import MEETING_CONTEXT, MEETING_JSON
import json

# Set your OpenAI API key
openai.api_key = ""

def get_llm_response(context):
    """
    Get response from pre-generated JSON
    """
    prompt = f"""
    Create a meeting minutes document from the given context.
    Return a simple JSON object with single-line string values for each key.
    Do not use nested objects or arrays.

    Context: {context}

    Required format (example):
    {{
        "title": "Vector Database Meeting - February 10, 2025",
        "summary": "Single paragraph summary of the meeting...",
        "key_discussions": "Bullet-pointed list written as a single string with \\n for line breaks",
        "decisions": "List of decisions as a single string with \\n for line breaks",
        "team_assignments": "List of team assignments as a single string with \\n for line breaks",
        "next_meeting": "Next meeting details as a single line",
        "generated_date": "2024-02-12"
    }}

    Keep each value as a single string, using \\n for line breaks where needed.
    Do not use nested JSON structures.
    """
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional meeting minutes writer. Return a simple JSON with string values only."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500
        )
        
        content = json.loads(response.choices[0].message.content)
        print("LLM Response:", json.dumps(content, indent=2))  # Debug print
        return content
        
    except Exception as e:
        print(f"Error generating content: {e}")
        return {
            "title": "Meeting Title and Date",
            "summary": "Meeting Summary",
            "key_discussions": "Key Discussion Points",
            "decisions": "Action Items",
            "team_assignments": "Team Assignments",
            "next_meeting": "Next Meeting Details",
            "generated_date": datetime.now().strftime("%Y-%m-%d")
        }

def fill_template_document(template_path, context, save_as):
    """
    Fill template document with LLM-generated content
    """
    os.makedirs('generated_docs', exist_ok=True)
    doc = Document(template_path)
    
    content = MEETING_JSON
    print("Content loaded:", content)
    
    # Fill in the document
    paragraphs = list(doc.paragraphs)  # Convert to list for easier indexing
    for i, paragraph in enumerate(paragraphs):
        text = paragraph.text
        print(f"Processing paragraph: '{text}'")
        
        if text == "{}":
            # Get the previous paragraph's text
            prev_text = paragraphs[i-1].text if i > 0 else ""
            print(f"Previous paragraph: '{prev_text}'")
            
            if "Meeting Summary" in prev_text:
                paragraph.text = content['summary']
            elif "Key Discussions & Findings" in prev_text:
                paragraph.text = content['key_discussions']
            elif "Decisions and Action Items" in prev_text:
                paragraph.text = content['decisions']
            elif "Team Assignments" in prev_text:
                paragraph.text = content['team_assignments']
            elif "Next Meeting" in prev_text:
                paragraph.text = content['next_meeting']
        elif "Meeting Title and Date:" in text:
            paragraph.text = content['title']
        elif "Generated on:" in text:
            paragraph.text = f"Generated on: {content['generated_date']}"
    
    save_path = os.path.join('generated_docs', save_as)
    doc.save(save_path)
    return save_path

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"filled_document_{timestamp}.docx"
    
    filled_doc = fill_template_document(
        template_path="template.docx",
        context=MEETING_CONTEXT,
        save_as=filename
    )
    print(f"Document created successfully: {filled_doc}")

if __name__ == "__main__":
    main()