import streamlit as st
import random

st.set_page_config(page_title="AI Alphabet", page_icon="🎨", layout="wide")

st.title("🔤 Interactive AI Dictionary")
st.write("Click a letter to see 3 AI images!")

# 1. The Dictionary of Words
data = {
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

# 2. The Fixed Image Link (Added model=flux)
def get_image(word):
    seed = random.randint(1, 100000)
    # Adding 'model=flux' is the secret fix for 2026!
    return f"https://image.pollinations.ai/prompt/a_photo_of_{word}?width=800&height=600&seed={seed}&model=flux"

# 3. The Buttons
st.subheader("Select a Letter")
letters = list(data.keys())
rows = [letters[:13], letters[13:]]

for row in rows:
    cols = st.columns(13)
    for i, letter in enumerate(row):
        if cols[i].button(letter, key=letter):
            st.session_state.choice = letter

# 4. Show the Images
if 'choice' in st.session_state:
    letter = st.session_state.choice
    st.header(f"Results for {letter}")
    img_cols = st.columns(3)
    for idx, item in enumerate(data[letter]):
        with img_cols[idx]:
            st.write(f"### {item}")
            # This will show a spinner while the AI draws
            with st.spinner("Drawing..."):
                st.image(get_image(item), use_container_width=True)
