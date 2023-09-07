import os
import streamlit as st


def app():
    """
    汇集温暖瞬间
    """

    ##############################################################
    st.write("## 💝 环保素材库")
    
    st.info("""
             **环境需要你我的保护.**
            
             
             """)
    st.write(".")
    
    # num_ls =10
    cols = st.columns(5)

    files = [file for file in os.listdir("pic_gallery") if file.startswith("pic")]
    j = 0
    for f in files:
        cols[j].image(f"pic_gallery/{f}", use_column_width=True) 
        j+=1
        if j>=5:
            j=0

    st.write('---')
    
    
    st.write("## 视频demo")
    cols = st.columns(2)
    cols[1].video("demo/env2.mp4")
    cols[0].video("demo/env4.mp4")




