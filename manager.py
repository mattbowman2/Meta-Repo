import yaml
import os

def calculate_score(vibe, impact, effort_val):
    # Higher score = Better to do now
    # Effort: 1 (Small), 3 (Medium), 5 (Large)
    return round(((vibe * 0.6) + (impact * 0.4)) / effort_val, 2)

def add_idea():
    title = input("Project Title: ")
    domain = input("Domain (Graphs/Optimization/DL): ")
    vibe = int(input("Vibe Score (1-5): "))
    impact = int(input("Career Impact (1-5): "))
    effort = input("Effort (Small/Medium/Large): ")
    
    effort_map = {"Small": 1, "Medium": 3, "Large": 5}
    score = calculate_score(vibe, impact, effort_map.get(effort, 3))
    
    new_idea = {
        "title": title,
        "domain": domain,
        "vibe_score": vibe,
        "impact_score": impact,
        "effort": effort,
        "growth_score": score,
        "status": "Backlog",
        "atomic_tasks": []
    }
    
    # Load and save
    if os.path.exists('ideas.yaml'):
        with open('ideas.yaml', 'r') as f:
            data = yaml.safe_load(f) or []
    else:
        data = []
        
    data.append(new_idea)
    with open('ideas.yaml', 'w') as f:
        yaml.dump(data, f, sort_keys=False)
    print(f"\n✅ Added '{title}' with a Growth Score of {score}")

if __name__ == "__main__":
    add_idea()