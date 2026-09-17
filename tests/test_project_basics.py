from src.project_name.exception import CustomException


def test_custom_exception_message():
    try:
        raise ValueError("sample failure")
    except ValueError as exc:
        error = CustomException(exc, __import__("sys"))
        assert "sample failure" in str(error)
