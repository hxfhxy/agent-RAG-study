from openai import OpenAI
#1.获取client对象。Openai类对象
client=OpenAI(
    api_key="your_api_key_here",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

#2.调用模型
response=client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "你是python专家，不说废话."},
        {"role": "assistant", "content": "我是python专家，有什么可以帮助你的吗？"},
        {"role": "user", "content": "简单字典范例"},
    ],
    stream=True  #开启流式输出，返回一个迭代器对象
)

#3.处理结果
for chunk in response:
    print(chunk.choices[0].delta.content, 
          end=" ", #每一段输出以空格分隔，避免换行
          flush=True #立即刷新输出缓冲区，保证实时输出
    )