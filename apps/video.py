import os
import streamlit as st
import pandas as pd
import cv2
import tempfile
import numpy as np 

from generate_video import generate


# 创建一个函数来处理上传的视频文件
def process_video(video_file):
    # 将上传的视频文件读取为字节流
    
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())

    cap = cv2.VideoCapture(tfile.name)  
    return cap


# 创建一个函数来处理上传的图像
def process_image(uploaded_image):
    # 使用BytesIO读取上传的图像文件
    image_bytes = uploaded_image.read()
    # 将字节数据转换为NumPy数组
    image_np = np.frombuffer(image_bytes, np.uint8)
    # 使用OpenCV将NumPy数组解码为图像
    image_cv = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    
    return image_cv


def app():
    """
    环境保护视频替换.
    """
    
    st.sidebar.write("# 💟 科技赋能环保")
    # 允许用户上传视频文件
    inp_video = st.sidebar.file_uploader("上传原始视频", type=["mp4", "avi"],key=1)   
    # 允许用户上传图像
    sub_image = st.sidebar.file_uploader("原视频中要替换的内容", type=["jpg", "jpeg", "png"],key=2)

    sub_video = st.sidebar.file_uploader("上传替换的图片或视频", type=["jpg", "jpeg", "png","mp4", "avi"],key=3)

    files = [file for file in os.listdir("pic_gallery") if file.startswith("pic")]
    sub_image_select = st.sidebar.selectbox("选择替换的视频", index=0,options=files, key=4)

    st.info("""
            **科技赋能环保，提高环保意识!**
            
            - 为地球减负我是践行者
            减少能源排放。 
            为地球的环境出一份力。 
            关爱地球关爱家园、保护海洋环境。

             """)
    
#     st.markdown("""
# ### 背景
    
# - 8月24号日本正式向大海排放核废水。 
# - 视频博主被日本核废水话题被限流。

# 因此就有了开发这个项目的冲动，我们也想为环保做一些自己的事情。
        

# ##### 服务对象：
# 视频博主 （环保理念）

# 我们用技术手段，来为他们的视频增加一点 “环保” , 不被限流               

# ##### 开发理念
                
# **环保不适合商业广告的频重复**

# 环保意识的培养不在于声音大， 而在与频率高  
# 我们目标是通过为博主的视频中无痕添加一些环保元素，**弱化说教**味道，将环保从言传向身教转变。
# 主打一个**潜移默化**。

                
# ##### 技术选型
                
# 视频元素替换模型 中的 佼佼者——NeuralMarker
                
# 前端轻量化框架————streamlit           
# """)


    st.write('---')
    col1, col2 = st.columns(2)

    with col1:
        st.write("### 🥫 为视频加点 环保 🥫")
        st.info(f"""
        - 科技赋能环保，提高环保意识.
        """)
        st.markdown("""

        """)

        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")



    with col2:
        inp_video1 = None
        if inp_video is not None:
            st.video(inp_video)
            inp_video1 = process_video(inp_video)
        else:
            # video_name = "demo/home3.mp4"
            video_name = "demo/scene.mp4"
            st.video(video_name)
            inp_video1 = cv2.VideoCapture(video_name)

    st.write('---')
    st.sidebar.write("---")
    col3, col4 = st.columns(2)
    image_cv = None
    sub_video1 = None
    
    if sub_image is not None:
        # 显示上传的图像
        col3.image(sub_image, caption="上传的图像", use_column_width=False,width=300)
        image_cv = process_image(sub_image)
    else:
        img_path = "demo/fantastic_beast.jpg"
        # img_path = "demo/base.png"

        col3.image(img_path, caption="上传的图像", use_column_width=False,width=300)
        image_cv = cv2.imread(img_path)

    if sub_video is not None:
        if sub_video.name.split(".")[-1] in ['jpg','png','jpeg']:
            col4.image(sub_video, caption="上传的图像", use_column_width=False,width=300)
            sub_video1 = process_image(sub_video)
            sub_video=False
        else:
            col4.video(sub_video)
            # 显示上传的视频文件信息
            st.write("上传替换的视频文件：", sub_video.name)
            st.write("视频文件大小：", round(sub_video.size / (1024 * 1024), 2), "MB")
            sub_video1 = process_video(sub_video)
            sub_video=True
    else:
        filename = f"pic_gallery/{sub_image_select}"
        # col4.write(f'<video height="400" controls><source src="{demo_path}" type="video/mp4"></video>', unsafe_allow_html=True)
        col4.image(filename, caption="上传的图像", use_column_width=False,width=300)
        sub_video1 = cv2.imread(filename)
        sub_video=False

    st.write('---')

    st.write("## 视频处理")
    if  st.button("开始处理"):
        if (inp_video1 is not None) & (image_cv is not None) & (sub_video1 is not None):
            st.write(" 视频处理中.....")
            result = generate(inp_video1,image_cv,sub_video1,sub_video,movie_start_idx = 0,movie_end_idx=5,scene_start_idx=0,scene_end_idx=5)
            if result:
                st.video(result)
                st.info("视频完成啦~")


    