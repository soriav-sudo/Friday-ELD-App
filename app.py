import google.generativeai as genai
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="FRIDAY — Master ELD & SDAIE Partner",
    page_icon="⚡",
    layout="wide",
)

# Custom Dark Theme Styling (Matching website code.docx palette)
st.markdown(
    """
<style>
    .stApp {
        background-color: #020617;
        color: #f8fafc;
    }
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid #1e293b;
    }
    h1, h2, h3 {
        color: #38bdf8 !important;
    }
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {
        background-color: #020617 !important;
        border-color: #334155 !important;
        color: #f8fafc !important;
    }
    .stButton > button {
        background-color: #1e293b;
        border: 1px solid #334155;
        color: #cbd5e1;
        width: 100%;
        border-radius: 6px;
        font-size: 13px;
        text-align: left;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        background-color: #0284c7;
        color: #ffffff;
        border-color: #38bdf8;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Retrieve API Key from Streamlit Secrets or Sidebar Input
api_key = st.secrets.get("GEMINI_API_KEY") or st.sidebar.text_input(
    "Enter Gemini API Key", type="password"
)

if not api_key:
  st.info(
      "Please enter your Gemini API Key in Streamlit Secrets or in the sidebar to"
      " begin."
  )
  st.stop()

genai.configure(api_key=api_key)

# ------------------------------------------------------------------------------
# MASTER FRIDAY SYSTEM PROMPT
# ------------------------------------------------------------------------------
FRIDAY_SYSTEM_PROMPT = """UNIFYING GATEWAY ROUTER & OPERATING MODES
INTENT ROUTING & WELCOME LOGIC
WELCOME & AMBIGUOUS GREETINGS ("Hi", "Hello", "Go", "Help me"): On generic greetings without a specific topic or request, output ONLY the greeting below and STOP (do NOT output diagnostic questions):

"Welcome! I am FRIDAY, your Master ELD & SDAIE Instructional Partner. Share your topic, grade level, and subject (or upload lesson materials/slides) to get started!"

AUTO-EXECUTION VS. DIAGNOSTIC GATEWAY PROTOCOL:

MISSING LESSON TOPIC SAFEGUARD (STRICT NO-GHOST-LESSON RULE): Course names and class settings (e.g., "12th Grade ALD", "7th Grade Science", "ELD Class", "Levels 1 & 2") are CLASS SETTINGS, NOT LESSON TOPICS. NEVER auto-generate a lesson plan without a specific topic, text, concept, or resource. If provided with settings/demographics but no lesson topic or file upload: PAUSE immediately, acknowledge provided context, and ask ONLY:

"Got it! [Acknowledge provided facts, e.g., 12th Grade ALD Class (Levels 1 & 2)]. To build your custom lesson package, please let me know:

What topic, reading text, or concept would you like to focus on today? (Or do you have a PDF, slides, or notes to upload/paste?)
What is your class duration? (e.g., 50 min, 90 min block—or press enter for our 55-min default)."

PENDING UPLOAD CATCH (MANDATORY PAUSE & INSTRUCTION FOR FILE UPLOADS): If the user indicates they have a file, PDF, document, text, or "something" to upload/paste (e.g., "I have a PDF", "I have something to upload", "attaching notes"), OR asks where/when to upload: PAUSE immediately and output:

"You can upload or paste your file right here in the chat at any time! Simply attach your document, PDF, slides, or text (or paste it directly into your message), and I will generate your complete differentiated lesson package directly from your material."

AUTO-EXECUTION RULE (MODULAR FAST-PASS MODE 1 GENERATION): Execute MODE 1 IMMEDIATELY ONLY IF the user provides BOTH: (1) A specific Lesson Topic/Resource/File, AND (2) Basic context (Grade Level or Class Setting). Lead with the Curriculum Grounding Callout Banner, followed by: "Here is your 5-Step Core Differentiated Lesson & Assessment Package!" and generate Steps 1–5 in Fast-Pass mode (~15-second generation time).

📄 Curriculum Grounding Note: Generated using standard CA curriculum frameworks. Have a specific textbook excerpt, PDF, slides, or notes you'd rather use? Simply attach or paste them below, and I'll re-tune this entire package directly to your material!

MODE EXECUTION TRIGGERS:
Core Lesson (Mode 1): Lead with Grounding Banner + "Here is your 5-Step Core Differentiated Lesson & Assessment Package!" (Fast-Pass Steps 1–5)
Student Package Only (Mode 4 - "Packages"): "Here are your clean, student-facing differentiated packages!"
MagicSchool Prompts Only (Mode 6 - "MAGIC"): "Here are your standalone, copy-ready MagicSchool AI Prompts!"
Station Rotation (Mode 8 - "Stations"): "Here is your 3-Station Blended Learning Implementation Plan!"
LMS Rubric CSV (Mode 5 - "Schoology Rubric"): "Here is your LMS-compatible Rubric CSV file for 1-click gradebook import!"
Standalone Rubric (Mode 3 - "Rubric Only"): "Here is your standalone Differentiated Assessment Rubric Package!"

MODE 3: STANDALONE RUBRIC SUITE PROTOCOL ("Rubric Only")
Generate strictly the assessment suite in standard Markdown text (NO code blocks):

Master Unified Rubric Matrix
Assessment Criterion	Gen Ed / Benchmark Target (CCSS)	ELL Emerging Level (CA ELD)	ELL Expanding Level (CA ELD)	ELL Bridging Level (CA ELD)
[Criterion 1 Name]	[Gen Ed Benchmark Description]	[Emerging Level Description]	[Expanding Level Description]	[Bridging Level Description]
[Criterion 2 Name]	[Gen Ed Benchmark Description]	[Emerging Level Description]	[Expanding Level Description]	[Bridging Level Description]

MODE 4: STUDENT PACKAGE ONLY PROTOCOL ("Packages", "Student Package Only", "Student Facing")
Generate strictly the student packages as clean Markdown text using the Randomized Adjective + Animal Codewords:
Header Mandate: Output strictly ### Student Package — [Codeword] with NO parenthetical level labels.

MODE 6: MAGICSCHOOL PROMPTS ONLY PROTOCOL ("MAGIC", "Magic", "MagicSchool")
Generate strictly the two fenced, copy-ready MagicSchool AI prompts with clear titles and step-by-step setup instructions for teachers above each code box:

### 🤖 PROMPT 1: MagicSchool AI Student Room / Tutor
📋 **Setup Instructions for Teachers (2 Quick Steps):**
1️⃣ **Copy Code Box 1 below** ➡️ Paste into MagicSchool's **Custom Prompt / Instructions** box.
2️⃣ **Copy your Student Worksheets** (from Step 4 above or reply "Packages") ➡️ Paste into MagicSchool's **"What does this room need to know?" (Knowledge / Context)** box.

STUDENT ASSIGNMENT & WORKSHEET WALKTHROUGH CONTEXT:
Grade Level & Subject: [Grade Level] [Subject/Topic]
Assignment Title & Focus: [Lesson Topic / Title of Student Packages generated in Step 4]
Student Worksheet Materials: Refer strictly to the Student Worksheet Packages ([Codeword 1]–[Codeword 4]) pasted into this Room's "What does this room need to know?" (Knowledge / Context) box.
Tiered Worksheet Packages & Scaffolds Available in Knowledge Box: • Package [Codeword 1]: Core analytical prompts & synthesis tasks • Package [Codeword 2]: Level 1 word bank, fill-in-the-blank frames, & visual cues • Package [Codeword 3]: Level 2 sentence starters & paragraph templates • Package [Codeword 4]: Level 3 academic precision prompts & cohesion frames
ROLE & TUTORING PROTOCOL: You are a supportive, step-by-step AI Learning Coach helping a student complete their assigned worksheet.

### 📊 PROMPT 2: MagicSchool Presentation Deck Generator
📋 **Setup Instructions for Teachers:**
1️⃣ **Copy Code Box 2 below** ➡️ Paste directly into MagicSchool's **Presentation Generator / AI Slide Tool**.

IMAGE REQUIREMENT: Mandatory content-specific image on every slide except exit ticket. Visuals are language-access scaffolds for multilingual learners.

SYSTEM PROMPT: FRIDAY — MASTER ELD & SDAIE COACH
ROLE & CORE PHILOSOPHY
You are FRIDAY, an expert ELD & SDAIE Instructional Coach and lesson-design partner for K–12 educators across all subjects. Maintain grade-level cognitive rigor while providing language access supports matched to multilingual learners' CA ELD proficiency levels.

GLOBAL RULES & SAFEGUARDS
CODEWORD MANDATE (STRICT RANDOMIZATION DIRECTIVE): 
Dynamically invent 4 UNIQUE, RANDOM, empowering Adjective + Animal codewords for EVERY NEW LESSON (e.g., Crimson Eagle, Radiant Fox, Solar Hawk, Noble Lynx, Cobalt Puma, Brave Panther, Emerald Raven). NEVER default to reusing "Swift Falcon", "Golden Bear", or "Blue Dolphin" across lessons!
"""

# ------------------------------------------------------------------------------
# SIDEBAR CONTROL PANEL (DROPDOWNS WITH DYNAMIC "OTHER" TRIGGER)
# ------------------------------------------------------------------------------
with st.sidebar:
  st.title("⚡ FRIDAY")
  st.caption("Master ELD & SDAIE Instructional Partner")
  st.markdown("---")

  st.markdown("### 📋 CLASS CONFIG")

  cfg_grade = st.selectbox(
      "Grade Level",
      [
          "12th Grade",
          "11th Grade",
          "10th Grade",
          "9th Grade",
          "Middle School (6-8)",
          "Elementary (4-5)",
      ],
      index=0,
  )

  selected_subject_option = st.selectbox(
      "Subject / Course",
      [
          "ELA / ALD (English & Academic Language Dev)",
          "Mathematics (Math 6–8, Algebra, Geometry)",
          "Science (Biology, Chemistry, Physics, NGSS)",
          "Social Science / History (US/World History, Civics)",
          "Career Technical Education (CTE / Tech)",
          "Visual & Performing Arts / Electives",
          "World Languages",
          "Other (Specify below)",
      ],
      index=0,
  )

  # Dynamic trigger for custom subjects
  if selected_subject_option == "Other (Specify below)":
    cfg_subject = st.text_input(
        "Specify Subject / Course",
        placeholder="e.g., Physical Education, Health, Leadership",
    )
    if not cfg_subject:
      cfg_subject = "Custom Content Area"
  else:
    cfg_subject = selected_subject_option

  cfg_duration = st.selectbox(
      "Class Duration",
      ["55 minutes", "50 minutes", "90 minutes (Block)"],
      index=0,
  )

  st.markdown("**Roster Levels Included**")
  lvl_core = st.checkbox("Core / Benchmark Target", value=True)
  lvl_1 = st.checkbox("Level 1 (Emerging)", value=True)
  lvl_2 = st.checkbox("Level 2 (Expanding)", value=True)
  lvl_3 = st.checkbox("Level 3 (Bridging)", value=False)

  st.markdown("---")
  st.markdown("### ⚡ MODE FAST-PASS")

  if st.button("📦 Student Packages Only", use_container_width=True):
    st.session_state.pending_trigger = "Packages"
  if st.button("🤖 MagicSchool AI Prompts", use_container_width=True):
    st.session_state.pending_trigger = "MAGIC"
  if st.button("📊 Standalone Rubric Suite", use_container_width=True):
    st.session_state.pending_trigger = "Rubric Only"
  if st.button("📈 LMS Rubric CSV", use_container_width=True):
    st.session_state.pending_trigger = "Schoology Rubric"
  if st.button("🔄 3-Station Rotation Plan", use_container_width=True):
    st.session_state.pending_trigger = "Stations"

# ------------------------------------------------------------------------------
# MAIN CHAT STREAM INTERFACE
# ------------------------------------------------------------------------------
st.title("⚡ FRIDAY Master ELD Engine")
st.caption(
    "Universal multi-disciplinary lesson design partner across all K–12 subjects."
)

if "messages" not in st.session_state:
  st.session_state.messages = []

for msg in st.session_state.messages:
  with st.chat_message(msg["role"]):
    st.markdown(msg["content"])

user_input = st.chat_input(
    "Enter lesson topic or concept (e.g., Photosynthesis, Quadratic"
    " Formula)..."
)

if getattr(st.session_state, "pending_trigger", None):
  user_input = st.session_state.pending_trigger
  st.session_state.pending_trigger = None

if user_input:
  # Assemble roster levels list from sidebar checkboxes
  roster_levels = []
  if lvl_core:
    roster_levels.append("Core/Benchmark")
  if lvl_1:
    roster_levels.append("Level 1 Emerging")
  if lvl_2:
    roster_levels.append("Level 2 Expanding")
  if lvl_3:
    roster_levels.append("Level 3 Bridging")

  roster_str = (
      ", ".join(roster_levels) if roster_levels else "All Levels (Default)"
  )

  # Attach sidebar config parameters to the user prompt automatically
  contextual_user_prompt = (
      f"[CLASS CONFIGURATION]: Grade: {cfg_grade} | Subject: {cfg_subject} |"
      f" Duration: {cfg_duration} | Roster Tiers: {roster_str}\n[USER"
      f" REQUEST]: {user_input}"
  )

  st.session_state.messages.append({"role": "user", "content": user_input})
  with st.chat_message("user"):
    st.markdown(user_input)

  model = genai.GenerativeModel(
      model_name="gemini-3.8-flash", system_instruction=FRIDAY_SYSTEM_PROMPT
  )

  gemini_history = []
  for m in st.session_state.messages[:-1]:
    role = "user" if m["role"] == "user" else "model"
    gemini_history.append({"role": role, "parts": [m["content"]]})

  chat = model.start_chat(history=gemini_history)

  with st.chat_message("assistant"):
    placeholder = st.empty()
    full_text = ""

    try:
      response = chat.send_message(contextual_user_prompt, stream=True)
      for chunk in response:
        full_text += chunk.text
        placeholder.markdown(full_text + "▌")
      placeholder.markdown(full_text)
    except Exception as err:
      st.error(f"Generation error: {err}")

  if full_text:
    st.session_state.messages.append(
        {"role": "assistant", "content": full_text}
    )
