# Real-time AI Clipboard Translator for Gamers
## 为游戏玩家打造的实时AI剪贴板翻译器

A simple yet powerful Python script that provides a seamless, real-time translation workflow, perfect for gamers playing on international servers.

一个简洁而强大的Python脚本，为常玩外服的游戏玩家提供无缝的实时翻译工作流。

---

### 💡 The Problem / 项目初衷

Communicating in foreign game servers can be slow and cumbersome. Constantly switching between the game and a translation app breaks immersion and is too slow for fast-paced interactions. This tool was built to solve that exact problem.

在外服游戏中与外国玩家交流可能是一件非常痛苦的事情。在游戏和翻译软件之间不断切屏，不仅会打断沉浸感，而且对于快节奏的对战来说实在太慢了。这个工具正是为了解决这个痛点而生。

### ✨ Features / 主要功能

- **Clipboard Monitoring / 剪贴板监控**: Automatically detects when you copy (`Ctrl+C`) or cut (`Ctrl+X`) Chinese text. / 自动检测你复制或剪切的中文文本。
- **AI-Powered Translation / AI驱动的高质量翻译**: Uses the powerful GPT-4o model via the OpenAI API for accurate and natural translations. / 使用强大的GPT-4o模型进行高质量、高精度的翻译。
- **Automatic Pasting / 自动化粘贴**: Simulates a `Ctrl+V` command to instantly paste the translated English text back into your game's chat box or any other input field. / 模拟按下`Ctrl+V`，将翻译好的英文瞬间粘贴回游戏聊天框或任何输入框。
- **Real-time & Seamless / 实时无缝的工作流**: The entire process from copying Chinese to pasting English is fully automated, creating a near-instant communication experience. / 从复制中文到粘贴英文的全过程完全自动化，创造近乎即时的交流体验。

### 🛠️ How to Use / 如何使用

1.  **Clone the repository: / 克隆代码仓库：**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```
    *(Please replace `your-username` and `your-repository-name` with your actual GitHub info. / 请将 `your-username` 和 `your-repository-name` 替换成您的实际信息。)*

2.  **Set up a Python environment: / 创建独立的Python环境：**
    (It is highly recommended to use a virtual environment. / 强烈建议使用虚拟环境。)
    ```bash
    python -m venv venv
    ```
    - On Windows / 在Windows上:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux / 在macOS或Linux上:
      ```bash
      source venv/bin/activate
      ```

3.  **Install dependencies: / 安装依赖库：**
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt` file, you can install them manually: `pip install openai pyperclip pynput` / 如果您没有 `requirements.txt` 文件，可以手动安装：`pip install openai pyperclip pynput`)*

4.  **Add your API Key: / 添加你的API密钥：**
    Open the `translator.py` script and replace the placeholder text with your actual OpenAI API key.
    
    打开 `translator.py` 文件，将代码中的占位符替换成你真实的OpenAI API密钥。
    ```python
    OPENAI_API_KEY = "Your-OpenAI-API-key-goes-here"
    ```

5.  **Run the script: / 运行脚本：**
    ```bash
    python translator.py
    ```
    Now, the script is running in the background. Whenever you copy a piece of Chinese text, it will be automatically translated and pasted!
    
    现在，脚本已经在后台运行。每当您复制一段中文，它就会被自动翻译并粘贴！

### ⚙️ Configuration / 配置

All configuration is done directly within the `translator.py` script.
所有配置都在 `translator.py` 脚本内部直接完成。

- **`OPENAI_API_KEY`**: You must provide your own OpenAI API key. / 你必须提供自己的OpenAI API密钥。
- **`model`**: The script uses `gpt-4o` by default for its speed and quality. You can change it to other models like `gpt-3.5-turbo` if you prefer. / 脚本默认使用`gpt-4o`模型，你也可以根据喜好更换为`gpt-3.5-turbo`等其他模型。

### 📦 Dependencies / 依赖库

This project relies on the following Python libraries:
本项目依赖以下Python库：

- `openai`
- `pyperclip`
- `pynput`

You can create the `requirements.txt` file yourself by running `pip freeze > requirements.txt` in your activated virtual environment.
你可以在激活的虚拟环境中运行 `pip freeze > requirements.txt` 来自己生成 `requirements.txt` 文件。

### ❤️ Contributing / 贡献代码

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
欢迎各种贡献、问题和功能请求！

---

_This project was born out of a gamer's need and brought to life with the power of AI._
_这个项目诞生于一个游戏玩家的真实需求，并由AI的力量赋予其生命。_
