import os
import subprocess

def run_code(code):
    # 确保sandbox目录存在
    os.makedirs('sandbox', exist_ok=True)
    
    # 脚本的路径
    script_path = 'sandbox/run.py'
    
    # 写入代码到文件
    with open(script_path, 'w') as file:
        file.write(code)
    
    # 运行脚本并捕获输出
    result = subprocess.run(['python', script_path], capture_output=True, text=True)

    # 返回程序输出
    return "run result: "+result.stdout.strip()