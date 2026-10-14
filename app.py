import streamlit as st
import json
import jarvis
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from streamlit_mic_recorder import speech_to_text

import streamlit.components.v1 as components


# ==============================
# BROWSER SPEECH
# ==============================

def speak_in_browser(text):
    """Speak text in the user's browser using the Web Speech API."""
    if not text:
        return

    # JSON encoding safely handles quotes, backslashes, and line breaks.
    safe_text = json.dumps(str(text))

    components.html(
        f"""
        <script>
            const message = {safe_text};
            if ('speechSynthesis' in window && message.trim()) {{
                window.speechSynthesis.cancel();
                const utterance = new SpeechSynthesisUtterance(message);
                utterance.lang = 'en-US';
                utterance.rate = 1;
                utterance.pitch = 1;
                window.speechSynthesis.speak(utterance);
            }}
        </script>
        """,
        height=0,
    )


# ==============================
# ENVIRONMENT
# ==============================

env_path = Path(__file__).parent / ".env"

load_dotenv(dotenv_path=env_path)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# ==============================
# GROQ CLIENT
# ==============================

if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)
else:
    client = None


# ==============================
# PAGE SETTINGS
# ==============================

st.set_page_config(
    page_title="Jarvis AI Assistant",
    page_icon="🤖",
    layout="centered"
)



# ==============================
# PROFESSIONAL UI THEME
# ==============================

