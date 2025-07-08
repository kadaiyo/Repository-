# 导入我们需要的工具
# Import the necessary tools
import pyperclip  # 用于读写剪贴板 / For reading and writing to the clipboard
import time  # 用于设置程序检查的间隔时间 / For setting the program's check interval
from openai import OpenAI  # 导入OpenAI官方库 / Import the official OpenAI library
from pynput.keyboard import Key, \
    Controller  # 导入键盘控制器，用于模拟按键 / Import the keyboard controller for simulating key presses


# --- 工具函数：判断一段文本是否包含中文字符 ---
# --- Utility Function: Check if a piece of text contains Chinese characters ---
def contains_chinese(text):
    # 如果文本为空，直接返回False
    # If the text is empty, return False immediately
    if not text:
        return False
    # 遍历文本中的每一个字符
    # Iterate through each character in the text
    for char in text:
        # 通过检查字符的Unicode编码范围来判断是否为中文
        # Check if the character is Chinese by its Unicode range
        if '\u4e00' <= char <= '\u9fff':
            # 只要找到一个中文字符，就立即返回True
            # As soon as one Chinese character is found, return True
            return True
    # 如果遍历完所有字符都没有找到中文，返回False
    # If no Chinese characters are found after checking all characters, return False
    return False


# --- AI翻译函数：调用GPT模型并使用流式传输 ---
# --- AI Translation Function: Call the GPT model using streaming ---
def translate_with_gpt_stream(text, api_key):
    try:
        # 创建一个OpenAI的客户端实例，并传入API密钥
        # Create an OpenAI client instance, passing in the API key
        client = OpenAI(api_key=api_key)

        # 发送请求给AI，并开启流式传输 (stream=True)
        # Send a request to the AI and enable streaming (stream=True)
        response_stream = client.chat.completions.create(
            # 指定使用的模型为 gpt-4o，它速度快、效果好
            # Specify the model as gpt-4o, which is fast and effective
            model="gpt-4o",
            # 'messages'是与AI对话的内容列表
            # 'messages' is the list of content for the conversation with the AI
            messages=[
                {
                    # 'system'角色的内容是给AI的指令，告诉它扮演什么角色
                    # The content for the 'system' role is the instruction for the AI, telling it what role to play
                    "role": "system",
                    "content": "You are a professional translation engine. Your task is to translate the user's Chinese text into English. Do not add any extra content, explanations, or comments. Just return the translated English text."
                },
                {
                    # 'user'角色的内容是用户实际输入的文本
                    # The content for the 'user' role is the text actually input by the user
                    "role": "user",
                    "content": text
                }
            ],
            stream=True  # 开启流式传输！ / Enable streaming!
        )

        # 在终端打印提示，end=""表示不换行，flush=True确保立即显示
        # Print a prompt in the terminal, end="" means no newline, flush=True ensures immediate display
        print("AI译文 (流式输出): ", end="", flush=True)

        # 创建一个空字符串，用来拼接AI返回的完整结果
        # Create an empty string to assemble the complete result returned by the AI
        full_response = ""
        # 遍历AI返回的数据流（一个一个的数据块）
        # Iterate through the data stream returned by the AI (chunk by chunk)
        for chunk in response_stream:
            # 获取每个数据块中的文本内容，如果没有内容则为空字符串
            # Get the text content from each chunk; if there's no content, it's an empty string
            content = chunk.choices[0].delta.content or ""
            # 实时地将内容打印到终端
            # Print the content to the terminal in real-time
            print(content, end="", flush=True)
            # 将内容拼接到完整结果中
            # Append the content to the full response
            full_response += content

        # 所有数据流接收完毕后，打印一个换行符，让终端格式更好看
        # After all data streams are received, print a newline for better terminal formatting
        print()

        # 返回拼接好的、并去除了首尾空格的完整翻译文本
        # Return the assembled and stripped full translation text
        return full_response.strip()

    except Exception as e:
        # 如果在翻译过程中发生任何错误，打印错误信息
        # If any error occurs during the translation process, print the error message
        print(f"\n!! GPT翻译时发生错误: {e}")
        # 并返回None，表示翻译失败
        # And return None to indicate that the translation failed
        return None


# --- 主程序开始 ---
# --- Main Program Starts ---

# 在这里粘贴你从 OpenAI 平台获取的API密钥 (以 sk- 开头)
# Paste your API key obtained from the OpenAI platform here (starts with sk-)
OPENAI_API_KEY = "此处粘贴OpenAI API key"

# 检查API密钥是否已填写
# Check if the API key has been filled in
if OPENAI_API_KEY == "在这里粘贴你刚刚获取的OpenAI API密钥":
    print("！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
    print("！！！ 错误：请在代码中填写你的OpenAI API密钥 ！！！")
    print("！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
else:
    # 创建一个键盘控制器实例，后面用它来模拟按键
    # Create a keyboard controller instance to simulate key presses later
    keyboard = Controller()

    print("--- AI实时翻译粘贴程序启动 (终极版 - Powered by GPT-4o) ---")
    print("--- 现在，去剪切或复制任何中文，体验无缝翻译粘贴！ ---")

    # 创建一个变量，用来存储上一次剪贴板的内容，以防止重复翻译
    # Create a variable to store the last clipboard content to prevent duplicate translations
    last_copied_text = ""

    # 开始一个无限循环，让程序持续在后台运行
    # Start an infinite loop to keep the program running in the background
    while True:
        try:
            # 读取当前剪贴板的文本
            # Read the current text from the clipboard
            current_text = pyperclip.paste()

            # 检查剪贴板内容是否是新的、非空的，并且包含中文
            # Check if the clipboard content is new, not empty, and contains Chinese
            if current_text and current_text != last_copied_text and contains_chinese(current_text):

                print(f"\n检测到新的中文内容: 【{current_text}】")
                # 更新“上一次的内容”，防止下一次循环时重复处理
                # Update the "last content" to prevent reprocessing in the next loop
                last_copied_text = current_text

                # 调用我们新的GPT翻译函数
                # Call our new GPT translation function
                translated_text = translate_with_gpt_stream(current_text, OPENAI_API_KEY)

                # 如果翻译成功 (即返回的不是None)
                # If the translation is successful (i.e., the return is not None)
                if translated_text:
                    # 将翻译好的完整结果复制回剪贴板
                    # Copy the complete translated result back to the clipboard
                    pyperclip.copy(translated_text)
                    print("翻译完成! 完整译文已复制到剪贴板。")

                    # 模拟按下 Ctrl+V 进行自动粘贴
                    # Simulate pressing Ctrl+V for automatic pasting
                    print("执行自动粘贴...")
                    keyboard.press(Key.ctrl)
                    keyboard.press('v')
                    keyboard.release('v')
                    keyboard.release(Key.ctrl)
                    print("粘贴完成！")

            # 让程序暂停1秒，以降低CPU占用率
            # Pause the program for 1 second to reduce CPU usage
            time.sleep(1)

        except Exception as e:
            # 如果主循环中发生任何未预料的错误，打印它
            # If any unexpected error occurs in the main loop, print it
            print(f"\n!! 主循环发生错误: {e}")
            # 并等待5秒后继续尝试，以增加程序的稳定性
            # And wait for 5 seconds before trying again to increase program stability 
            print("程序将在5秒后继续...")
            time.sleep(5)
