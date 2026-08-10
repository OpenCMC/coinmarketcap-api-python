from typing import Literal, cast

Status4ErrorCode = Literal[500]

STATUS_4_ERROR_CODE_VALUES: set[Status4ErrorCode] = {
    500,
}


def check_status_4_error_code(value: int) -> Status4ErrorCode:
    if value in STATUS_4_ERROR_CODE_VALUES:
        return cast(Status4ErrorCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STATUS_4_ERROR_CODE_VALUES!r}")
