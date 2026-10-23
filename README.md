# 🍎 FRIDAY v5.4 — Master ELD & SDAIE Instructional Partner

An AI-powered lesson design and differentiation web application built for K–12 educators. Powered by Google Gemini 2.5 Flash and Streamlit, **FRIDAY** generates complete, multi-tiered lesson packages and student-facing worksheets aligned with California Common Core State Standards (CCSS) and CA English Language Development (ELD) Standards.

---

## ✨ Features

- **Fast-Pass Core Generation (~15s):** Automatically outputs Steps 1–4 (Teacher Context, Language Demands & Kinsella Vocabulary Routine, Standards Map, and Full Student Worksheets).
- **Roster-Calibrated Worksheets:** Generates student-facing packages strictly tailored to your classroom demographics (e.g., General Ed + Level 1 + Level 2).
- **Stigma-Free Student Materials:** Uses empowering `Adjective + Animal` codewords (e.g., *Swift Falcon*, *Golden Bear*) with zero deficit labels or admin codes on student worksheets.
- **1-Click Google Docs Export:** Format-engineered without pipe tables so worksheets export cleanly directly into Google Docs for easy printing.
- **Modular On-Demand Triggers:** Pull up companion tools in clean, separate turns:
  - 📊 **`Rubric`** — Master Unified Rubric Matrix + AI Feedback Tool Evaluation Script.
  - 🤖 **`MAGIC`** — MagicSchool AI Space Tutor & Presentation Deck generator prompts.
  - 🔄 **`Stations`** — 3-Station Blended Learning rotation plan.
  - 📈 **`Schoology Rubric` / `Canvas Rubric`** — LMS-compatible gradebook CSV files.

---

## 🚀 Tech Stack

- **Frontend / UI:** [Streamlit]([suspicious link removed])
- **AI Model:** Google Gemini (`gemini-2.5-flash` via the `google-genai` SDK)
- **Deployment:** Streamlit Community Cloud

---

## 🛠️ Local Setup & Running

1. **Clone the repository:**
   ```bash
   git clone [suspicious link removed]
   cd friday-eld-app
