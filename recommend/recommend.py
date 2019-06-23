# 构造一份打分数据集，可以去movielens下载真实的数据做实验
users = {"小明": {"中国合伙人": 5.0, "太平轮": 3.0, "荒野猎人": 4.5, "老炮儿": 5.0, "我的少女时代": 3.0, "肖洛特烦恼": 4.5, "火星救援": 5.0},
         "小红": {"小时代4": 4.0, "荒野猎人": 3.0, "我的少女时代": 5.0, "肖洛特烦恼": 5.0, "火星救援": 3.0, "后会无期": 3.0},
         "小阳": {"小时代4": 2.0, "中国合伙人": 5.0, "我的少女时代": 3.0, "老炮儿": 5.0, "肖洛特烦恼": 4.5, "速度与激情7": 5.0},
         "小四": {"小时代4": 5.0, "中国合伙人": 3.0, "我的少女时代": 4.0, "匆匆那年": 4.0, "速度与激情7": 3.5, "火星救援": 3.5, "后会无期": 4.5},
         "六爷": {"小时代4": 2.0, "中国合伙人": 4.0, "荒野猎人": 4.5, "老炮儿": 5.0, "我的少女时代": 2.0},
         "小李": {"荒野猎人": 5.0, "盗梦空间": 5.0, "我的少女时代": 3.0, "速度与激情7": 5.0, "蚁人": 4.5, "老炮儿": 4.0, "后会无期": 3.5},
         "隔壁老王": {"荒野猎人": 5.0, "中国合伙人": 4.0, "我的少女时代": 1.0, "Phoenix": 5.0, "甄嬛传": 4.0, "The Strokes": 5.0},
         "邻村小芳": {"小时代4": 4.0, "我的少女时代": 4.5, "匆匆那年": 4.5, "甄嬛传": 2.5, "The Strokes": 3.0}
         }
# 定义几种距离计算函数
# 更高效的方式为把得分向量化之后使用scipy中定义的distance方法

# https://blog.csdn.net/cc_want/article/details/85001762
from math import sqrt


def pearson_dis(rating1, rating2):
    """计算2个打分序列间的pearson距离. 输入的rating1和rating2都是打分dict
       格式为{'小时代4': 1.0, '疯狂动物城': 5.0}"""
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]

            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)
    # now compute denominator
    denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator


# 查找最近邻
def computeNearestNeighbor(username, users):
    """在给定username的情况下，计算其他用户和它的距离并排序"""
    print("查找最近邻")
    distances = []
    for user in users:
        if user != username:
            # distance = manhattan_dis(users[user], users[username])

            distance = pearson_dis(users[user], users[username])
            distances.append((distance, user))
    # 根据距离排序，距离越近，排得越靠前
    distances.sort()
    print("distances => ", distances)
    return distances


# 推荐
def recommend(username, users):
    print("输入=》", username)
    """对指定的user推荐电影"""
    # 找到最近邻
    nearest = computeNearestNeighbor(username, users)[0][1]

    recommendations = []
    # 找到最近邻看过，但是我们没看过的电影，计算推荐
    neighborRatings = users[nearest]

    print("nearest -> ", nearest)
    print("neighborRatings -> ", neighborRatings)

    userRatings = users[username]

    print("userRatings -> ", userRatings)
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
    print("recommendations -> ", recommendations)
    results = sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse=True)
    for result in results:
        print(result[0], result[1])


if __name__ == "__main__":
    recommend('小明', users)