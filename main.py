import streamlit as st

# Set Streamlit page configuration
st.set_page_config(
    page_title="Content Creator App",
    page_icon="📷",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Define a pink and white theme
page_bg = "pink"
font_color = "white"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {page_bg};
        color: {font_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Age Check Dialog
if "age_verified" not in st.session_state:
    st.session_state.age_verified = False

if not st.session_state.age_verified:
    if st.button("I am 15 or older"):
        st.session_state.age_verified = True
    else:
        webbrowser.open("https://www.google.com")
    st.stop()

# Sidebar with page navigation
st.sidebar.title("Navigation")
st.sidebar.write("Select a page:")
page = st.sidebar.radio("Go to", ("Home", "Gallery", "More Links"))

# Define Home Page
if page == "Home":
    st.title("Welcome to the Content Creator App")
    st.write("A small bio goes here about who you are, what you do, and other relevant information to introduce yourself.")

# Define Gallery Page
elif page == "Gallery":
    st.title("Gallery")
    media_type = st.radio("Select media type to display:", ("Images and Videos", "Images only", "Videos only"))
    
    if media_type == "Images and Videos":
        st.write("Displaying all images and videos.")
        # Sample display for Images and Videos (Replace with your actual media)
        st.image("https://via.placeholder.com/300x200", caption="Sample Image")
        st.video("https://www.youtube.com/watch?v=2Xc9gXyf2G4")
    elif media_type == "Images only":
        st.write("Displaying images only.")
        # Sample Images (Replace with your actual media)
        st.image("https://via.placeholder.com/300x200", caption="Sample Image")
        st.image("https://via.placeholder.com/300x200", caption="Sample Image 2")
    elif media_type == "Videos only":
        st.write("Displaying videos only.")
        # Sample Videos (Replace with your actual media)
        st.video("https://www.youtube.com/watch?v=2Xc9gXyf2G4")
        st.video("https://www.youtube.com/watch?v=2Xc9gXyf2G4")

# Define More Links Page
elif page == "More Links":
    st.title("More Links")
    st.write("Check out these links to stay connected!")
    st.markdown("[Instagram](https://www.instagram.com)")
    st.markdown("[YouTube](https://www.youtube.com)")
    st.markdown("[Twitter](https://www.twitter.com)")
    st.markdown("[Facebook](https://www.facebook.com)")
