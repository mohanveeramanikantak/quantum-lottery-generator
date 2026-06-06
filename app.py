import streamlit as st
from lottery import generate_unique_lottery_numbers, get_lottery_mode

st.set_page_config(
    page_title="Quantum Lottery Generator",
    page_icon="🎰"
)

st.title("🎰 Quantum Lottery Number Generator")

st.write(
    "Generate lottery numbers using quantum randomness powered by Qiskit."
)

mode = st.selectbox(
    "Select Lottery Mode",
    ["Classic 6/49", "Powerball Style", "EuroMillions Style"]
)

settings = get_lottery_mode(mode)

if st.button("Generate Lottery Numbers"):
    numbers = generate_unique_lottery_numbers(
        count=settings["count"],
        min_num=settings["min_num"],
        max_num=settings["max_num"]
    )

    st.subheader("Your Quantum Lottery Numbers")

    st.success("  ".join(str(num) for num in numbers))

    st.write("Generated using quantum superposition and measurement.")