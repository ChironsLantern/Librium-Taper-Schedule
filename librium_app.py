import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Librium Detox Scheduler")

st.title("Librium Detox Schedule Calculator ️")

st.write("""
Enter the **date and time** of the first 50 mg dose below.
This website will automatically generate the full Librium taper schedule.
""")

# User input fields (ON THE WEBSITE)
start_date = st.date_input("📅 Date of first 50 mg dose")
start_time = st.time_input("⏰ Time of first 50 mg dose in military time")

# Librium taper schedule
schedule = [
    ("50 mg", 0),
    ("25 mg", 6),
    ("25 mg", 6),
    ("25 mg", 6),
    ("25 mg", 8),
    ("25 mg", 8),
    ("25 mg", 8),
    ("10 mg", 6),
    ("10 mg", 6),
    ("10 mg", 6),
    ("10 mg", 6),
    ("10 mg", 12),
    ("10 mg", 12),
]

# When user presses the button:
if st.button("Generate Schedule"):
    start_dt = datetime.combine(start_date, start_time)
    current = start_dt
    results = []

    for i, (dose, hours_after) in enumerate(schedule, start=1):
        if hours_after != 0:
            current += timedelta(hours=hours_after)
        results.append({
            "Dose #": i,
            "Dose": dose,
            "Date/Time": current.strftime("%Y-%m-%d %I:%M %p")
        })

    st.subheader("📋 Librium Administration Times")
    st.table(results)
    st.success("Schedule generated successfully.")
