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
    ]
)

#3.处理结果
print(response.choices[0].message.content)