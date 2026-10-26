# AGENTS.md

## What this repo is

Minimal tutorial/demo repo for building a CrewAI multi-agent setup. The entire
application is `example/crew_ai.py`; `dataset/data.txt` is just sample travel
notes text.

## Commands

- Setup: `pip install -r requirements.txt` (installs `crewai==1.15.30` and
  `python-dotenv==1.2.4`). A `.venv/` (conda) already exists in the repo.
- Run the agent: `python example/crew_ai.py` from the repo root.

There is no test suite, linter, typechecker, CI, build step, or codegen. No
verification commands beyond running the script.

## Key facts / gotchas

- The LLM is configured via OpenRouter: model `openrouter/qwen/qwen3.8-27b`,
  base URL `https://openrouter.ai/api/v1`, API key from the
  `OPENROUTER_API_KEY` environment variable.
- `example/crew_ai.py` calls `load_dotenv()` and reads
  `os.environ["OPENROUTER_API_KEY"]`, so the key must be present in `.env` at
  the repo root (loaded from the current working directory — run the script from
  the repo root, not from `example/`).
- `.env` is gitignored; never commit real keys.

## Conventions

- Agent changes happen in `example/crew_ai.py` (CrewAI `Agent`/`Task`/`Crew`
  API, v1.x style). Keep the entrypoint minimal; tweak the task description /
  question to change behavior.

## Sources of truth

- Executable source: `example/crew_ai.py`; dependency list: `requirements.txt`.

## กติกาโปรเจกต์ (Spec-Driven Development)

- งานใหม่ทุกชิ้นเริ่มจาก specs/<ชื่อฟีเจอร์>/spec.md
- ห้ามเขียนโค้ดจนกว่าจะมี spec.md, plan.md, tasks.md ที่ผู้ใช้อนุมัติแล้ว
- ทำ tasks.md ทีละข้อ เขียนเทสต์ก่อน ติ๊ก [x] เมื่อเทสต์ผ่าน
- ถ้าพบว่า spec ผิดหรือไม่ครบ ให้หยุดและบอกผู้ใช้ ห้ามเดาเอง
