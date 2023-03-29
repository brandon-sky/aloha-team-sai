import streamlit as st

from typing import List, Tuple

class ScheduleElement:
    """
    A class representing a schedule element, such as a task or event.
    
    Attributes:
    -----------
    text_path : str
        The path to the text file containing the description of the schedule element.
    image_path : str
        The path to the image file representing the schedule element.
    caption : str
        The caption to be displayed under the image.
        
    Methods:
    --------
    show()
        Displays the image and the text description of the schedule element using Streamlit.
    """
    
    def __init__(self, text_path: str, image_path: str, caption: str) -> None:
        self.text_path = text_path
        self.image_path = image_path
        self.caption = caption
        pass
    
    def __get_text(self):
        """
        Reads the text file and sets the `text` attribute.
        """
        with open(self.text_path, "r") as file:
            self.text = file.read()
        return
    
    def show(self):
        """
        Displays the image and the text description of the schedule element using Streamlit.
        """
        self.__get_text()
        st.image(image=self.image_path, caption=self.caption)
        st.markdown(body=self.text)
        return 
    pass


class RecommendBar():

    def __init__(self, 
                 food:List[Tuple[str]], 
                 actions: List[Tuple[str]]) -> None:
        
        self.food = food
        self.actions = actions
        pass

    def show(self):
        with st.expander("Empfehlung"):
            for food_icon, item in self.food:
                st.markdown(f"- {food_icon} {item}")
            for action_icon, action in self.actions:
                st.markdown(f"- {action_icon} {action}")
        return 

    pass