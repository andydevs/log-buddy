import pytest
import log_buddy


@pytest.fixture
def my_function_data():
    def my_function(log: log_buddy.Logger, a: int, b: int, z: int = 4) -> int:
        """
        My custom function with it's own docstring
        """
        log.info("Internal log... got a = %s, b = %s, and z = %s", a, b, z)
        return (a - b) * z

    return my_function, "my_function"


def test_log_function_default_args_debug_log_function_args(my_function_data, caplog):
    """
    Test log function with default args and just using args in function
    """
    caplog.set_level(log_buddy.DEBUG)
    log = log_buddy.getLogger("test")
    my_function, my_function_name = my_function_data
    my_function = log_buddy.log_function(log)(my_function)
    result = my_function(2, 3, 1)
    assert all(r.name == f"test.{my_function_name}" for r in caplog.records)
    assert "Called with args (2, 3, 1) and kwargs {}" in caplog.messages
    assert f"Returned {result}" in caplog.messages
    assert "Internal log... got a = 2, b = 3, and z = 1" in caplog.messages


def test_log_function_default_args_debug_log_function_args_and_kwargs(my_function_data, caplog):
    """
    Test log function with default args and just using args in function
    """
    caplog.set_level(log_buddy.DEBUG)
    log = log_buddy.getLogger("test")
    my_function, my_function_name = my_function_data
    my_function = log_buddy.log_function(log)(my_function)
    result = my_function(2, b=1, z=8)
    assert all(r.name == f"test.{my_function_name}" for r in caplog.records)
    assert "Called with args (2,) and kwargs {'b': 1, 'z': 8}" in caplog.messages
    assert f"Returned {result}" in caplog.messages
    assert "Internal log... got a = 2, b = 1, and z = 8" in caplog.messages


def test_log_function_default_args_info_log_function_args(my_function_data, caplog):
    """
    Test log function with default args and just using args in function
    """
    caplog.set_level(log_buddy.INFO)
    log = log_buddy.getLogger("test")
    my_function, my_function_name = my_function_data
    my_function = log_buddy.log_function(log)(my_function)
    result = my_function(2, 3, 1)
    assert all(r.name == f"test.{my_function_name}" for r in caplog.records)
    assert "Called with args (2, 3, 1) and kwargs {}" not in caplog.messages
    assert f"Returned {result}" not in caplog.messages
    assert "Internal log... got a = 2, b = 3, and z = 1" in caplog.messages


def test_log_function_default_args_info_log_function_args_and_kwargs(my_function_data, caplog):
    """
    Test log function with default args and just using args in function
    """
    caplog.set_level(log_buddy.INFO)
    log = log_buddy.getLogger("test")
    my_function, my_function_name = my_function_data
    my_function = log_buddy.log_function(log)(my_function)
    result = my_function(2, b=1, z=8)
    assert all(r.name == f"test.{my_function_name}" for r in caplog.records)
    assert "Called with args (2,) and kwargs {'b': 1, 'z': 8}" not in caplog.messages
    assert f"Returned {result}" not in caplog.messages
    assert "Internal log... got a = 2, b = 1, and z = 8" in caplog.messages
