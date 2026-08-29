from openai import OpenAI

client = OpenAI(
    api_key="your_api_key_here",  # 替换为你的实际API Key
    # 旧兼容地址，不需要WorkspaceId，直接复制
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ]
)
print(completion.model_dump_json())
