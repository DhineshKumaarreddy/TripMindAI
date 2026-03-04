import re
import streamlit as st
from ai_engine import generate_itinerary
from pdf_generator import create_pdf


# -------------------------------
# Budget Calculation Function
# -------------------------------

def calculate_total(itinerary_text, days):
    def get_first_amount(pattern, text):
        match = re.search(pattern, text, re.I)
        if match:
            amount_str = match.group(1).replace(",", "")
            return int(amount_str)
        return 0

    intercity = get_first_amount(
        r"Intercity Travel Cost:\s*(?:INR|₹)\s*([\d,]+)",
        itinerary_text
    )

    accommodation = get_first_amount(
        r"Accommodation Cost:\s*(?:INR|₹)\s*([\d,]+)",
        itinerary_text
    )

    day_costs = re.findall(
        r"Per-day cost.*?:\s*(?:INR|₹)\s*([\d,]+)",
        itinerary_text,
        re.I
    )

    daily_sum = sum(int(val.replace(",", "")) for val in day_costs)

    total_budget = intercity + accommodation + daily_sum
    per_day = total_budget // days if days else 0

    return total_budget, per_day


# -------------------------------
# Streamlit Page Setup
# -------------------------------

st.set_page_config(page_title="TripMind AI", layout="centered")

st.title("🌍 TripMind AI – Smart Travel Planner")
st.markdown("---")


# -------------------------------
# User Inputs
# -------------------------------

destination = st.text_input("Destination")
days = st.number_input("Days", 1, 15, 3)
budget = st.selectbox("Budget", ["Low", "Medium", "Luxury"])
style = st.selectbox("Travel Style", ["Relaxed", "Balanced", "Packed"])
traveler_type = st.selectbox("Traveling As", ["Solo", "Couple", "Friends", "Family"])
interests = st.text_input("Interests (Food, Nature, Adventure...)")
start_city = st.text_input("Starting City")


# -------------------------------
# Session State Initialization
# -------------------------------

if "itinerary" not in st.session_state:
    st.session_state.itinerary = None

if "total_budget" not in st.session_state:
    st.session_state.total_budget = None

if "per_day_budget" not in st.session_state:
    st.session_state.per_day_budget = None


# -------------------------------
# Generate Button
# -------------------------------

if st.button("Generate My Trip"):
    with st.spinner("Designing your perfect trip..."):
        itinerary = generate_itinerary(
            destination,
            days,
            budget,
            style,
            interests,
            start_city,
            traveler_type
        )

        total, per_day = calculate_total(itinerary, days)

        st.session_state.itinerary = itinerary
        st.session_state.total_budget = total
        st.session_state.per_day_budget = per_day


# -------------------------------
# Display Results
# -------------------------------

if st.session_state.itinerary:

    st.markdown("### 🗺 Your Smart Travel Plan")
    st.markdown(st.session_state.itinerary)

    st.markdown(f"""
### 💰 Budget Breakdown
- Estimated Per Day: ₹{st.session_state.per_day_budget}
- Total Estimated Cost: ₹{st.session_state.total_budget}
""")

    # -------------------------------
    # Relax / Packed Buttons
    # -------------------------------

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Make It More Relaxed"):
            new_itinerary = generate_itinerary(
                destination,
                days,
                budget,
                "Relaxed",
                interests,
                start_city,
                traveler_type
            )

            total, per_day = calculate_total(new_itinerary, days)

            st.session_state.itinerary = new_itinerary
            st.session_state.total_budget = total
            st.session_state.per_day_budget = per_day

    with col2:
        if st.button("Make It More Packed"):
            new_itinerary = generate_itinerary(
                destination,
                days,
                budget,
                "Packed",
                interests,
                start_city,
                traveler_type
            )

            total, per_day = calculate_total(new_itinerary, days)

            st.session_state.itinerary = new_itinerary
            st.session_state.total_budget = total
            st.session_state.per_day_budget = per_day


    # -------------------------------
    # Premium PDF Download
    # -------------------------------
if st.button("Download Premium PDF (₹99)"):
    filename = create_pdf(
        st.session_state.itinerary,
        st.session_state.total_budget,
        st.session_state.per_day_budget
    )

    with open(filename, "rb") as file:
        st.download_button(
            label="Click Here to Download",
            data=file,
            file_name="TripMind_Premium_Itinerary.pdf",
            mime="application/pdf"
        )