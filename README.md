# YouTubeCompare : Comparing Science Communication on YouTube

This repository contains the code and analysis for our DH‑500 project at EPFL. We studied how **institutional YouTube channels** (EPFL, ETH Zürich, MIT, Stanford) differ from **independent science creators** (3Blue1Brown, Kurzgesagt, Walter Lewin, minutephysics) in the way they communicate science and how audiences respond to them.

Our dataset includes **8,742 videos** published between **2008 and 2025**, collected through the YouTube Data API.  
We looked at engagement, video format, title vocabulary, thumbnail style, and how these elements evolved over time.

---


## Dataset

We collected public metadata from the YouTube Data API. Here is the link to it: 
For each video, we kept:

- title, description, tags  
- publication date  
- duration  
- views, likes, comments  
- thumbnails (default + high‑res)  
- channel information  

Only public data was used, and no user‑level information was collected




---

## Repository structure





---



## What we analyzed

### Video format & style
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

This allowed us to compare visual styles across all 9,568 thumbnails

---

## Key findings 

- Independent creators consistently achieve **higher engagement**
- Institutional channels have shifted from long lectures to **shorter, more focused videos**
- Independent channels use **catchier titles** (questions, numbers, hooks), while institutions stay more factual 
- Thumbnails differ strongly: independents lean toward **illustration and high visual impact**, institutions toward **faces, lectures, and stock photography**
- Visual clustering clearly separates the two groups

---
