# Claude Code 权限清单

本项目（`ai-resources-penn-sas`）当前授予 Claude Code 的全部权限记录。
最后核对：2026-09-08（本次会话新增第 13–14 条）

配置来源：

| 层级 | 文件 | 是否进 git |
|---|---|---|
| 项目本地 | `.claude/settings.local.json` | 否（被全局 gitignore 排除） |
| 用户全局 | `~/.claude/settings.json` | 否 |
| 项目条目 | `~/.claude.json` → `projects["/Users/yuxin/ai-resources-penn-sas"]` | 否 |
| 预览服务 | `.claude/launch.json` | 是 |

---

## 1. 项目级 allow 列表（`.claude/settings.local.json`）

共 14 条，全部是 `Bash` 规则。**没有 `deny`，没有 `ask`。**

| # | 规则 | 作用 | 状态 |
|---|---|---|---|
| 1 | `cp assets/css/students.css → scratchpad/students.css.bak` | 备份 CSS | 失效：写死了旧会话的 scratchpad 路径 |
| 2 | `sed 's/student-/guide-/g' assets/css/students.css` | 只打印替换结果，不改文件 | 有效 |
| 3 | `python3 -` | **从 stdin 执行任意 Python** | 有效 · 权限最宽的一条 |
| 4 | `sed -i '' 's/ R(713, 732),…/…/' split.py` | 原地改 `split.py` | 失效：`split.py` 已不在仓库 |
| 5 | `sed -i '' 's/…Hidden state for filtered prompts…/' split.py` | 同上 | 失效：同上 |
| 6 | `sed -i '' 's/ R(735, 738),…/…/' split.py` | 同上 | 失效：同上 |
| 7 | `python3 split.py` | 运行该脚本 | 失效：同上 |
| 8 | `cp scratchpad/guide.css → assets/css/guide.css` | 落盘新 CSS | 失效：旧 scratchpad 路径 |
| 9 | `cp scratchpad/students.new.css → assets/css/students.css` | 覆盖 CSS | 失效：旧 scratchpad 路径 |
| 10 | `sed -i '' 's/student-/guide-/g' _layouts/students.html` | **原地改 layout 文件** | 有效 |
| 11 | `cp -r _site → scratchpad/_site_before` | 备份构建产物 | 失效：旧 scratchpad 路径 |
| 12 | `bundle exec *` | **通配符**：任意 `bundle exec` 命令（`jekyll build` / `serve` 等） | 有效 |
| 13 | `bundle exec jekyll serve:*` | 显式允许本地预览，不再逐次询问 | 有效（已被第 12 条覆盖，留作备档） |
| 14 | `bundle exec jekyll build:*` | 同上，构建 | 有效（同上） |

**实际仍生效的只有第 2、3、10、12、13、14 条。**

失效原因：第 1、8、9、11 条把某次会话的 scratchpad ID（`340192ac-…`）写进了规则，scratchpad 路径每个会话都会变；第 4–7 条指向的 `split.py` 是当时的临时脚本，已不在仓库。这些是死规则，可以随时删掉。

两条值得留意的宽规则：

- `python3 -` — 等于允许执行任意 Python，能读写本项目内任何文件、发网络请求。
- `bundle exec *` — 通配符匹配所有子命令。

## 2. 用户全局设置（`~/.claude/settings.json`）

**不包含任何 permissions 配置**，只有偏好项：

- `model: opus[1m]`
- `effortLevel: xhigh`
- `tui: fullscreen`
- `attribution.commit` / `attribution.pr` 置空 → commit 与 PR 描述不加署名行

## 3. 未配置的项

- 无 `deny` 列表（没有明令禁止的命令）
- 无 `ask` 列表
- 无 hooks
- 无 `additionalDirectories` → 工作范围限于 `/Users/yuxin/ai-resources-penn-sas` 与当次会话的 scratchpad
- `~/.claude.json` 中本项目 `allowedTools: []`、`hasTrustDialogAccepted: true`

## 4. 会话级行为

- **auto 模式**：优先用 Bash（`cat` / `grep` / `sed` / heredoc）代替 Read / Edit / Write 工具做读写。
- 只读命令直接执行不弹窗；写操作、网络请求、白名单外的命令仍会逐次征求确认。
- **Git：只在明确要求时才 commit / push。**

## 5. 可调用的工具（含项目外影响面）

除本地文件与 Bash 外，本会话还挂载了这些能影响项目之外的工具：

- **Google Drive 连接器** — 读、搜索、创建、更新、复制、分享、移入垃圾桶
- **blog-generator MCP** — 解析转录稿、存草稿、发布到博客
- **Artifact 发布** — 发布页面到 claude.ai（默认私有）
- **浏览器** — 应用内浏览器，以及真实 Chrome（携带已登录会话）
- **iOS 模拟器**、**定时任务 / cron**、**读取终端面板**

其中凡是对外发布、发送消息、更改账号设置、删除数据的动作，都会先确认再执行。

## 6. 维护建议

- 清理第 1、4–9、11 条死规则，`allow` 列表会短很多。
- 若想收紧，把 `python3 -` 换成具体脚本路径，把 `bundle exec *` 收窄为 `bundle exec jekyll build` / `bundle exec jekyll serve`。
- 加规则时**不要**把 scratchpad 绝对路径写进去 —— 每次会话都会变，写进去即成死规则。
- 需要禁止某类命令时，在 `.claude/settings.local.json` 里加 `deny` 列表，它优先于 `allow`。
