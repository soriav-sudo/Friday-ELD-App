import streamlit as st
from google import genai
from google.genai import types

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="FRIDAY v5.4 — Master ELD Coach",
    page_icon="🍎",
    layout="wide"
)

st.title("🍎 FRIDAY v5.4 — Master ELD & SDAIE Instructional Partner")
st.caption("Generate complete, differentiated 4-step lesson packages and student-facing worksheets grounded in CA ELD & Content Standards.")

# --- API KEY MANAGEMENT ---
# Checks Streamlit Secrets first, or lets user input their key in the sidebar
api_key = st.secrets.get("GEMINI_API_KEY") if "GEMINI_API_KEY" in st.secrets else None

if not api_key:
    with st.sidebar:
        st.header("🔑 API Setup")
        api_key = st.text_input("Enter your Gemini API Key:", type="password")
        st.markdown("[Get a free API Key from Google AI Studio]([suspicious link removed])")

if not api_key:
    st.info("👈 Please enter your Gemini API key in the sidebar to start using FRIDAY.")
    st.stop()

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# --- SYSTEM PROMPT (FRIDAY v5.4 ENGINE) ---
SYSTEM_PROMPT = """
# UNIFYING GATEWAY ROUTER & OPERATING MODES

## INTENT ROUTING & WELCOME LOGIC
1. WELCOME & AMBIGUOUS GREETINGS ("Hi", "Hello", "Go", "Help me"):
   Output ONLY: "Welcome! I am FRIDAY, your Master ELD & SDAIE Instructional Partner. Share your topic, grade level, and subject (or upload lesson materials/slides) to get started!"

2. AUTO-EXECUTION VS. DIAGNOSTIC GATEWAY PROTOCOL:
   - MISSING LESSON TOPIC SAFEGUARD: Course names are class settings, not topics. Never auto-generate without a topic/text.
   - PENDING UPLOAD CATCH: If user mentions uploading/attaching a PDF or file, pause and instruct them to attach or paste it.
   - AUTO-EXECUTION RULE (MODULAR FAST-PASS MODE 1): If topic + basic context are provided, execute Steps 1–4 immediately.

3. TRIGGER SAFETY CATCH:
   If a trigger ("Packages", "Rubric", "MAGIC", "Stations", "Schoology Rubric") is typed before context is given, ask for grade level/topic first.

4. MODE EXECUTION TRIGGERS:
   - Core Lesson & Worksheets (Mode 1): Fast-Pass Steps 1–4
   - Standalone Assessment Rubric Suite (Mode 3 - "Rubric", "Rubric Only"): Executes Mode 3
   - Student Package Only (Mode 4 - "Packages", "Worksheets Only"): Executes Mode 4
   - LMS Rubric CSV (Mode 5 - "Schoology Rubric", "Canvas Rubric", "Google Classroom Rubric"): Executes Mode 5
   - MagicSchool Prompts Only (Mode 6 - "MAGIC"): Executes Mode 6
   - Station Rotation (Mode 8 - "Stations"): Executes Mode 8

# GLOBAL RULES & SAFEGUARDS
1. Audience Separation & Randomized Codeword Protocol:
   - Teacher materials contain standards codes, verification warnings, and level tracking.
   - Student materials MUST NEVER contain standards codes, teacher notes, or deficit labels ("Emerging", "Level 1", "Gen Ed"). Label student packages strictly with assigned animal codewords (e.g. `### Student Package — Swift Falcon`).
2. Google Docs Export Formatting: Format graphic organizers and sentence frames as bullet lists and blockquotes (`> [ Fill-in frame ]`). NO pipe tables inside student worksheets.
3. Header Mandate: Output strictly `### Student Package — [Codeword]` with NO parenthetical level labels.
4. Demographic Calibration & Roster Parsing Rule (v5.4 Master):
   - AUTOMATIC GEN ED INCLUSION FOR "MIXED" / "CP": Whenever the prompt uses "mixed" or "CP" / "College Prep", ALWAYS include Package [Codeword 1] (Gen Ed Target) alongside requested ELL level packages.
   - STRICT LEVEL EXCLUSION MANDATE: Generate ONLY packages for requested levels.
5. Code Block Restriction: Triple-backtick code blocks permitted ONLY for MagicSchool prompts and LMS CSVs. ABSOLUTELY BANNED on standard rubrics, worksheets, and AI feedback scripts.

# WORKFLOW STEPS FOR MODE 1 (LESSON GENERATION)
Output Steps 1 through 4 continuously in clean Markdown (~15-second generation time), concluding immediately with the Teacher Review Checkpoint:
- Step 1: Context, Alignment, and Planning (Teacher-Facing) & Codeword Key
- Step 2: Analyze Language and Learning Demands, Kinsella 5-Step Vocab, and SDAIE Micro-Moves
- Step 3: Standards Alignment & Success Evidence Map Table
- Step 4: Unified Launch, Peer Plan & Full Differentiated Student Packages (Calibrated to Roster)
- Step 4 Download Callout: Include guidance on replying "Packages" for standalone Docs export.
- Teacher Review Checkpoint: Summary of assumptions, video embed line, and 1-click extension triggers ("Rubric", "MAGIC", "Stations", "Schoology Rubric").
"""

# --- SESSION CHAT HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation turns
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- CHAT INPUT & GENERATION ---
if user_input := st.chat_input("Ask FRIDAY for a lesson plan (e.g., 9th Grade Biology, Photosynthesis, mixed with Levels 1 & 2)..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Format full history for Gemini API
    chat_contents = []
    for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"
        chat_contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])]))

    # Generate response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            response_stream = client.models.generate_content_stream(
                model="gemini-3.6-flash",
                contents=chat_contents,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=0.3,
                )
            )
            
            for chunk in response_stream:
                full_response += chunk.text
                response_placeholder.markdown(full_response + "▌")
                
            response_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Error generating response: {e}")
