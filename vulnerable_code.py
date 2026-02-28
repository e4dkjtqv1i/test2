import os
import subprocess
import pickle

# 漏洞 1: 命令注入
def run_unsafe_command(user_input):
    # 危险：直接将用户输入拼接到命令行中
    command = f"ls -l {user_input}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8')

# 漏洞 2: SQL 注入
def get_user_data(username):
    # 危险：直接拼接 SQL 查询字符串
    query = f"SELECT * FROM users WHERE username = '{username}'"
    # 假设这里执行查询
    return query

# 漏洞 3: 不安全的反序列化
def load_data(data_string):
    # 危险：反序列化不受信任的数据可能导致任意代码执行
    return pickle.loads(data_string)

# 漏洞 4: 硬编码敏感信息
API_KEY = "sk-1234567890abcdef"
DB_PASSWORD = "admin123"

# 漏洞 5: 使用弱加密算法
def encrypt_data(data):
    from Crypto.Cipher import DES
    # 危险：DES 是不安全的加密算法
    key = b'8bytekey' 
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

# 漏洞 6: 随机数生成不安全
def generate_token():
    import random
    # 危险：使用伪随机数生成器生成安全令牌
    return ''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(32)])

if __name__ == "__main__":
    # 测试漏洞代码
    user_input = input("Enter directory: ")
    print(run_unsafe_command(user_input))
    
    username = input("Enter username: ")
    print(get_user_data(username))


