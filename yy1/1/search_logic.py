import json
import os

# 获取当前脚本所在目录
base_dir = os.path.dirname(os.path.abspath(__file__))

# 加载state_t1.json数据
state_file_path = os.path.join(base_dir, 'state_t1.json')
with open(state_file_path, 'r', encoding='utf-8') as f:
    state_data = json.load(f)
    # 处理NaN值
    for item in state_data:
        for key, value in item.items():
            if isinstance(value, float) and value != value:  # 检查是否为NaN
                item[key] = None

def search_schools(area, score, condition):
    """
    根据区域、分数和条件搜索学校
    
    :param area: 区域名称
    :param score: 分数
    :param condition: 条件 ('regular', 'supplement', 'study')
    :return: 符合条件的学校列表
    """
    # 确保分数是数字类型
    try:
        score = float(score)
    except (ValueError, TypeError):
        return []
    
    # 筛选符合条件的学校
    results = []
    
    # 如果选择了全部区域，则不筛选区域
    if area == "all":
        filtered_data = state_data
    else:
        # 根据区域筛选
        filtered_data = [item for item in state_data if item.get("区域") == area]
    
    # 根据不同条件筛选
    if condition == "regular":  # 常规录取
        # 显示小于等于输入分数的所有学校
        results = [item for item in filtered_data if isinstance(item.get("分数"), (int, float)) and item.get("分数") <= score]
    elif condition == "supplement":  # 补录机会
        # 显示大于输入分数的1至20分的所有学校
        results = [item for item in filtered_data if isinstance(item.get("分数"), (int, float)) and item.get("分数") > score and item.get("分数") <= score + 20]
    elif condition == "study":  # 借读可能性
        # 显示大于输入分数的1至50分的所有学校
        results = [item for item in filtered_data if isinstance(item.get("分数"), (int, float)) and item.get("分数") > score and item.get("分数") <= score + 50]
    
    # 按分数排序
    results.sort(key=lambda x: x.get("分数", 0))
    
    return results

# 测试代码
if __name__ == "__main__":
    # 测试常规录取
    print("常规录取测试 (浦东, 690分):")
    schools = search_schools("浦东", 690, "regular")
    for school in schools[:5]:  # 只显示前5个
        print(f"{school['名称']} - {school['区域']} - {school['类型']} - {school['分数']}分")
    
    print("\n补录机会测试 (浦东, 680分):")
    schools = search_schools("浦东", 680, "supplement")
    for school in schools[:5]:  # 只显示前5个
        print(f"{school['名称']} - {school['区域']} - {school['类型']} - {school['分数']}分")
    
    print("\n借读可能性测试 (浦东, 650分):")
    schools = search_schools("浦东", 650, "study")
    for school in schools[:5]:  # 只显示前5个
        print(f"{school['名称']} - {school['区域']} - {school['类型']} - {school['分数']}分")