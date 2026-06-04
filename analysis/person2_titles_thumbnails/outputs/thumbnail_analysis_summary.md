# Thumbnail Analysis Summary

The analysis covers **9,568 thumbnails** across 8 channels (4 independent: 3Blue1Brown, Kurzgesagt, Walter Lewin, minutephysics; 4 institutional: EPFL, ETH Zürich, MIT, Stanford), using a four-tier pipeline.

---

## Tier 1 — OpenCV Low-Level Visual Features (all 9,568 thumbnails)

Six pixel-level metrics were extracted: brightness, contrast, saturation, colorfulness (Hasler & Süsstrunk 2003), edge density, and dominant hue. These provide baseline visual statistics and feed into downstream models. Distributions were compared between independent and institutional groups.

---

## Tier 2 — CLIP Zero-Shot Semantic Classification (all 9,568 thumbnails)

Using ViT-B/32 (OpenAI CLIP), each thumbnail was scored against 7 opposing prompt pairs without any fine-tuning: `has_face`, `is_animated`, `has_text_overlay`, `is_diagram`, `is_colorful`, `is_professional`, `is_clickbait`. A logistic regression trained on CLIP + OpenCV features (5-fold cross-validation, n=320) tested whether thumbnail visuals alone can predict channel type.

---

## Tier 3 — BLIP VQA + Captioning (stratified sample, 320 thumbnails, 40/channel)

Two HuggingFace models ran locally on Apple MPS:
- **BLIP-VQA** answered yes/no questions: `has_face`, `has_text_overlay`, `is_animated`, `is_diagram`, `curiosity_trigger`, and an institutional/independent guess
- **BLIP-captioning** generated a natural language `main_subject` description per thumbnail
- Professionalism, appeal, and complexity **scores (1–5)** were derived from CLIP probabilities

Key per-channel results:

| Channel | Group | Has Face | Has Text | Curiosity Trigger |
|---|---|---|---|---|
| 3Blue1Brown | Independent | 0% | 90% | 10% |
| Kurzgesagt | Independent | 5% | 97.5% | 22.5% |
| Walter Lewin | Independent | 5% | 85% | 5% |
| minutephysics | Independent | 0% | 97.5% | 2.5% |
| EPFL | Institutional | 2.5% | 80% | 55% |
| ETH Zürich | Institutional | 0% | 77.5% | 37.5% |
| MIT | Institutional | 12.5% | 75% | 25% |
| Stanford | Institutional | 2.5% | 65% | 20% |

---

## Tier 4 — VLM Structured Semantic Analysis via Ollama (400 thumbnails, 200/group)

`qwen2.5vl:7b` running locally via Ollama with Pydantic schema enforcement extracted structured JSON for each thumbnail:

- **Embedded text** (exact transcription)
- **Text function**: `none` / `factual_statement` / `question` / `hyperbolic_hook` / `label_or_acronym`
- **Visual presentation style**: `academic_lecture` / `cgi_render` / `pop_illustration` / `vlog_selfie` / `stock_photography` / `minimalist_text`
- **Text placement zone**: top / bottom / center / full overlay / etc.
- **Human presence**: is_present, count, canvas coverage %, dominant emotion
- **Clickbait indicators**: red arrow/circle, exaggerated contrast, sensationalism score 1–5

**Key findings (independent vs. institutional):**

| Metric | Independent | Institutional |
|---|---|---|
| % with human face | 42.5% | 76.5% |
| Mean face canvas coverage | 14.8% | 28.6% |
| Question + hyperbolic hook text | 40% | 6% |
| Labels / acronyms text | 6.5% | 23% |
| No text at all | 28% | 49.5% |
| Pop-illustration style | 44.5% | 2.5% |
| Academic lecture style | 30% | 52% |
| Stock photography style | 5.5% | 33.5% |
| Mean sensationalism score | 2.08 / 5 | 1.30 / 5 |

Statistical tests (chi-square for categorical features, Mann-Whitney U for sensationalism score and face coverage) confirmed these differences are significant.

---

## DINOv2 Visual Embedding Clustering (all 9,568 thumbnails)

`facebook/dinov2-base` (ViT-B/14) produced 768-dimensional embeddings for every thumbnail. UMAP reduced these to 2D; silhouette-guided k-means selected **5 clusters**. Cluster composition revealed clear group separation:

| Cluster | Independent % | Institutional % |
|---|---|---|
| 0 | 39.9% | 60.1% |
| 1 | 17.8% | 82.2% |
| 2 | 55.1% | 44.9% |
| 3 | 22.2% | 77.8% |
| 4 | 1.0% | 99.0% |

The synthesis dataset cross-referenced VLM annotations with DINOv2 clusters to define **Thumbnail Archetypes**, profiled on both semantic (text function, style, emotion) and visual/spatial (edge density, face coverage, placement zone) dimensions.

---

## Engagement Correlation Analysis (all 9,569 videos)

All title and thumbnail features were merged and tested against three engagement metrics (log views, like rate, comment rate) via:
- **Spearman correlations** — full heatmap across all features
- **Random Forest** feature importance (5-fold CV R²) for predicting log(views)
- **Scatter plots** of BLIP appeal/professionalism scores vs. actual engagement, split by group

---

## Additional Spatial Analysis

Two supplementary analyses ran on all 9,568 thumbnails:
- **Face-to-canvas ratio** via OpenCV Haar cascade: detected face bounding box area as a fraction of total thumbnail area, compared by channel and group
- **Edge-dominant zone**: 6-zone grid (top-left, top-center, top-right, bottom-left, bottom-center, bottom-right) measuring where visual activity is concentrated as a text placement proxy
