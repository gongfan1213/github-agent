# JSON 工具方法文档

本文档详细说明了项目中使用的 JSON 相关工具方法。

## 1. 文件操作

### 1.1 读取 JSON 文件
```python
def read_json_file(file_path):
    """
    读取 JSON 文件并返回解析后的数据
    
    参数:
        file_path (str): JSON 文件路径
        
    返回:
        dict/list: 解析后的 JSON 数据，如果出错则返回空字典
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
```

### 1.2 写入 JSON 文件
```python
def write_json_file(file_path, data):
    """
    将数据写入 JSON 文件
    
    参数:
        file_path (str): 目标文件路径
        data (dict/list): 要写入的数据
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"写入文件时发生错误: {e}")
```

## 2. 数据解析

### 2.1 解析 JSON 字符串
```python
def parse_json_data(json_str):
    """
    解析 JSON 字符串
    
    参数:
        json_str (str): JSON 格式的字符串
        
    返回:
        dict/list: 解析后的数据，如果解析失败则返回 None
    """
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"JSON 解析错误: {e}")
        return None
```

## 3. 数据验证

### 3.1 验证 JSON Schema
```python
def validate_json_schema(data, schema):
    """
    验证数据是否符合指定的 JSON Schema
    
    参数:
        data (dict): 要验证的数据
        schema (dict): JSON Schema 定义
        
    返回:
        bool: 验证是否通过
    """
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"JSON 验证错误: {e}")
        return False
```

## 4. 数据格式化

### 4.1 格式化 JSON 数据
```python
def format_json_data(data):
    """
    将数据格式化为美观的 JSON 字符串
    
    参数:
        data (dict/list): 要格式化的数据
        
    返回:
        str: 格式化后的 JSON 字符串
    """
    return json.dumps(data, indent=4, ensure_ascii=False, sort_keys=True)
```

## 5. 数据合并

### 5.1 合并 JSON 数据
```python
def merge_json_data(data1, data2):
    """
    合并两个 JSON 数据
    
    参数:
        data1 (dict/list): 第一个数据
        data2 (dict/list): 第二个数据
        
    返回:
        dict/list: 合并后的数据
    """
    if isinstance(data1, dict) and isinstance(data2, dict):
        return {**data1, **data2}
    elif isinstance(data1, list) and isinstance(data2, list):
        return data1 + data2
    return data2
```

## 6. 使用示例

### 6.1 配置文件操作
```python
# 读取配置文件
config = read_json_file('config.json')

# 写入配置
config_data = {
    "github_token": "your_token",
    "notification_settings": {
        "email": "example@email.com"
    }
}
write_json_file('config.json', config_data)
```

### 6.2 数据验证示例
```python
# 定义 schema
schema = {
    "type": "object",
    "properties": {
        "github_token": {"type": "string"},
        "notification_settings": {
            "type": "object",
            "properties": {
                "email": {"type": "string", "format": "email"}
            }
        }
    }
}

# 验证数据
data = {
    "github_token": "abc123",
    "notification_settings": {
        "email": "test@example.com"
    }
}
is_valid = validate_json_schema(data, schema)
```

### 6.3 数据合并示例
```python
# 合并字典
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = merge_json_data(dict1, dict2)
# 结果: {"a": 1, "b": 3, "c": 4}

# 合并列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = merge_json_data(list1, list2)
# 结果: [1, 2, 3, 4, 5, 6]
```

## 7. 最佳实践

1. **错误处理**
   - 始终使用 try-except 处理可能的异常
   - 提供有意义的错误信息
   - 设置合适的默认返回值

2. **编码处理**
   - 使用 UTF-8 编码
   - 设置 `ensure_ascii=False` 以支持非 ASCII 字符

3. **数据验证**
   - 在写入文件前验证数据格式
   - 使用 JSON Schema 确保数据完整性
   - 验证关键字段的存在性和类型

4. **性能优化**
   - 避免频繁的文件读写操作
   - 使用适当的数据结构
   - 考虑使用缓存机制

5. **安全性**
   - 不要直接解析不可信的 JSON 数据
   - 验证数据大小和深度
   - 注意敏感信息的处理

## 8. 注意事项

1. 文件操作
   - 确保有适当的文件权限
   - 处理文件路径的跨平台兼容性
   - 注意文件锁定的问题

2. 内存使用
   - 大文件考虑使用流式处理
   - 注意 JSON 数据的深度和大小
   - 避免内存泄漏

3. 并发处理
   - 考虑多线程/多进程访问
   - 使用适当的锁机制
   - 处理文件冲突

4. 错误恢复
   - 实现数据备份机制
   - 提供回滚功能
   - 记录错误日志 


让我解释一下 Python 中的 `**` 操作符：

`**` 是 Python 中的解包操作符（Unpacking Operator），在字典中使用时，它有以下作用：

1. **字典解包**：
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
# 结果: {"a": 1, "b": 3, "c": 4}
```

这里的 `**` 做了两件事：
- `**dict1` 将第一个字典的所有键值对解包
- `**dict2` 将第二个字典的所有键值对解包
- 如果键重复，后面的值会覆盖前面的值

2. **实际执行过程**：
```python
# 这行代码：
merged_dict = {**dict1, **dict2}

# 等价于：
merged_dict = {
    "a": 1,  # 来自 dict1
    "b": 2,  # 来自 dict1
    "b": 3,  # 来自 dict2，覆盖了 dict1 的 "b"
    "c": 4   # 来自 dict2
}
```

3. **其他常见用法**：
```python
# 在函数参数中使用
def print_dict(**kwargs):
    print(kwargs)

# 调用函数
print_dict(a=1, b=2)  # 输出: {'a': 1, 'b': 2}

# 合并多个字典
dict1 = {"a": 1}
dict2 = {"b": 2}
dict3 = {"c": 3}
merged = {**dict1, **dict2, **dict3}
# 结果: {"a": 1, "b": 2, "c": 3}
```

4. **与 `*` 的区别**：
- `**` 用于字典解包
- `*` 用于列表/元组解包
```python
# 列表解包
list1 = [1, 2]
list2 = [3, 4]
merged_list = [*list1, *list2]
# 结果: [1, 2, 3, 4]
```

5. **实际应用场景**：
```python
# 配置合并
default_config = {
    "host": "localhost",
    "port": 8080
}
user_config = {
    "port": 9000,
    "debug": True
}
final_config = {**default_config, **user_config}
# 结果: {"host": "localhost", "port": 9000, "debug": True}

# 函数参数传递
def process_data(**kwargs):
    # 处理数据
    pass

config = {"name": "test", "value": 123}
process_data(**config)  # 等价于 process_data(name="test", value=123)
```

6. **注意事项**：
- 解包操作会创建新的字典，不会修改原字典
- 如果键重复，后面的值会覆盖前面的值
- 解包操作符 `**` 只能用于字典
- 在 Python 3.5 及以上版本中支持

这种解包操作符的使用使代码更简洁、更易读，特别是在处理配置合并、参数传递等场景时非常有用。