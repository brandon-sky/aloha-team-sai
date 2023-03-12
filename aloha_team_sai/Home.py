import streamlit as st


def meta_info():
    st.set_page_config(
    page_title="#AlohaTeamSai",
    page_icon="🍍",
    # layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        # 'Get Help': 'https://www.extremelycoolapp.com/help',
        # 'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "Lord have mercy. ChatGPT was the main contributor."
    }
)
    return 


def main():
    meta_info()
    st.image("images/kaneohe.jpg")
    st.title("🌺 Aloha Famile & Freunde")
    st.markdown("""
    
    Wir freuen uns, dass ihr hier seid, um uns auf unserer Reise nach O'ahu, Hawaii zu begleiten.

    Hawaii ist ein wunderschönes Reiseziel und wir möchten euch mit Tipps und Empfehlungen unterstützen, 
    damit ihr eure Zeit auf der Insel so gut wie möglich genießen könnt. Auf unserer Website findet ihr auch einen Zeitplan für die Hochzeit und andere Aktivitäten, 
    die während unseres Aufenthalts auf Hawaii stattfinden werden.

    Wir sind überwältigt, dass so viele Menschen den Weg nach Hawaii auf sich nehmen, um uns an diesem besonderen Tag zu begleiten. 
    Wir freuen uns sehr darauf, diese unvergesslichen Erinnerungen mit euch zu teilen.

    Also, macht es euch gemütlich und erkundet die Website! 
    
    Wir können es kaum erwarten, euch auf Hawaii begrüßen zu dürfen. 

    Mahalo,   
    **Monika & Brandon**
    """)
    st.subheader("#AlohaTeamSai!")
    return


if __name__ == "__main__":
    main()
