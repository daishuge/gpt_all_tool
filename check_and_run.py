import re
from tool import dalle, sandbox, web

def get_code(md_content):
    # 正则表达式来匹配 Markdown 中的代码块，包括没有指定语言的情况
    pattern = r"```(\w+)?([\s\S]+?)```"
    
    # 寻找所有匹配的代码块
    matches = re.findall(pattern, md_content)
    
    if matches:
        # 从匹配中提取语言和代码
        for match in matches:
            language, code = match
            return language if language else None, code.strip()
    else:
        return None, None
    
def main(reply):
    language, code = get_code(reply)

    if code==None or language==None:
        return None
    
    # elif language == "python_sand_box":
    #     result = sandbox.run_code(code)
    
    elif language == "dalle":
        result = dalle.create_and_show(code)
    
    # elif language == "get_url_content" or language == "google_search":
    #     result = web.main(code, language)
    
    return result