st.markdown(
    """
    <style>
    :root {
        --navy: #0b1220;
        --panel: #121d30;
        --line: rgba(148, 163, 184, 0.22);
        --text: #e8eef8;
        --muted: #a9b8cc;
        --accent: #55d6c2;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 10% 0%, rgba(45, 91, 140, 0.25), transparent 38%),
            radial-gradient(ellipse at 95% 15%, rgba(35, 145, 135, 0.13), transparent 30%),
            linear-gradient(145deg, #080e19 0%, #0d1727 52%, #101b2d 100%);
        color: var(--text);
    }

    [data-testid="stHeader"] {
        background: rgba(8, 14, 25, 0.72);
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 980px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3, p, label, .stMarkdown {
        color: var(--text);
    }

    [data-testid="stTextInput"] input,
    [data-testid="stTextArea"] textarea {
        background: rgba(16, 28, 46, 0.92);
        color: #f1f5f9;
        border: 1px solid var(--line);
        border-radius: 10px;
    }

    [data-testid="stTextInput"] input:focus,
    [data-testid="stTextArea"] textarea:focus {
        border-color: var(--accent);
        box-shadow: 0 0 0 1px var(--accent);
    }

    .stButton > button {
        border: 1px solid rgba(85, 214, 194, 0.55);
        border-radius: 10px;
        background: linear-gradient(135deg, #173a4a, #164b50);
        color: #f4fffd;
        font-weight: 600;
        padding: 0.55rem 1rem;
        transition: all 0.18s ease;
    }

    .stButton > button:hover {
        border-color: #8af0df;
        background: linear-gradient(135deg, #20536a, #1a6664);
        color: white;
        transform: translateY(-1px);
    }

    [data-testid="stVerticalBlockBorderWrapper"],
    [data-testid="stExpander"] {
        border-color: var(--line);
        border-radius: 14px;
    }

    hr {
        border-color: var(--line);
    }

    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    .jarvis-hero {
        text-align: center;
        padding: 2.2rem 1.2rem;
        margin: 0.5rem 0 1.5rem;
        border: 1px solid rgba(85, 214, 194, 0.28);
        border-radius: 22px;
        background: linear-gradient(135deg, rgba(20, 42, 65, 0.96), rgba(14, 34, 47, 0.88));
        box-shadow: 0 18px 55px rgba(0, 0, 0, 0.24);
    }

    .jarvis-hero .robot {
        font-size: 3.2rem;
        line-height: 1.2;
    }

    .jarvis-hero h1 {
        color: #7ce7d5;
        font-size: clamp(2rem, 5vw, 3rem);
        letter-spacing: 0.16em;
        margin: 0.55rem 0 0.35rem;
    }

    .jarvis-hero p {
        color: #c0d0e2;
        font-size: 1rem;
        margin-bottom: 1rem;
    }

    .jarvis-badge {
        display: inline-block;
        padding: 0.45rem 0.8rem;
        border-radius: 999px;
        border: 1px solid rgba(124, 231, 213, 0.35);
        color: #a5f3e6;
        font-size: 0.72rem;
        letter-spacing: 0.08em;
    }

    @media (max-width: 640px) {
        [data-testid="stMainBlockContainer"] {
            padding: 1rem 1rem 2rem;
        }
        .jarvis-hero {
            padding: 1.5rem 0.8rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ==============================
# SESSION STATE


    
if "password_tool" not in st.session_state:
    st.session_state.password_tool = False

if "chatbot_open" not in st.session_state:
    st.session_state.chatbot_open = False

if "student_mode" not in st.session_state:
    st.session_state.student_mode = False
if st.button("🔐 Password Tool"):
    st.session_state.password_tool = True
    st.rerun()

# ==============================
# STUDENT MODE BUTTON
# ==============================
# ==============================
# STUDENT MODE
# ==============================

if st.button("🎓 Student Mode"):

    st.session_state.student_mode = True
    st.rerun()


if st.session_state.student_mode:

    st.divider()

    st.subheader("🎓 Student Mode")

    student_question = st.text_input(
        "Ask your study question:",
        placeholder="Example: Explain photosynthesis",
        key="student_question"
    )

    if st.button("Ask Jarvis", key="student_ask"):

        if not client:

            st.error("Groq API key is not configured.")

        elif not student_question:

            st.warning("Please enter a question.")

        else:

            try:

                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are Jarvis Student Mode, "
                                "a helpful tutor. Explain concepts "
                                "clearly and simply. Give examples "
                                "when useful and help the student learn."
                            )
                        },
                        {
                            "role": "user",
                            "content": student_question
                        }
                    ]
                )

                answer = response.choices[0].message.content

                st.write("### 🤖 Jarvis")
                st.write(answer)

                speak_in_browser(answer)

            except Exception as e:

                st.error("Student Mode error:")
                st.write(e)
    
# ==============================
# JARVIS HERO HEADER
# ==============================

st.markdown(
    """
    <section class="jarvis-hero">
        <div class="robot">🤖</div>
        <h1>J.A.R.V.I.S</h1>
        <p>Your Personal AI Assistant</p>
        <span class="jarvis-badge">AI ASSISTANT&nbsp; • &nbsp;STUDENT MODE&nbsp; • &nbsp;SMART TOOLS</span>
    </section>
    """,
    unsafe_allow_html=True
)


# ==============================
# COMMAND INPUT
# ==============================

command = st.text_input(
    "Enter your command:",
    placeholder="Example: open YouTube"
)

# ==============================
# VOICE COMMAND
# ==============================

st.subheader("🎤 Voice Command")

voice_command = speech_to_text(
    language="en",
    start_prompt="🎤 Start Speaking",
    stop_prompt="⏹️ Stop",
    just_once=True,
    use_container_width=True,
    key="voice_command"
)
if voice_command:

    st.write("You said:", voice_command)

    if "open chatbot" in voice_command.lower():
        st.session_state.chatbot_open = True
        st.rerun()

    elif "password tool" in voice_command.lower():
        st.session_state.password_tool = True
        st.rerun()

    else:
        answer = jarvis.process_command(voice_command)

        if answer and answer != "PASSWORD_TOOL":
            st.write(answer)
            speak_in_browser(answer)


# ==============================
# SEND COMMAND
# ==============================

if st.button("Send"):

    if command:

        # ==========================
        # OPEN CHATBOT
        # ==========================

        if "open chatbot" in command.lower():

            st.session_state.chatbot_open = True
            st.rerun()

        # ==========================
        # OTHER COMMANDS
        # ==========================

        else:

            result = jarvis.process_command(command)

            if result == "exit":

                st.warning("Jarvis has been stopped.")

            else:

                st.success("Command processed successfully.")

                if result:
                    st.write(result)
                    speak_in_browser(result)

    else:

        st.warning("Please enter a command.")


# ==============================
# CHATBOT
# ==============================

if st.session_state.chatbot_open:

    st.divider()

    st.subheader("💬 Jarvis AI Chatbot")

    question = st.text_input(
        "Ask Jarvis anything:",
        key="chatbot_question"
    )

    if st.button("Ask Jarvis", key="ask_jarvis"):

        if not client:

            st.error("Groq API key is not configured.")

        elif question:

            try:

                response = client.chat.completions.create(

                    model="openai/gpt-oss-20b",

                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are Jarvis, a helpful "
                                "personal AI assistant. "
                                "Give clear and concise answers."
                            )
                        },
                        {
                            "role": "user",
                            "content": question
                        }
                    ]
                )

                answer = response.choices[0].message.content

                st.write("### 🤖 Jarvis")

                st.write(answer)

                speak_in_browser(answer)

            except Exception as e:

                st.error(
                    "Sorry, I couldn't connect to the AI service."
                )

                st.write(e)

        else:

            st.warning("Please enter a question.")
# ==============================
# PASSWORD TOOL
# ==============================

import random
import string

if st.session_state.password_tool:

    st.divider()
    st.subheader("🔐 Password Tool")

    option = st.radio(
        "Choose an option:",
        [
            "Generate Password",
            "Check Password Strength"
        ],
        key="password_option"
    )

    if option == "Generate Password":

        length = st.slider(
            "Choose password length:",
            min_value=8,
            max_value=32,
            value=12
        )

        if st.button("Generate Password"):

            characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"

            password = (
                random.choice(string.ascii_lowercase)
                + random.choice(string.ascii_uppercase)
                + random.choice(string.digits)
                + random.choice("!@#$%^&*()-_=+")
                + "".join(
                    random.choice(characters)
                    for _ in range(length - 4)
                )
            )

            password_list = list(password)
            random.SystemRandom().shuffle(password_list)
            password = "".join(password_list)

            st.success("Password generated!")
            st.code(password)

    elif option == "Check Password Strength":

        password = st.text_input(
            "Enter a password to check:",
            type="password",
            key="password_to_check"
        )

        if st.button("Check Strength"):

            if not password:
                st.warning("Please enter a password.")

            else:
                score = 0

                if len(password) >= 8:
                    score += 1

                if any(c.islower() for c in password):
                    score += 1

                if any(c.isupper() for c in password):
                    score += 1

                if any(c.isdigit() for c in password):
                    score += 1

                if any(c in string.punctuation for c in password):
                    score += 1

                if score <= 2:
                    st.warning("Weak password")

                elif score <= 3:
                    st.info("Moderate password")

                else:
                    st.success("Stronger password")

                st.caption(
                    "This is a basic estimate, not a guarantee "
                    "of password security."
                )
