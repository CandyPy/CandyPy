import streamlit as st

st.set_page_config(page_title='猫咪站', page_icon='😸')

# 设置页面标题
st.title("🐈️猫咪图片切换展示")

# 定义图片路径和对应的图注（至少3张）
image_data = [
    {"path": "https://ts1.tc.mm.bing.net/th/id/R-C.3235e35c59459ba396345c3407885c20?rik=epyDRPA5AhIWqA&riu=http%3a%2f%2fimages.muzisucai.com%2fdata%2fattachment%2fforum%2f202402%2f24%2f134207da0fy559zemg8dva.png&ehk=TsNraHtYLHOcMA03BDGZrinUqVLJNVJAqhvvkUFW1ig%3d&risl=&pid=ImgRaw&r=0", "caption": "小猫咪1"},
    {"path": "https://ts1.tc.mm.bing.net/th/id/R-C.fc9bad1c8ba518d3aaf27167b624100b?rik=feGv5uTVHDJLWQ&riu=http%3a%2f%2fwww.talkimages.cn%2fimages%2fmedium%2f20133087%2ftkf003_985763.jpg&ehk=viRY%2f8eNS6b0vWkvra3PzWIE285iKHqbaU6lvu%2bKum4%3d&risl=&pid=ImgRaw&r=0", "caption": "小猫咪2"},
    {"path": "https://pic2.zhimg.com/v2-b6399145c80f909e020874d3c670ae44_r.jpg?source=1940ef5c", "caption": "小猫咪3"}
]
total_imgs = len(image_data)

# 初始化session_state，记录当前显示的图片索引
if "current_idx" not in st.session_state:
    st.session_state.current_idx = 0

# 定义“上一张”按钮的逻辑函数
def prev_img():
    st.session_state.current_idx = (st.session_state.current_idx - 1) % total_imgs

# 定义“下一张”按钮的逻辑函数
def next_img():
    st.session_state.current_idx = (st.session_state.current_idx + 1) % total_imgs

# 显示当前图片和图注
current_img = image_data[st.session_state.current_idx]
st.image(current_img["path"], caption=current_img["caption"])

# 按钮行（控制切换：和参考图样式一致，用函数绑定+use_container_width=True）
col1, col2 = st.columns(2)

with col1:
    # 按钮占满列宽，绑定上一张函数
    st.button("上一张", use_container_width=True, on_click=prev_img)

with col2:
    # 按钮占满列宽，绑定下一张函数
    st.button("下一张", use_container_width=True, on_click=next_img)
