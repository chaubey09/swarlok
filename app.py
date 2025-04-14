import streamlit as st
import json

# Load mantra data from JSON file
def load_mantras():
    with open("mantras.json", "r", encoding="utf-8") as file:
        return json.load(file)["mantras"]

# Main function to run the app
def main():
    # Center-aligned Title and Subtitle using HTML/CSS
    st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: orange;'>स्वरलोक</h1>
        <h3 style='color: teal;'>ॐ हनुमते नमः।</h3>
    </div>
    """, unsafe_allow_html=True)

    # Add top image (centered and resized)
    st.image("pic.jpg", width=300, caption="Top Image")

    # Load mantras
    mantras = load_mantras()

    # Sidebar for mantra selection (in Hindi)
    st.sidebar.header("मंत्र चुनें")
    selected_mantra = st.sidebar.selectbox("एक मंत्र चुनें", [mantra["name"] for mantra in mantras])

    # Find the selected mantra
    mantra_data = next((mantra for mantra in mantras if mantra["name"] == selected_mantra), None)

    if mantra_data:
        # Display mantra details
        st.subheader(mantra_data["name"])

        # Audio playback (label in Hindi)
        audio_url = mantra_data.get("audio_url", None)
        if audio_url:
            st.write("**मंत्र सुनें:**")
            st.audio(audio_url, format="audio/mp3")

        # Display each verse (doha or chaupai)
        for i, verse in enumerate(mantra_data["verses"], start=1):
            # Replace \n with <br> for proper line breaks in Devanagari script
            devanagari_with_breaks = verse['devanagari'].replace('\n', '<br>')
            styled_devanagari = f"<span style='color: orange; font-size: 18px;'>{devanagari_with_breaks}</span>"
            st.markdown(f"**{i}.** {styled_devanagari}", unsafe_allow_html=True)

            # Meaning in teal color
            styled_meaning = f"<span style='color: teal; font-size: 16px;'>{verse['meaning']}</span>"
            st.markdown(styled_meaning, unsafe_allow_html=True)

            # Add a small space between each verse
            st.markdown("---")

    # Add bottom image (centered and resized)
    st.image("pic2.jpg", width=300, caption="Bottom Image")

# Run the app
if __name__ == "__main__":
    main()