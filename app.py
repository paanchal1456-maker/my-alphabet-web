import streamlit as st
import random

# 1. Page Setup
st.set_page_config(page_title="Alphabet AI Dictionary", page_icon="📚", layout="wide")

st.title("🎨 My Interactive AI Dictionary")
st.write("Click a letter below to see the AI generate 3 unique images for that letter!")

# 2. Data
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

# 3. Reliable Image Function
def get_ai_image(word):
    # We use 'nologo' and a specific model to make it more professional for your project
    seed = random.randint(1, 999999)
    return f"https://image.pollinations.ai/prompt/a_vibrant_professional_photo_of_a_{word}?width=800&height=600&seed={seed}&nologo=true&model=flux"

# 4. Alphabet Buttons
st.subheader("Select a Letter")
letters = list(alphabet_data.keys())
row1 = st.columns(13)
for i, letter in enumerate(letters[:13]):
    if row1[i].button(letter, key=f"top_{letter}"):
        st.session_state.sel = letter

row2 = st.columns(13)
for i, letter in enumerate(letters[13:]):
    if row2[i].button(letter, key=f"bot_{letter}"):
        st.session_state.sel = letter

# 5. Display Area
if 'sel' in st.session_state:
    current_letter = st.session_state.sel
    st.divider()
    st.header(f"Results for Letter: {current_letter}")
    
    # This creates a nice loading effect
    with st.status(f"Drawing images for {current_letter}...", expanded=True) as status:
        cols = st.columns(3)
        items = alphabet_data[current_letter]
        
        for idx, item in enumerate(items):
            with cols[idx]:
                st.subheader(item)
                # We add a unique key to the image to force it to refresh
                st.image(get_ai_image(item), use_container_width=True)
        status.update(label="Images Loaded Successfully!", state="complete")
    
    st.balloons() # This adds a "celebration" effect when it works!
