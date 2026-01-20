import streamlit as st
import random

st.set_page_config(page_title="A-Z Visual Dictionary", page_icon="🎨", layout="wide")

st.title("🔤 Interactive A-Z Dictionary")
st.write("Click any letter to see 3 amazing images starting with that letter!")

alphabet_data = {
    'A': ['Apple', 'Astronaut', 'Airplane'], 'B': ['Balloon', 'Butterfly', 'Bicycle'],
    'C': ['Castle', 'Cat', 'Camera'], 'D': ['Dolphin', 'Desert', 'Diamond'],
    'E': ['Elephant', 'Eagle', 'Earth'], 'F': ['Flower', 'Fire', 'Forest'],
    'G': ['Guitar', 'Galaxy', 'Giraffe'], 'H': ['Hammer', 'Helicopter', 'Horse'],
    'I': ['Ice Cream', 'Island', 'Iguana'], 'J': ['Jungle', 'Jellyfish', 'Jet'],
    'K': ['Kangaroo', 'Keyboard', 'Kite'], 'L': ['Lion', 'Lantern', 'Lighthouse'],
    'M': ['Mountain', 'Moon', 'Monkey'], 'N': ['Night', 'Nature', 'Necklace'],
    'O': ['Ocean', 'Owl', 'Orange'], 'P': ['Panda', 'Parrot', 'Pizza'],
    'Q': ['Queen', 'Quartz', 'Quail'], 'R': ['Robot', 'Rocket', 'Rainbow'],
    'S': ['Spaceship', 'Sunflower', 'Shark'], 'T': ['Tiger', 'Telescope', 'Train'],
    'U': ['Umbrella', 'Universe', 'Unicorn'], 'V': ['Volcano', 'Violin', 'Vulture'],
    'W': ['Waterfall', 'Wolf', 'Watch'], 'X': ['Xylophone', 'X-ray', 'Xenops'],
    'Y': ['Yacht', 'Yak', 'Yoga'], 'Z': ['Zebra', 'Zoo', 'Zigzag']
}

def get_image_url(word):
    seed = random.randint(1, 100000)
    return f"https://image.pollinations.ai/prompt/a_high_quality_photo_of_a_{word.replace(' ', '_')}?width=800&height=600&nologo=true&seed={seed}"

st.subheader("Select a Letter")
letters = list(alphabet_data.keys())
cols1 = st.columns(13)
for i, letter in enumerate(letters[:13]):
    if cols1[i].button(letter):
        st.session_state.selected_letter = letter

cols2 = st.columns(13)
for i, letter in enumerate(letters[13:]):
    if cols2[i].button(letter):
        st.session_state.selected_letter = letter

if 'selected_letter' in st.session_state:
    letter = st.session_state.selected_letter
    items = alphabet_data[letter]
    st.header(f"Showing things for: {letter}")
    col1, col2, col3 = st.columns(3)
    display_cols = [col1, col2, col3]
    for idx, item in enumerate(items):
        with display_cols[idx]:
            img_url = get_image_url(item)
            st.markdown(f"### {item}")
            st.image(img_url, use_container_width=True)
