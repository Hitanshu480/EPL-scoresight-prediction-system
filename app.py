import streamlit as st
import numpy as np
from train_model import train_models

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="ScoreSight Prediction System",
    page_icon="⚽",
    layout="centered"
)

# ---------------- LOAD MODELS ----------------
reg_model, clf_model, scaler, features, df = train_models("epl_players.csv")

# Dummy team list (replace later with real teams if needed)
teams = sorted(df["Club"].dropna().unique())

# ---------------- TITLE ----------------
st.markdown("## ⚽ ScoreSight Prediction System")
st.markdown("---")

# ---------------- TABS ----------------
tab1, tab2 = st.tabs(["🏟️ Match Prediction", "🧑‍💼 Player Prediction"])

# ======================================================
# 🏟️ MATCH PREDICTION TAB
# ======================================================
with tab1:
    st.subheader("Match Outcome Prediction")

    col1, col2 = st.columns(2)
    with col1:
        home_team = st.selectbox("Home Team", teams)
    with col2:
        away_team = st.selectbox("Away Team", teams)

    st.markdown("### 📊 Predicted Outcome")

    # ---------- PLACEHOLDER PROBABILITIES ----------
    # (Replace with real ML probabilities later)
    home_win_prob = np.random.randint(40, 70)
    away_win_prob = 100 - home_win_prob

    col3, col4 = st.columns(2)
    with col3:
        st.metric(label="🏠 Home Team Wins", value=f"{home_win_prob}%")
    with col4:
        st.metric(label="🚗 Away Team Wins", value=f"{away_win_prob}%")

    st.markdown("")

    if st.button("🔮 Predict Match"):
        if home_team == away_team:
            st.warning("Please select different teams")
        else:
            if home_win_prob > away_win_prob:
                st.success(f"🏆 {home_team} is more likely to WIN")
            else:
                st.success(f"🏆 {away_team} is more likely to WIN")

# ======================================================
# 🧑‍💼 PLAYER PREDICTION TAB
# ======================================================
with tab2:
    st.subheader("Player Performance Prediction")

    player = st.selectbox("Select Player", df["Name"].unique())

    row = df[df["Name"] == player].iloc[0]
    X_input = [[row[f] for f in features]]
    X_scaled = scaler.transform(X_input)

    predicted_goals = reg_model.predict(X_scaled)[0]
    performance = clf_model.predict(X_scaled)[0]

    st.markdown("### 📈 Prediction Result")
    st.write(f"⚽ **Predicted Goals:** `{round(predicted_goals, 2)}`")

    if performance == 1:
        st.success("🔥 High Performance Player")
    else:
        st.warning("⚠️ Average Performance Player")
