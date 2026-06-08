# YouTubeCompare : A Comparative Study of Content and Audience Engagement

This repository contains the code and analysis for our DH‑500 project at EPFL. We studied how **institutional YouTube channels** (EPFL, ETH Zürich, MIT, Stanford) differ from **independent science creators** (3Blue1Brown, Kurzgesagt, Walter Lewin, minutephysics) in the way they communicate science and how audiences respond to them.

Our dataset includes **8,742 videos** published between **2008 and 2025**, collected through the YouTube Data API.  

The different analysis perfomed focus on the following research question :<br> 
*How does scientific content perform on YouTube depending on who produces it, and what distinguishes the communication strategies of the two groups?*

Rather than treating popularity as a measure of scientific quality, we study it as an outcome of communication style. Thus, the analysis examines factors such as engagement, video format, title vocabulary, thumbnail style, and how these elements evolved over time.

---


## Dataset

We collected public metadata from the YouTube Data API. Here is the link to it: https://go.epfl.ch/CSM_data_group1

For each video, we kept:

- title, description, tags  
- publication date  
- duration  
- views, likes, comments  
- thumbnails (default + high‑res)  
- channel information  

Only public data was used, and no user‑level information was collected.




---

## Repository structure
```
YouTubeCompare/
├── README.md
├── analysis/
│   ├── person1_format_style/
│   │   ├── visualizations/        
│   │   └── notebook.ipynb
│   ├── person2_titles_thumbnails/
│   │   ├── output/               
│   │   ├── 01_title_features.ipynb
│   │   ├── 02_thumbnail_download.ipynb
│   │   ├── 03_thumbnail_analysis.ipynb
│   │   ├── 04_correlation_engagement.ipynb
│   │   ├── 05_advanced_thumbnail_analysis.ipynb
│   │   └── 06_temporal_thumbnail_analysis.ipynb
│   └── person3_evolution/
│       ├── text_analysis/
│       │   └── title_analysis.ipynb
│       ├── visualizations/        
│       └── engagement_comparison.ipynb
└── shared/
    ├── config.py
    └── preprocessing.ipynb          

```


- **`shared/`** — Shared configuration and preprocessing.
  Run `preprocessing.ipynb` once after downloading the raw dataset to
  generate the preprocessed data used by all analyses. `config.py` holds
  common settings (paths, channel groups, color palette).

- **`analysis/person1_format_style/`** — Format and style analysis.
  Figures in `visualizations/`.

- **`analysis/person2_titles_thumbnails/`** — Title and thumbnail analysis,
  run notebooks `01`–`06` in order. Generated files go to `output/`.

- **`analysis/person3_evolution/`** — Temporal evolution of titles and
  engagement. Text analysis in `text_analysis/`, figures in `visualizations/`.

---

## What we analyzed

### Video format and style
We compared:

- video duration  
- title length  
- description length  
- presence of links and call‑to‑action keywords  
- how these changed over time  

### Title vocabulary
We tokenized all titles and compared:

- most frequent words  
- attention‑grabbing features (questions, numbers, hooks)  
- differences in framing between institutional and independent channels  

### Thumbnail analysis
We used a mix of:

- low‑level image features (brightness, contrast, saturation…)  
- CLIP zero‑shot classification  
- BLIP captioning and VQA  
- structured annotation with a vision‑language model  
- DINOv2 embeddings + UMAP + clustering  

This allowed us to compare visual styles across all thumbnails.

---

## Key findings 
- Independent creators consistently achieve **higher engagement**
- Institutional channels have shifted from long lectures to **shorter, more focused videos**
- Independent channels use **catchier titles** (questions, numbers, hooks), while institutions stay more factual 
- Thumbnails differ strongly: independents lean toward **illustration and high visual impact**, institutions toward **faces, lectures, and stock photography**
- Visual clustering clearly separates the two groups

---
