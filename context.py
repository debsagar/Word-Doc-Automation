MEETING_CONTEXT = """
Meeting Summary - Monday, 10th February 2025
Progress
The meeting primarily focused on chunking strategies for vector databases, covering different approaches and evaluating the best method for implementation. The team also discussed the broader project scope, emphasizing local implementation over cloud storage, prioritization of tasks, and onboarding new members.

Key Discussions & Findings
1. Understanding Vector Databases & Chunking Strategies
Context given: Chunking is essential for embedding textual data into a vector database for retrieval in AI models.
Different chunking methods were explored:
Character/Token-Based Chunking: Splits text based on a defined character or token size.
Recursive Chunking: Uses hierarchical separators like paragraph breaks for better structure.
Semantic Chunking: Groups text chunks based on meaning, ensuring contextual continuity.
Cluster Chunking & LLM Chunking: More advanced, novel methods.
Consensus: Recursive chunking appears efficient and widely used, making it a strong candidate for implementation.

2. Moving Towards a Local Implementation
Client Concern: Clients do not want their data going to external servers (privacy issue).
Decision:
Instead of hosting chunked data on S3, the approach will be modified to store and retrieve locally.
The system should still allow configuration for future cloud integration (if required).

3. Chunking for PDFs - Additional Considerations
Existing challenge: Chunking text-based documents is straightforward, but handling structured data like tables in PDFs is complex.
Observations:
Chunking typically ignores tables if structured text is used.
If the table is an image, it will be saved separately as an image file.
Decision:
Instead of reinventing chunking logic for PDFs, use open-source tools like Marker PDF or Unstructured to handle complex document structures.
Run sample PDFs through these tools to evaluate their output.

4. Project Prioritization & Task Allocation
Workload balancing:
The Word DOC agent project needs to be wrapped up this week.
The chunking strategy research can take slightly longer due to its complexity.
Plan:
Chunking strategy (PDFs & text): Continue R&D but also begin Word DOC agent implementation.
Anishi Raj will be shadowing Sagar Deb to ramp up on the project.

Next Steps & Action Items
✅ Sagar Deb
Continue evaluating Marker PDF & Unstructured for PDF chunking.
Modify chunking storage logic to work locally instead of using S3.
Collaborate with Anishi Raj and guide her on the project.
Prepare findings on chunking strategy for discussion.

✅ Aadarsh Bhalerao
Assist Sagar with logic tweaks for local implementation.
Ensure the Word DOC agent project remains on track.
Validate chunking strategy findings with real-world data.

✅ Deblin Chaudhuri
Provide feedback on chunking methodology once initial tests are complete.
Help refine query parameters for retrieval efficiency.

✅ Anishi Raj
Shadow Sagar Deb and familiarize herself with the chunking process.
Begin contributing to testing and validation.

Next Meeting
📅 Tentative Date: Mid-week check-in (12th or 13th February 2025)
📌 Agenda:
Review test results from Marker PDF & Unstructured.
Validate local storage changes for chunking.
Check progress on Word DOC agent.
This ensures R&D continues, while also making progress on high-priority deliverables. 🚀
"""

# Pre-generated JSON response
MEETING_JSON = {
    "title": "Meeting Summary - Monday, 10th February 2025",
    "summary": "The meeting focused on chunking strategies for vector databases, project scope, and onboarding new members.",
    "key_discussions": "1. Understanding Vector Databases & Chunking Strategies\n- Different chunking methods explored: Character/Token-Based, Recursive, Semantic, Cluster, LLM\n- Recursive chunking chosen for implementation efficiency.\n2. Moving Towards a Local Implementation\n- Decision to store and retrieve chunked data locally.\n- Future cloud integration configuration to be retained.\n3. Chunking for PDFs - Additional Considerations\n- Challenges with handling structured data like tables in PDFs.\n- Decision to use open-source tools like Marker PDF or Unstructured.\n4. Project Prioritization & Task Allocation\n- Wrap up Word DOC agent project this week.\n- Continue R&D on chunking strategy.",
    "decisions": "1. Use recursive chunking for vector databases.\n2. Store and retrieve chunked data locally.\n3. Utilize open-source tools for complex PDF structures.\n4. Prioritize Word DOC agent project and continue chunking strategy R&D.",
    "team_assignments": "✅ Sagar Deb - Evaluate Marker PDF & Unstructured, modify chunking storage, collaborate with Anishi Raj.\n✅ Aadarsh Bhalerao - Assist Sagar, ensure Word DOC project progress, validate chunking strategy.\n✅ Deblin Chaudhuri - Provide feedback on chunking methodology, refine query parameters.\n✅ Anishi Raj - Shadow Sagar, contribute to testing and validation.",
    "next_meeting": "📅 Tentative Date: Mid-week check-in (12th or 13th February 2025) 📌 Agenda: Review test results from Marker PDF & Unstructured, validate local storage changes for chunking, check Word DOC agent progress.",
    "generated_date": "2025-02-12"
} 