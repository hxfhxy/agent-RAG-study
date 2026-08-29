from openai import OpenAI

client=OpenAI(
    api_key="your_api_key_here",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

example_data={  #示例数据
    '新闻报道':'今日，股市经历新一轮波动，受到宏观经济数据和全球贸易紧张局势影响，投资者情绪谨慎，专家建议关注长期投资价值。',
    '财务报告':'公司第三季度财报显示，营收同比增长15%，净利润增长20%，主要得益于新产品的成功推出和市场拓展。',
    '公司公告':'公司宣布将于下月启动新一轮的市场营销活动，旨在提升品牌知名度和客户参与度，同时计划推出一系列创新产品以满足市场需求。',
    '分析师观点':'最新的行业分析报告指出，科技公司的创新将成为未来的关键，相关企业需要不断创新，以保持竞争优势。投资者应关注行业趋势和企业战略调整。',
}

#分类列表
example_types=['新闻报道','财务报告','公司公告','分析师观点']

#提问数据
question=[
    "今日，央行发布公告宣布降低利率，以刺经济增长。这一降息举措将影响贷款利率，并在未来几个季度可能对金融市场产生深远影响。",
    "ABC公司今日发布公告称，已完成对XYZ公司的收购交易，预计将进一步扩大其市场份额，并提升整体竞争力。",
    "公司资产负债表显示，流动资产同比增长10%，而流动负债保持稳定，反映出公司在财务管理方面的稳健表现。",
    "最新的行业分析报告显示，人工智能技术在医疗领域的应用正在迅速发展，相关企业需要加大研发投入，以保持技术领先地位。",
    "小明喜欢小新"
]

message=[
    {"role": "system", "content": "你是一个金融专家，帮我把下面的内容进行分类，分类类型有：新闻报道、财务报告、公司公告、分析师观点。不清楚的内容请分类为不清楚类别。"},

]
for key,value in example_data.items():
    message.append({"role": "user", "content": value})
    message.append({"role": "assistant", "content": key})

#for x in message:
#    print(x)    

for q in question:
    response = client.chat.completions.create(
        model="qwen3-max",
        messages=message+[{"role": "user", "content":f"按照实例，回答这段文本分类类别{q}"}]
    )

    print(response.choices[0].message.content)