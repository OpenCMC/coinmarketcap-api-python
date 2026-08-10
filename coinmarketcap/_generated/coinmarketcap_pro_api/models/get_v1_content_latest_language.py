from typing import Literal, cast

GetV1ContentLatestLanguage = Literal[
    "ar",
    "de",
    "en",
    "es",
    "fil-rph",
    "fr",
    "hi",
    "id",
    "it",
    "ja",
    "ko",
    "nl",
    "pl",
    "pt-br",
    "ru",
    "th",
    "tr",
    "uk",
    "vi",
    "zh",
    "zh-tw",
]

GET_V1_CONTENT_LATEST_LANGUAGE_VALUES: set[GetV1ContentLatestLanguage] = {
    "ar",
    "de",
    "en",
    "es",
    "fil-rph",
    "fr",
    "hi",
    "id",
    "it",
    "ja",
    "ko",
    "nl",
    "pl",
    "pt-br",
    "ru",
    "th",
    "tr",
    "uk",
    "vi",
    "zh",
    "zh-tw",
}


def check_get_v1_content_latest_language(value: str) -> GetV1ContentLatestLanguage:
    if value in GET_V1_CONTENT_LATEST_LANGUAGE_VALUES:
        return cast(GetV1ContentLatestLanguage, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_V1_CONTENT_LATEST_LANGUAGE_VALUES!r}")
