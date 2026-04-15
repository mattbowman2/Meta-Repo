# 📚 Project: Knowledge Graph for Personal Reading
**Goal:** Build a graph-based representation of technical books and research papers to identify intersections in learning.

- [ ] **Task 1: Environment Setup** Install `networkx`, `spacy`, `pandas`, and `matplotlib`. Download the medium-sized English NLP model (`python -m spacy download en_core_web_md`). (30 min)

- [ ] **Task 2: Data Schema Definition** Create a `library_data.yaml` or CSV file. Define headers: `Title`, `Author`, `Technical_Domain`, `Key_Concepts`, and `Summary_Text`. (30 min)

- [ ] **Task 3: Seed Data Entry** Manually populate your file with 5–10 recent technical books or papers you have read. Ensure the `Summary_Text` contains at least 3–4 sentences per entry. (30 min)

- [ ] **Task 4: NLP Pipeline - Initialization** Write a Python script to load your data and process the `Summary_Text` field using the Spacy pipeline to tokenize and tag parts of speech. (30 min)

- [ ] **Task 5: NLP Pipeline - Keyword Extraction** Implement logic to extract "Noun Phrases" or entities related to technical concepts. Filter out common English stop words. (30 min)

- [ ] **Task 6: Graph Initialization** Initialize a NetworkX `Graph()` object. Define a mapping for node colors (e.g., Blue for 'Book', Green for 'Topic'). (30 min)

- [ ] **Task 7: Node and Edge Ingestion** Iterate through the processed data. Add a node for each book and a node for each extracted keyword. Create edges connecting Books to their relevant Topics. (30 min)

- [ ] **Task 8: Relational Logic Expansion** Create "Similarity Edges" between Book nodes if they share more than 50% of the same technical keywords. (30 min)

- [ ] **Task 9: Centrality Analysis** Calculate "Degree Centrality" for all Topic nodes. Print a list of the top 5 "Bridge" concepts that connect different domains in your reading. (30 min)

- [ ] **Task 10: Basic Visualization** Use `matplotlib` and `networkx.draw` with a `spring_layout` to generate a static plot of the graph in a Jupyter Notebook. (30 min)

- [ ] **Task 11: Vector Similarity (Exploration)** Use Spacy's `.similarity()` method to compare the vectors of different summaries. Add weighted edges to the graph based on semantic similarity scores. (30 min)

- [ ] **Task 12: Interactive Export** Use the `pyvis` library to export your graph as an interactive `.html` file that allows for zooming and node-dragging in a browser. (30 min)

- [ ] **Task 13: Documentation & GitHub Ready** Refactor your code into a single script, add comments, and draft a `README.md` explaining how the graph helps visualize your learning journey. (30 min)