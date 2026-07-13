import streamlit as st

from modules.audio import get_audio_input
from modules.evaluator import evaluate
from modules.face_analysis import detect_emotion
from modules.voice_analysis import analyze_voice
from modules.stress_analysis import detect_stress
from modules.interview_report import show_report


def run_interview(questions):
    """
    Conducts the interview.
    Handles:
    - Questions
    - Recording
    - Emotion
    - Voice
    - Stress
    - Evaluation
    """

    # ==========================================
    # SHOW FINAL REPORT
    # ==========================================
    if st.session_state.question_index >= len(questions):
        show_report()
        return

    # ==========================================
    # CURRENT QUESTION
    # ==========================================
    current = questions[st.session_state.question_index]
    current_question = current["question"]
    current_skill = current["skill"]

    progress = (st.session_state.question_index + 1) / len(questions)

    # ==========================================
    # HEADER
    # ==========================================
    st.markdown("# 🎤 AI Interview Session")

    st.caption(
        f"Question {st.session_state.question_index + 1} of {len(questions)}"
    )

    st.info(
        "💡 Answer naturally. Speak confidently and avoid filler words like 'um', 'uh' and 'like'."
    )
    st.progress(progress)

    # Fixed Indentation for the 4-column layout block
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "📍 Question",
            f"{st.session_state.question_index + 1}/{len(questions)}"
        )

    with c2:
        st.metric(
            "🧠 Skill",
            current_skill
        )

    with c3:
        st.metric(
            "📝 Answered",
            len(st.session_state.results)
        )

    with c4:
        st.metric(
            "📊 Progress",
            f"{int(progress * 100)}%"
        )

    st.divider()

    # ==========================================
    # QUESTION
    # ==========================================
    st.markdown("## 💬 Interview Question")
    st.markdown(
        f"""
        <div style="
        padding:25px;
        background:#f8fafc;
        border-left:8px solid #2563EB;
        border-radius:10px;
        box-shadow:0 2px 10px rgba(0,0,0,0.08);
        font-size:22px;
        font-weight:500;
        margin-bottom:20px;
        ">
        {current_question}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.success(f"🧠 Skill Being Evaluated: **{current_skill}**")
    st.divider()

    # ==========================================
    # BUTTONS
    # ==========================================
    col1, col2, col3 = st.columns(3)
    with col1:
        record_clicked = st.button("🎤 Record Answer", use_container_width=True, type="primary")
    with col2:
        skip_clicked = st.button("⏭ Skip Question ", use_container_width=True)
    with col3:
        finish_clicked = st.button("🛑 End Interview", use_container_width=True)

    # ==========================================
    # FINISH INTERVIEW
    # ==========================================
    if finish_clicked:
        st.session_state.question_index = len(questions)
        st.rerun()

    # ==========================================
    # SKIP QUESTION
    # ==========================================
    if skip_clicked:
        st.session_state.results.append(
            {
                "skill": current_skill,
                "question": current_question,
                "answer": "Not Attempted",
                "score": 0,
                "emotion": "Not Recorded",
                "emotion_confidence": 0,
                "voice_score": 0,
                "stress": 0,
                "fillers": [],
            }
        )
        st.session_state.question_index += 1
        st.rerun()

    # ==========================================
    # RECORD ANSWER
    # ==========================================
    if record_clicked:
        try:
            # ==========================================
            # RECORD AUDIO
            # ==========================================
            with st.spinner("🎙️ Recording your response..."):
                st.info("🎤 Recording has started. Please answer clearly into your microphone.")
                answer = get_audio_input()

            if answer.strip() == "":
                st.error("❌ No speech detected.")
                return

            st.success("✅ Answer Recorded")
            st.markdown("### 📝 Your Response")
            st.write(answer)
            st.divider()

            # ==========================================
            # EMOTION DETECTION
            # ==========================================
            emotion, confidence = detect_emotion()

            # ==========================================
            # VOICE ANALYSIS
            # ==========================================
            voice_score, fillers = analyze_voice(answer)

            # ==========================================
            # STRESS ANALYSIS
            # ==========================================
            stress = detect_stress(emotion)

            # ==========================================
            # TECHNICAL EVALUATION
            # ==========================================
            score = evaluate(current_question, answer)

            # ==========================================
            # LIVE ANALYTICS
            # ==========================================
            st.markdown("## 📊 Live Interview Analytics")
            
            # Fixed indentation for live analytics columns
            live_c1, live_c2, live_c3, live_c4 = st.columns(4)

            with live_c1:
                st.metric("🎯 Technical", f"{score:.1f}")

            with live_c2:
                st.metric("🎤 Voice", f"{voice_score:.1f}")

            with live_c3:
                st.metric("😊 Emotion", emotion.capitalize())

            with live_c4:
                st.metric("😰 Stress", f"{stress}%")

            st.info(f"Emotion Confidence : {confidence:.2f}%")
            
            if score >= 85:
                st.success("🌟 Excellent Answer")
            elif score >= 70:
                st.info("👍 Good Answer")
            elif score >= 50:
                st.warning("⚠ Average Answer")
            else:
                st.error("❌ Needs Improvement")

            if len(fillers) == 0:
                st.success("No filler words detected.")
            else:
                st.warning(f"⚠️ Filler Words Used ({len(fillers)}): " + ", ".join(fillers))

            st.divider()

            # ==========================================
            # SAVE RESULT
            # ==========================================
            st.session_state.results.append(
                {
                    "skill": current_skill,
                    "question": current_question,
                    "answer": answer,
                    "score": score,
                    "emotion": emotion,
                    "emotion_confidence": confidence,
                    "voice_score": voice_score,
                    "stress": stress,
                    "fillers": fillers,
                }
            )

            st.success("✅ Answer evaluated and saved successfully!")
            st.balloons()
            
            st.session_state.question_index += 1
            st.rerun()

        # ==========================================
        # ERROR HANDLING
        # ==========================================
        except Exception as e:
            st.error("❌ An unexpected error occurred during the interview.")
            st.exception(e)
            st.info("Please try answering the question again.")

            if st.button("🔄 Retry", use_container_width=True):
                st.rerun()