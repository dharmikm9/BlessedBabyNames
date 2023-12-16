import streamlit as st
import streamlit.components.v1 as components

def contactus_page():
    st.title("Developer Contact Info")



    col1, col2 = st.columns([1, 3])

    with col1:
        st.image("https://kit8.net/wp-content/uploads/edd/2022/04/robots_and_humans_communication_preview.jpg",
                 width=200)  # Replace with your image URL
    with col2:
        st.header("Meet the Developer")
        st.write("""
            Hello! I'm Dharmik, a passionate developer interested in Machine Learning & ML.
            Feel free to connect with me through the following social media platforms:
            """)
        
        components.html("""
         <script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
         <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="large" data-theme="light" data-type="VERTICAL" data-vanity="dharmikm9" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/dharmikm9?trk=profile-badge">Dharmik Mehta</a></div>
        """, )
        
        soc_col1, soc_col2 = st.columns([1, 3])

        with soc_col1:
            st.markdown(
                "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/dharmikm9)"
            )
        with soc_col2:
            st.markdown(
                "[![GitHub](https://img.shields.io/badge/GitHub-Profile-lightgrey)](https://github.com/dharmikm9)"
            )
