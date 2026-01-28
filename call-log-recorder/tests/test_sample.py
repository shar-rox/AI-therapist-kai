from call_log_recorder import parser

def test_parse_simple_record():
    sample = "2026-01-01,Caller,Receiver,00:05:30"
    rec = parser.parse_line(sample)
    assert rec["duration_seconds"] == 330
