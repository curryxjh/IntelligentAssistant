# IntelligentAssistant

IntelligentAssistant 是一个用于学习和重写企业智能客服系统的 Python 项目。当前版本先保留最小可运行后端骨架，后续会逐步补齐意图识别、多 Agent 编排、记忆系统、RAG 知识库、监控评测和前端调试台。

项目参考 EchoMind 的整体思路，但这里会按学习节奏从小到大实现，避免一开始就把所有模块堆满。

## 当前状态

当前已经完成：

- FastAPI 应用入口
- 应用生命周期 `lifespan`
- 启动 Banner
- CORS 中间件
- `/health` 健康检查接口
- `pyproject.toml + uv.lock` 依赖管理
- 前端目录 `Frontend/` 保留为后续联调使用

当前暂未实现：

- `/chat` 对话接口
- 意图识别
- Agent 路由
- Redis 记忆
- Milvus / ChromaDB 向量知识库
- RAG 检索
- Prometheus 监控
- 端到端评测

这些未实现部分会后续逐步加回来。

## 技术栈

后端：

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- uv

后续计划引入：

- Redis：短期会话记忆
- Milvus：知识库向量检索和长期记忆
- LLM API：意图识别、回复生成、总结和重排
- Prometheus：运行指标监控

前端：

- Vue 3
- Vite

## 目录结构

```text
IntelligentAssistant/
├── cmd/
│   ├── main.py              # FastAPI 应用入口
│   ├── lifespan.py          # 启动和关闭生命周期
│   ├── deps.py              # 全局依赖占位
│   ├── schemas.py           # Pydantic 模型，后续逐步补充
│   └── routes/
│       ├── __init__.py
│       └── health.py        # GET /health
├── agents/                  # Agent 编排，待实现
├── core/                    # 意图识别、LLM 工具，待实现
├── memory/                  # 记忆系统，待实现
├── mcp/                     # 工具调用/RAG，待实现
├── monitor/                 # 监控，待实现
├── evaluation/              # 评测，待实现
├── Frontend/                # Vue 前端，后续联调
├── pyproject.toml
├── uv.lock
└── README.md
```

## 环境准备

推荐使用 uv 管理 Python 版本和虚拟环境。

```bash
cd {WORK_SPACE}/IntelligentAssistant

uv python install 3.11
uv venv .venv --python 3.11
source .venv/bin/activate
uv sync
```

如果已经存在 `.venv`，可以直接激活：

```bash
source .venv/bin/activate
```

## 启动后端

方式一：使用 uv 运行。

```bash
uv run uvicorn cmd.main:app --reload
```

方式二：使用当前虚拟环境运行。

```bash
.venv/bin/uvicorn cmd.main:app --reload
```

默认访问地址：

```text
http://localhost:8000
```

Swagger 文档：

```text
http://localhost:8000/docs
```

健康检查：

```bash
curl http://localhost:8000/health
```

返回示例：

```json
{
  "status": "ok",
  "service": "IntelligentAssistant"
}
```

## 启动前端

前端目前保留为后续联调用。

```bash
cd {WORK_SPACE}/IntelligentAssistant/Frontend
npm install
npm run dev
```

默认访问：

```text
http://localhost:5173
```

## 学习实现路线

建议按下面顺序逐步实现：

1. 完善 `cmd/schemas.py`
   添加 `ChatRequest` 和 `ChatResponse`。

2. 新增 `cmd/routes/chat.py`
   先实现一个最简单的 `/chat`，返回 echo 回复。

3. 实现 `core/intent_recognizer.py`
   先用关键词识别 `general`、`technical`、`billing`，后续再接 LLM。

4. 实现 `agents/agent_orchestrator.py`
   根据意图路由到不同 Agent。

5. 实现 `memory/`
   先用内存字典保存最近对话，再替换为 Redis。

6. 实现 `mcp/` 或 `rag/`
   用 Milvus 做知识库文档导入和向量检索。

7. 把 RAG 接入 `/chat`
   业务类问题先检索知识库，再生成回复。

8. 增加 `monitor/` 和 `evaluation/`
   记录延迟、成功率，并做简单测试用例。

## 开发约定

- `.venv/` 不提交到 Git。
- `pyproject.toml` 和 `uv.lock` 需要提交。
- 未实现模块不要提前接入启动链路，避免项目一启动就因为缺依赖或缺类失败。
- 每加一个模块，先保证 `/health` 和 Swagger 仍然可用。

## 当前可用接口

| 方法 | 路径 | 说明 |
|------|------|------|
| `GET` | `/health` | 健康检查 |

后续接口会逐步增加。
