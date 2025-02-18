# Word Doc Automation

**Word Doc Automation** is a Python project that automates the generation of meeting minutes as a Microsoft Word document. The project leverages the [python-docx](https://python-docx.readthedocs.io/) library to work with Word files and the OpenAI API (using the GPT-3.5-turbo model) to generate meeting content based on a provided context.

## Overview

The project follows these main steps:

1. **Input Context:**  
   The meeting details (agenda, discussions, decisions, etc.) are provided via a pre-defined context in `context.py`. This context is used both as a prompt for generating a refined meeting minutes JSON and as a source of static content.

2. **Generating Meeting Minutes:**  
   The `main.py` script constructs a prompt using the meeting context and calls the OpenAI API to generate a JSON response. This JSON contains the meeting title, summary, key discussions, decisions, team assignments, and next meeting details. In case the API call fails, a default JSON is used.

3. **Template Creation and Filling:**  
   A Word template is created using `template.py`. This template includes placeholders (denoted by `{}`) for different sections like Meeting Summary, Key Discussions, Decisions, etc.  
   The function `fill_template_document` in `main.py` then reads the generated JSON content and replaces the placeholders in the template with the actual content.

4. **Output:**  
   The final filled-in Word document is saved in the `generated_docs` folder with a timestamped filename.

## Prerequisites

- **Python 3.6+**
- Install required Python packages:
  - `python-docx`
  - `openai`

  You can install these via pip:

  ```bash
  pip install python-docx openai
