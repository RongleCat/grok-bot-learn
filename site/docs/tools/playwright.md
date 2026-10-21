---
title: Playwright
sidebar: false
prev: false
next: false
---

# Playwright

<ToolMeta id="playwright" />

`playwright` 是微软开源的浏览器自动化工具库。**适合编写脚本批量截屏、爬取需 JavaScript 渲染的网页以及进行页面回归检查以节省额度。**

## 前置条件

- **系统需安装 Python 3 或 Node.js 环境。**
- 可单独安装 `chromium` 核心以节省磁盘空间。

## 安装

```bash
python3 -m venv ~/.venvs/pw
~/.venvs/pw/bin/pip install playwright
~/.venvs/pw/bin/python -m playwright install --with-deps chromium
```

## 登录与授权

**不需要登录。**

## 验证

```bash
~/.venvs/pw/bin/python -m playwright --version
```

## 常见坑与解决

### Debian 安装报 `externally-managed-environment`

**先创建 Python venv 虚拟环境再执行 pip 安装。** 系统自带 Python 受 PEP 668 保护禁止全局安装。

### 无 root 权限时依赖安装报错

**执行安装命令时去掉 `--with-deps` 参数。** 包含该参数会强制调用 sudo 安装系统依赖。

## 来源

- [Playwright Python 官方文档](https://playwright.dev/python/docs/intro)

> 本页为社区非官方整理，与该工具厂商、xAI 均无隶属关系，命令以官方文档为准。

[← 返回目录](/tools/)
