import streamlit as st
import os

folderpath = "markdown"  # 這是相對路徑, C:\Users\milov\OneDrive\桌面\python-AI\markdown
files = os.listdir(folderpath)  # 列出所有檔案
files_name = []  # 建立空的列表
for f in files:
    if f.endswith(".md"):  # 判斷是否為.md檔案
        files_name.append(f)  # 將檔案名字加入到列表中

for f in files_name:
    with open(f"{folderpath}/{f}", "r", encoding="utf-8") as file:
        content = file.read()  # 讀取檔案內容
        with st.expander(f[:-3]):
            st.markdown(content)  # 將檔案內容加入到Streamlit的區塊中
