import streamlit as st
from metrics.meta import meta_info

from data.SchedulePage import ScheduleElement, RecommendBar


def main():
    meta_info()
    st.header("Waimea Bay Beach 🌅🏖️")
    st.info("Sunset Beach at North Shore")

    info = ScheduleElement(
        text_path="texts/08_waimea.md",
        image_path="images/sunset_beach.jpg",
        caption="Sunset.",
    )
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
        actions=[("🏖️ ", "Waimea Beach ")],
    )
    reco.show()
    info.show()
    st.image("images/food_garlic_shrimp.jpg", caption="Giovanni's Shrimp Truck")
    return


if __name__ == "__main__":
    main()
