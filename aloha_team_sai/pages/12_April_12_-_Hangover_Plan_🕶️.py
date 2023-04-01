import streamlit as st

from data.SchedulePage import ScheduleElement, RecommendBar
from metrics.meta import meta_info


def main():
    meta_info()
    st.header("The Hangover Plan 🕶️")
    st.info(
        "Hangover Plan: Gutes Frühstück, strahlende Sonne, leckeres Eis und eine tolle Aussicht"
    )

    reco = RecommendBar(
        food=[("🥞😊", "Macademia Nut Panecakes"), ("🍨🌈", "Shave Ice")],
        actions=[("🏖️", "Kailua Beach Park"), ("🥾", "Pillbox Hike")],
    )
    reco.show()
    info = ScheduleElement(
        text_path="texts/12_kailua.md",
        image_path="images/pillbox_2.jpg",
        caption="Easy day in Kailua.",
    )
    info.show()
    st.image("images/shave_ice.jpg", caption="Delicious shave ice.")
    st.image("images/kaili.jpg", caption="Easy day at Kailua Beach.")


if __name__ == "__main__":
    main()
