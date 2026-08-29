from langchain_community.embeddings import DashscopeEmbeddings

# 得到模型对象 不传model参数，默认使用dashscope-embedding
model = DashscopeEmbeddings(
    model="dashscope-embedding",
    dashscope_api_key="your_api_key_here"
)

#不用invoke stream
print(model.embed_query("我喜欢你"))  # 直接返回向量
print(model.embed_documents(["我喜欢你", "我稀饭你","晚上吃啥"]))  # 直接返回向量列表