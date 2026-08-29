import json

d={
    "name": "周杰伦",
    "age": 30,
    "gender": "男",
}

s=json.dumps(d,ensure_ascii=False)
print(s)

l=  [
    {
        "name": "周杰伦",
        "age": 30,
        "gender": "男",
    },
    
    {
        "name": "蔡依林",
        "age": 29,
        "gender": "女",
    },

    {
        "name": "hzy",
        "age": 20,
        "gender": "男",
    }
]

print(json.dumps(l,ensure_ascii=False))

json_str='{"name": "周杰伦", "age": 30, "gender": "男"}'
json_arrary_str='[{"name": "周杰伦", "age": 30, "gender": "男"}, {"name": "蔡依林", "age": 29, "gender": "女"}, {"name": "hzy", "age": 20, "gender": "男"}]     '

res_dict=json.loads(json_str)
print(res_dict,type(res_dict))
res_array=json.loads(json_arrary_str)
print(res_array,type(res_array))
