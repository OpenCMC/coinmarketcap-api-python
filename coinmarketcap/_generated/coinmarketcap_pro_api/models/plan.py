from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Plan")


@_attrs_define
class Plan:
    """Object containing rate limit and daily/monthly credit limit details for your API Key.

    Attributes:
        credit_limit_monthly (float): The number of API credits that can be used each monthly period before receiving a
            HTTP 429 rate limit error. This limit is based on the API plan tier. Example: 120000.
        credit_limit_monthly_reset (str): A human readable countdown of when the API key monthly credit limit will reset
            back to 0. Example: In 3 days, 19 hours, 56 minutes.
        credit_limit_monthly_reset_timestamp (str): Timestamp (ISO 8601) of when the monthly credit limit will reset.
            This is based on your billing plan activation date for premium subscription based keys or calendar month UTC
            midnight for free Basic plan keys. Example: 2019-09-01T00:00:00.000Z.
        rate_limit_minute (float): The number of API calls that can be made within the same UTC minute before receiving
            a HTTP 429 rate limit error. This limit is based on the API plan tier. Example: 60.
    """

    credit_limit_monthly: float
    credit_limit_monthly_reset: str
    credit_limit_monthly_reset_timestamp: str
    rate_limit_minute: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        credit_limit_monthly = self.credit_limit_monthly

        credit_limit_monthly_reset = self.credit_limit_monthly_reset

        credit_limit_monthly_reset_timestamp = self.credit_limit_monthly_reset_timestamp

        rate_limit_minute = self.rate_limit_minute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credit_limit_monthly": credit_limit_monthly,
                "credit_limit_monthly_reset": credit_limit_monthly_reset,
                "credit_limit_monthly_reset_timestamp": credit_limit_monthly_reset_timestamp,
                "rate_limit_minute": rate_limit_minute,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credit_limit_monthly = d.pop("credit_limit_monthly")

        credit_limit_monthly_reset = d.pop("credit_limit_monthly_reset")

        credit_limit_monthly_reset_timestamp = d.pop("credit_limit_monthly_reset_timestamp")

        rate_limit_minute = d.pop("rate_limit_minute")

        plan = cls(
            credit_limit_monthly=credit_limit_monthly,
            credit_limit_monthly_reset=credit_limit_monthly_reset,
            credit_limit_monthly_reset_timestamp=credit_limit_monthly_reset_timestamp,
            rate_limit_minute=rate_limit_minute,
        )

        plan.additional_properties = d
        return plan

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
