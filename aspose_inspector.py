import aspose.words as aw
import json
import os

def inspect_document(doc_path):
    """Inspect a Word document's content and formatting using Aspose"""
    print(f"Opening document: {doc_path}")
    doc = aw.Document(doc_path)
    
    # Simple dictionary to store results
    results = {}
    
    # Print basic document info
    print("\nDocument Properties:")
    print(f"Page count: {doc.page_count}")
    
    # Get paragraphs
    paragraphs = doc.get_child_nodes(aw.NodeType.PARAGRAPH, True)
    paragraph_count = paragraphs.count
    print(f"Paragraph count: {paragraph_count}")
    
    # Print each paragraph's text and formatting
    print("\nParagraph Contents:")
    for i in range(paragraph_count):
        para = paragraphs[i].as_paragraph()
        text = para.get_text().strip()
        if text:  # Only print non-empty paragraphs
            print(f"\nParagraph {i}:")
            print(f"Text: {text}")
            print(f"Style: {para.paragraph_format.style.name}")
            
            # Get style font information
            style_font = para.paragraph_format.style.font
            print(f"Font Name: {style_font.name}")
            print(f"Font Size: {style_font.size}")
            print(f"Bold: {style_font.bold}")
            print(f"Italic: {style_font.italic}")
            
            # Store in results with formatting
            results[f"paragraph_{i}"] = {
                "text": text,
                "style": para.paragraph_format.style.name,
                "font": {
                    "name": style_font.name,
                    "size": style_font.size,
                    "bold": style_font.bold,
                    "italic": style_font.italic
                },
                "runs": []  # For individual run formatting
            }
            
            # Check individual runs for direct formatting
            for j, run in enumerate(para.runs):
                if run is not None:
                    run_info = {
                        "text": run.get_text(),
                        "font": {
                            "name": run.font.name,
                            "size": run.font.size,
                            "bold": run.font.bold,
                            "italic": run.font.italic
                        }
                    }
                    results[f"paragraph_{i}"]["runs"].append(run_info)
                    print(f"\n  Run {j}:")
                    print(f"  Text: {run.get_text()}")
                    print(f"  Font Name: {run.font.name}")
                    print(f"  Font Size: {run.font.size}")
                    print(f"  Bold: {run.font.bold}")
                    print(f"  Italic: {run.font.italic}")
    
    # Save results
    with open('doc_inspection.txt', 'w', encoding='utf-8') as f:
        f.write("Document Inspection Results\n")
        f.write("=========================\n\n")
        for para_key, para_data in results.items():
            f.write(f"{para_key}:\n")
            f.write(f"Text: {para_data['text']}\n")
            f.write(f"Style: {para_data['style']}\n")
            f.write(f"Font Name: {para_data['font']['name']}\n")
            f.write(f"Font Size: {para_data['font']['size']}\n")
            f.write(f"Bold: {para_data['font']['bold']}\n")
            f.write(f"Italic: {para_data['font']['italic']}\n")
            
            # Write run information
            for i, run in enumerate(para_data['runs']):
                f.write(f"\n  Run {i}:\n")
                f.write(f"  Text: {run['text']}\n")
                f.write(f"  Font Name: {run['font']['name']}\n")
                f.write(f"  Font Size: {run['font']['size']}\n")
                f.write(f"  Bold: {run['font']['bold']}\n")
                f.write(f"  Italic: {run['font']['italic']}\n")
            f.write("-" * 50 + "\n")

if __name__ == "__main__":
    # Get the latest document
    doc_dir = "generated_docs"
    files = [f for f in os.listdir(doc_dir) if f.endswith('.docx')]
    if not files:
        print("No .docx files found in generated_docs directory")
        exit(1)
        
    latest_file = max([os.path.join(doc_dir, f) for f in files], key=os.path.getctime)
    print(f"Inspecting file: {latest_file}")
    
    # Run inspection
    inspect_document(latest_file)
    print("\nInspection complete. Results saved to doc_inspection.txt")