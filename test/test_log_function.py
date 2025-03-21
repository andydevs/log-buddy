import pytest
import log_buddy


def test_log_function_debug_log_default_args_function_args(caplog: pytest.LogCaptureFixture):
    """
    Test log function with default args and just using args
    in function
    """
    caplog.set_level(log_buddy.DEBUG)
    log = log_buddy.getLogger("test")

    @log_buddy.log_function(log)
    def my_function(log: log_buddy.Logger, a: int, b: int, z: int = 4) -> int:
        """
        My custom function with it's own docstring
        """
        log.info("Internal log... got a = %s, b = %s, and z = %s", a, b, z)
        return (a - b) * z

    result = my_function(2, 3, 1)

    assert all(r.name == "test.my_function" for r in caplog.records)
    assert "Called with args (2, 3, 1) and kwargs {}" in caplog.messages
    assert f"Returned {result}" in caplog.messages
    assert "Internal log... got a = 2, b = 3, and z = 1" in caplog.messages
