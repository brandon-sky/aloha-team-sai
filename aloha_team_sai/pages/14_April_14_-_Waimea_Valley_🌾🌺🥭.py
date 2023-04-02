import streamlit as st

from data.SchedulePage import ScheduleElement, RecommendBar
from metrics.meta import meta_info


def main():
    meta_info()
    st.header("Exploring Waimea Valley 🌾🌺🥭")

    reco = RecommendBar(
        food=[
            (
                "🌮",
                "Fish Tacos essen bei [North Shore Tacos](https://northshoretacos.com/)",
            ),
            (
                "🦐",
                "Shrimps essen bei [Giovanni Shrimp Truck](https://goo.gl/maps/U9UbECZC4BHFzmNP7) oder [Romy's](https://goo.gl/maps/YSfGFqQc9eoL84vz8)",
            ),
        ],
        actions=[("🥾", "Waimea Valley"), ("🏖️", "Waimea Bay Beach ")],
    )
    reco.show()
    info = ScheduleElement(
        text_path="texts/14_waimea_valley.md",
        image_path="images/waimea_valley.jpg",
        caption="Während der Wanderung im Wasser abkühlen.",
    )
    info.show()


if __name__ == "__main__":
    main()
