import streamlit as st
from services.auth.login_wall import render_login_wall
from services.state.session_defaults import initial_session_defaults
def main():
    st.set_page_config(
        page_icon="🏋️‍♀️",
        page_title="AI Real-time GYM Coach",
        initial_sidebar_state="expanded",
        layout="centered"
    )

    # load_css(os.path.join(os.getcwd(), "static", "style.css"))
    # inject_local_font(os.path.join(os.getcwd(), "static", "AdobeClean.otf"), "AdobeClean")

    # init_db()

    if not render_login_wall():
        return 
    
    # initial_session_defaults()

    
if __name__ == "__main__":
    main()