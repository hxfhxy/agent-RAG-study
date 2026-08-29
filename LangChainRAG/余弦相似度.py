def get_dot(vec_a, vec_b):
    """计算两个向量的点积，2个向量同纬度的元素相乘后求和"""
    if len(vec_a) != len(vec_b):
        raise ValueError("两个向量的维度不一致，无法计算点积")

    dot_sum=0
    for a, b in zip(vec_a, vec_b):
        dot_sum += a * b

    return dot_sum

def get_norm(vec):
    """计算向量的模长，向量每个元素平方后求和再开方"""
    norm_sum=0
    for v in vec:
        norm_sum += v ** 2

    return norm_sum ** 0.5

def cosine_similarity(vec_a, vec_b):
    """计算两个向量的余弦相似度"""
    dot_product = get_dot(vec_a, vec_b)
    norm_a = get_norm(vec_a)
    norm_b = get_norm(vec_b)

    if norm_a == 0 or norm_b == 0:
        raise ValueError("向量的模长为零，无法计算余弦相似度")

    result = dot_product / (norm_a * norm_b)
    print(f"余弦相似度计算结果: {result}")

if __name__ == "__main__":
    vec_a = [0.5, 0.5]
    vec_b = [0.7, 0.7]
    vec_c = [0.7, 0.5]
    vec_d = [-0.6, -0.5]
    print("a与b的余弦相似度:")
    print(cosine_similarity(vec_a, vec_b))
    print("a与c的余弦相似度:")
    print(cosine_similarity(vec_a, vec_c))
    print("a与d的余弦相似度:")
    print(cosine_similarity(vec_a, vec_d))
