import json
import pprint

# 第一题
# def process_json(json_data):
#     result = []
#     for item in json_data:
#         func_name = item["name"]
#         total_time_percentage = item["total_time_percentage"]
#         result.append({"func_name": func_name, "total_time_percentage": total_time_percentage})
#         if "children" in item:
#             children = item["children"]
#             result.extend(process_json(children))
#     return result


# 第二题
# def process_json(json_data):
#     result_dict = {}
#     for item in json_data:
#         func_name = item["name"]
#         total_time_percentage = item["total_time_percentage"]
#         if func_name in result_dict:
#             result_dict[func_name] += total_time_percentage
#         else:
#             result_dict[func_name] = total_time_percentage
#         if "children" in item:
#             children = item["children"]
#             child_result = process_json(children)
#             for child in child_result:
#                 child_func_name = child["func_name"]
#                 child_total_time_percentage = child["total_time_percentage"]
#                 if child_func_name in result_dict:
#                     result_dict[child_func_name] += child_total_time_percentage
#                 else:
#                     result_dict[child_func_name] = child_total_time_percentage
#
#     result = [{"func_name": func_name, "total_time_percentage": total_time_percentage} for
#               func_name, total_time_percentage in result_dict.items()]
#     return result

# 第三题
def process_json(json_data, parent_name=""):
    result = []
    for item in json_data:
        func_name = item["name"]
        total_time_percentage = item["total_time_percentage"]
        # 父级名称 ? 父级名称/自己名称 : 自己名称
        full_name = f"{parent_name}/{func_name}" if parent_name else func_name
        result.append({
            "name": full_name,
            "total_time_percentage": total_time_percentage
        })
        if "children" in item:
            children = item["children"]
            child_result = process_json(children, full_name)
            result.extend(child_result)
    return result

# 读取json数据
with open("func_data_summary.json", "r") as f:
    json_data = json.load(f)

# 处理数据并输出结果
result = process_json(json_data)
pprint.pprint(result)