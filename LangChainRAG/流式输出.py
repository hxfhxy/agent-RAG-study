# 聊天模型用法
from langchain_community.chat_models import ChatTongyi

model = ChatTongyi(
    model="qwen-max",
    dashscope_api_key="your_api_key_here"
)

# 调用方式
res = model.stream("你是谁?")
for chunk in res:
    print(chunk, end=" ", flush=True)  # 每一段输出以空格分隔，避免换行)