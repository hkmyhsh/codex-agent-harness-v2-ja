#!/usr/bin/env python3
import json
from pathlib import Path

STATE = Path('.agent/state.json')
SCHEMA = Path('.agent/state.schema.json')

required = [
    'schema_version','task_id','title','status','current_agent','next_agent',
    'current_step','next_action','retry_count','max_retry_count',
    'blockers','completed_steps','pending_steps','updated_at'
]

allowed_status = {'not_started','planning','designing','executing','testing','review_required','documenting','blocked','done','failed'}
allowed_agents = {'Planner','Architect','Executor','Tester','Reviewer','Documenter'}

def main():
    if not STATE.exists():
        raise SystemExit('missing .agent/state.json')
    data = json.loads(STATE.read_text(encoding='utf-8'))
    missing = [k for k in required if k not in data]
    if missing:
        raise SystemExit(f'missing required keys: {missing}')
    if data['status'] not in allowed_status:
        raise SystemExit(f'invalid status: {data["status"]}')
    if data['current_agent'] not in allowed_agents:
        raise SystemExit(f'invalid current_agent: {data["current_agent"]}')
    if data['next_agent'] not in allowed_agents:
        raise SystemExit(f'invalid next_agent: {data["next_agent"]}')
    if data['retry_count'] > data['max_retry_count']:
        raise SystemExit('retry_count exceeds max_retry_count')
    print('state.json validation passed')

if __name__ == '__main__':
    main()
