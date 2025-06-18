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