import requests
from PIL import Image
from io import BytesIO
from openai import OpenAI

# DALL-E 3图片生成函数
def generate_image_url(prompt):
    client = OpenAI()
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url

# 下载图片并保存到本地的函数
def download_and_save_image(image_url, filename):
    response = requests.get(image_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        image.save(filename)
        return filename
    else:
        print("无法下载图片")
        return None

# 展示图片的函数
def display_image(filename):
    image = Image.open(filename)
    image.show()

# 主程序
def create_and_show(prompt):
    url = generate_image_url(prompt)
    print(f"get url successfully")

    # 指定保存的文件名
    filename = "dalle.jpg"
    saved_file = download_and_save_image(url, filename)

    # 如果图片保存成功，则展示它
    if saved_file:
        display_image(saved_file)

    return "created successfully, saved as " + filename