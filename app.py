import streamlit as st
import os

# 1. Page Configuration
st.set_page_config(page_title="My Alphabet Dictionary", page_icon="📚", layout="wide")

st.title("📚 My Alphabet Dictionary")
st.write("Click a letter to see the images I uploaded!")

# 2. Your Image Dictionary 
# IMPORTANT: Make sure these names match your files in the 'images' folder EXACTLY.
alphabet_data = {
    'A': ['apple.jpg', 'astronaut.jpg', 'airplane.jpg'],
    'B': ['balloon.jpg', 'butterfly.jpg', 'bicycle.jpg'],
    'C': ['castle.jpg', 'cat.jpg', 'camera.jpg'],
    'D': ['dolphin.jpg', 'desert.jpg', 'diamond.jpg'],
    'E': ['elephant.jpg', 'eagle.jpg', 'earth.jpg'],
    'F': ['flower.jpg', 'fire.jpg', 'forest.jpg'],
    'G': ['guitar.jpg', 'galaxy.jpg', 'giraffe.jpg'],
    'H': ['hammer.jpg', 'helicopter.jpg', 'horse.jpg'],
    'I': ['ice_cream.jpg', 'island.jpg', 'iguana.jpg'],
    'J': ['jungle.jpg', 'jellyfish.jpg', 'jet.jpg'],
    'K': ['kangaroo.jpg', 'keyboard.jpg', 'kite.jpg'],
    'L': ['lion.jpg', 'lantern.jpg', 'lighthouse.jpg'],
    'M': ['mountain.jpg', 'moon.jpg', 'monkey.jpg'],
    'N': ['night.jpg', 'nature.jpg', 'necklace.jpg'],
    'O': ['ocean.jpg', 'owl.jpg', 'orange.jpg'],
    'P': ['panda.jpg', 'parrot.jpg', 'pizza.jpg'],
    'Q': ['queen.jpg', 'quartz.jpg', 'quail.jpg'],
    'R': ['robot.jpg', 'rocket.jpg', 'rainbow.jpg'],
    'S': ['spaceship.jpg', 'sunflower.jpg', 'shark.jpg'],
    'T': ['tiger.jpg', 'telescope.jpg', 'train.jpg'],
    'U': ['umbrella.jpg', 'universe.jpg', 'unicorn.jpg'],
    'V': ['volcano.jpg', 'violin.jpg', 'vulture.jpg'],
    'W': ['waterfall.jpg', 'wolf.jpg', 'watch.jpg'],
    'X': ['xylophone.jpg', 'x-ray.jpg', 'xenops.jpg'],
    'Y': ['yacht.jpg', 'yak.jpg', 'yoga.jpg'],
    'Z': ['zebra.jpg', 'zoo.jpg', 'zigzag.jpg']
}

# 3. Alphabet Buttons
st.subheader("Select a Letter")
letters = list(alphabet_data.keys())

# Row 1: A to M
cols1 = st.columns(13)
for i, letter in enumerate(letters[:13]):
    if cols1[i].button(letter, key=f"btn_{letter}"):
        st.session_state.selected_letter = letter

# Row 2: N to Z
cols2 = st.columns(13)
for i, letter in enumerate(letters[13:]):
    if cols2[i].button(letter, key=f"btn_{letter}"):
        st.session_state.selected_letter = letter

# 4. Display Logic
if 'selected_letter' in st.session_state:
    letter = st.session_state.selected_letter
    st.divider()
    st.header(f"Showing items for: {letter}")
    
    items = alphabet_data[letter]
    col1, col2, col3 = st.columns(3)
    display_cols = [col1, col2, col3]
    
    for idx, filename in enumerate(items):
        with display_cols[idx]:
            # This makes the label look nice (e.g., 'apple.jpg' -> 'Apple')
            label = filename.split('.')[0].replace('_', ' ').capitalize()
            st.markdown(f"### {label}")
            
            # The path to your image in the GitHub folder
            img_path = f"images/{filename}"
            
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            else:
                st.error(f"Cannot find '{filename}' in the images folder. Check the spelling!")

st.balloons()
