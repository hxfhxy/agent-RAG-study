# 聊天模型用法（推荐，适配 qwen-max）
from langchain_community.chat_models import ChatTongyi

model = ChatTongyi(
    model="qwen-max",
    dashscope_api_key="your_api_key_here"
)

# 调用方式
res = model.invoke("你是谁?")
print(res.content)
