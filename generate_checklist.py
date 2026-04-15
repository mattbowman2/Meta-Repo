import yaml
import os
from datetime import datetime

def generate_printable_list():
    if not os.path.exists('ideas.yaml'):
        print("Error: ideas.yaml not found.")
        return

    with open('ideas.yaml', 'r') as f:
        projects = yaml.safe_load(f)

    # Find the project currently marked as 'In-Progress'
    active_project = next((p for p in projects if p.get('status') == 'In-Progress'), None)

    if not active_project:
        print("No project currently marked as 'In-Progress'.")
        return

    # Create the Markdown Content
    title = active_project.get('title', 'Project')
    tasks = active_project.get('atomic_tasks', [])
    
    md_content = f"# 📝 Weekly Sprint: {title}\n"
    md_content += f"*Generated on: {datetime.now().strftime('%Y-%m-%d')}*\n\n"
    md_content += "## 30-Minute Daily Tasks\n"
    
    if not tasks:
        md_content += "_No tasks found. Use the LLM Prompt to generate some!_\n"
    else:
        for task in tasks:
            md_content += f"- [ ] {task}\n"

    md_content += "\n---\n"
    md_content += "### ✍️ Notes / Reflections\n"
    md_content += "(Use this space to jot down breakthroughs or bugs encountered during your 30 mins)\n\n\n"

    # Save to file
    with open('PRINT_ME.md', 'w') as f:
        f.write(md_content)
    
    print("✅ Success! 'PRINT_ME.md' has been generated. Open and print it.")

if __name__ == "__main__":
    generate_printable_list()