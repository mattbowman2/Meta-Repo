# 🧩 Dev-Growth Context Manifest

## 1. User Profile & Constraints
* **Role:** Data Scientist.
* **Technical Interests:** Deep Learning, Graph Theory (GNNs, NetworkX), and Mathematical Optimization.
* **Workflow:** * **Weekdays:** 30-minute "Atomic" sessions after work.
    * **Weekends:** Deep-work sessions for complex implementation.
* **Preferred Stack:** Python (Jupyter for experimentation, scripts for automation), GitHub for portfolio tracking.
* **Psychology:** High value placed on **tactile progress**. Uses printed to-do lists to physically cross off tasks.

---

## 2. System Architecture: The "Meta-Repo"
The system treats self-development as a software project.
* **Database:** `ideas.yaml` stores all project ideas, metadata, and task breakdowns.
* **Logic:** A prioritization formula calculates which project to tackle next.
* **Execution:** LLMs are used to decompose large projects into 30-minute tasks.
* **Artifacts:** A Python script converts YAML tasks into a printable Markdown checklist.

---

## 3. The Prioritization Formula
Projects are ranked using a **Growth Score ($S$)**:

$$S = \frac{(Vibe \times 0.6) + (Impact \times 0.4)}{Effort}$$

* **Vibe (1-5):** Personal interest and "Coastal/Natural" aesthetic appeal.
* **Impact (1-5):** Career value and portfolio strength.
* **Effort (1, 3, 5):** 1=Small (Weekend), 3=Medium (1-2 weeks), 5=Large (Monthly).

---

## 4. `ideas.yaml` Schema Reference
```yaml
- id: UNIQUE_ID
  title: "Project Name"
  domain: "Graphs / Optimization / DL"
  vibe_score: 1-5
  impact_score: 1-5
  effort: "Small/Medium/Large"
  growth_score: Float
  status: "Backlog / Selected / In-Progress / Completed"
  data_strategy: "Synthetic / Online Dataset / Scraped"
  atomic_tasks:
    - "30-min Task 1"
    - "30-min Task 2"
```

---

## 5. Active LLM Prompt Templates

### A. For Task Decomposition (Atomic Tasks)
> "Based on the Project Title: [X] and Domain: [Y], break this down into 10-15 Atomic Tasks. Each task must be doable in 30 minutes, focus on Python implementation, and have a clear 'Definition of Done'. Format as a YAML list."

### B. For Idea Generation
> "Review my current `ideas.yaml` [PASTE CONTENT]. Suggest 5 new project ideas in the domains of Graphs and Optimization. Ensure each idea has a clear data-generating process or source. Provide vibe_score, impact_score, and effort level. Format as YAML."

---

## 6. Project History & Completed Work
* **Current Focus:** Building the system infrastructure (Scripts and Schema).
* **Future Goal:** Uploading individual project folders to GitHub with high-quality READMEs and reproducible notebooks.

---

### How to use this in a new chat:
**User:** *"I am starting a new project session. Here is my Context Manifest: [Paste the above]. I have selected the project 'Graph-Based Optimization' from my list. Please help me with Task 1."*