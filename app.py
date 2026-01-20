import streamlit as st

# Set up the page
st.set_page_config(page_title="A-Z Visual Dictionary", page_icon="🎨", layout="wide")

st.title("🔤 Interactive A-Z Dictionary")
st.write("Click any letter to see 3 amazing images starting with that letter!")

# 1. THE COMPLETE DATASET (A to Z)
alphabet_data = {
    'A': ['Apple', 'Astronaut', 'Airplane'],
    'B': ['Balloon', 'Butterfly', 'Bicycle'],
    'C': ['Castle', 'Cat', 'Camera'],
    'D': ['Dolphin', 'Desert', 'Diamond'],
    'E': ['Elephant', 'Eagle', 'Earth'],
    'F': ['Flower', 'Fire', 'Forest'],
    'G': ['Guitar', 'Galaxy', 'Giraffe'],
    'H': ['Hammer', 'Helicopter', 'Horse'],
    'I': ['Ice Cream', 'Island', 'Iguana'],
    'J': ['Jungle', 'Jellyfish', 'Jet'],
    'K': ['Kangaroo', 'Keyboard', 'Kite'],
    'L': ['Lion', 'Lantern', 'Lighthouse'],
    'M': ['Mountain', 'Moon', 'Monkey'],
    'N': ['Night', 'Nature', 'Necklace'],
    'O': ['Ocean', 'Owl', 'Orange'],
    'P': ['Panda', 'Parrot', 'Pizza'],
    'Q': ['Queen', 'Quartz', 'Quail'],
    'R': ['Robot', 'Rocket', 'Rainbow'],
    'S': ['Spaceship', 'Sunflower', 'Shark'],
    'T': ['Tiger', 'Telescope', 'Train'],
    'U': ['Umbrella', 'Universe', 'Unicorn'],
    'V': ['Volcano', 'Violin', 'Vulture'],
    'W': ['Waterfall', 'Wolf', 'Watch'],
    'X': ['Xylophone', 'X-ray', 'Xenops'],
    'Y': ['Yacht', 'Yak', 'Yoga'],
    'Z': ['Zebra', 'Zoo', 'Zigzag']
}

# 2. HELPER FUNCTION TO GET IMAGES
def get_image_url(word):
    # This fetches a high-quality photo from Unsplash based on the word
    return f"https://source.unsplash.com/800x600/?{word.replace(' ', '')}"

# 3. CREATING THE BUTTON GRID (A-Z)
st.subheader("Select a Letter")
letters = list(alphabet_data.keys())

# Create two rows of 13 buttons
row1 = letters[:13]
row2 = letters[13:]

cols1 = st.columns(13)
for i, letter in enumerate(row1):
    if cols1[i].button(letter):
        st.session_state.selected_letter = letter

cols2 = st.columns(13)
for i, letter in enumerate(row2):
    if cols2[i].button(letter):
        st.session_state.selected_letter = letter

# 4. DISPLAY SECTION
st.divider()

if 'selected_letter' in st.session_state:
    letter = st.session_state.selected_letter
    items = alphabet_data[letter]
    
    st.header(f"Showing things for: {letter}")
    
    col1, col2, col3 = st.columns(3)
    display_cols = [col1, col2, col3]
    
    for idx, item in enumerate(items):
        with display_cols[idx]:
            def get_image_url(word):
    # This uses a newer, more reliable free image service (Pollinations or Lorempixel)
    return f"https://image.pollinations.ai/prompt/a_high_quality_photo_of_a_{word.replace(' ', '_')}?width=800&height=600&nologo=true"
            st.markdown(f"### {item}")
            st.image(img_url, use_column_width=True)
else:
    st.info("Please click a letter button above to start!")

# Footer
st.sidebar.markdown("---")

st.sidebar.write("Created with Python & Streamlit")
