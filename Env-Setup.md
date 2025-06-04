# 项目环境配置

## 安装项目依赖包

1. 基础环境：Python3.12+

2. 安装UV
```shell
pip install uv
set UV_INDEX=https://mirrors.aliyun.com/pypi/simple
```

3. 安装Python依赖包
```shell
uv sync --python 3.12 --all-extras
```

4. 切换到本地环境(.venv)，请安装whl包
```shell
cd .venv/Scripts
activate
```

## 启动Jupyter编辑器

```shell
jupyter notebook
```

## 模型加载

1. 在项目根目录下新建`.env`文件，并添加以下内容
```text
API_KEY=your_api_key
BASE_URL=model_base_url
```

2. 加载模型  
如果需要调用模型，请直接在notebook中添加以下代码（注意需要加载项目根目录到环境的path中），不需要额外的配置。
```python
import os
import sys

# 加载项目根目录到环境的path中
sys.path.append(os.getcwd().split('content')[0][:-1])

# 读取.env配置文件，加载配置的模型
import utils.load_model
from utils.load_model import get_completion
```