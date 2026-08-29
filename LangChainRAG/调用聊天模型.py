from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 得到模型对象
model = ChatTongyi(
    model="qwen-max",
    dashscope_api_key="your_api_key_here"
)

#准备消息列表
messages = [
    SystemMessage(content="你是边塞诗人."),
    HumanMessage(content="写一首唐诗"),
    AIMessage(content="锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。"),
    HumanMessage(content="按照你上一个回复的风格，再写一首唐诗"),
]

#stream执行
res=model.stream(messages)
for chunk in res:
    print(chunk.content, end=" ", flush=True)  # 每一段输出以空格分隔，避免换行