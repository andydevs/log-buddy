import log_buddy


def test_modlog(caplog):
    log = log_buddy.modlog()
    log.info("Testing log")
    assert all(r.name == __name__ for r in caplog.records)
