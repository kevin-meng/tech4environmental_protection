# -*- coding:utf-8 -*-
# 环保有你有我!!!
import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu

from apps import video, love


st.set_page_config(page_title="环保有你我", page_icon="💗", layout="wide",
                             )
image = Image.open("./static/sea.jpg")
st.image(image,caption="",use_column_width='always')  

apps = [
    # 解除注释可显示完整站点    
    {"func": video.app, "title": "视频合成", "icon": "map"},
    {"func": love.app, "title": "环保素材库", "icon": "house"},
]

titles = [app["title"] for app in apps]
icons = [app["icon"] for app in apps]
params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles.index(params["page"][0].lower()))
else:
    default_index = 0
    
selected = option_menu(
            None, 
            options=titles,
            icons=icons,
            menu_icon="cast",
            default_index=default_index,
            orientation="horizontal",
            styles={# "container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"font-size": "14px", "margin":"0px",},  # "color": "orange", 
                    "nav-link": {"font-size": "14px", "text-align": "center", "margin":"0px",
                                 "padding":"10px 0px 10px 0px", },  # "--hover-color": "#eee"
                    # "nav-link-selected": {"background-color": "green"},
                    }
        )


for app in apps:
    if app["title"] == selected:
        app["func"]()
        break




