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
        {"role": "system", "content": "你是ai助理，回答简介."},
        {"role": "user", "content": "小明有两条狗"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有3只猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小明和小红谁的宠物多？"},
    ]
)

#3.处理结果
print(response.choices[0].message.content)