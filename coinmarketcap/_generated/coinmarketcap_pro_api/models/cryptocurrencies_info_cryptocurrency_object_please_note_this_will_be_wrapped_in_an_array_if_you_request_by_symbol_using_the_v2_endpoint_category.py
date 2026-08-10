from typing import Literal, cast

CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2EndpointCategory = Literal[
    "coin", "token"
]

CRYPTOCURRENCIES_INFO_CRYPTOCURRENCY_OBJECT_PLEASE_NOTE_THIS_WILL_BE_WRAPPED_IN_AN_ARRAY_IF_YOU_REQUEST_BY_SYMBOL_USING_THE_V2_ENDPOINT_CATEGORY_VALUES: set[
    CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2EndpointCategory
] = {
    "coin",
    "token",
}


def check_cryptocurrencies_info_cryptocurrency_object_please_note_this_will_be_wrapped_in_an_array_if_you_request_by_symbol_using_the_v2_endpoint_category(
    value: str,
) -> CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2EndpointCategory:
    if (
        value
        in CRYPTOCURRENCIES_INFO_CRYPTOCURRENCY_OBJECT_PLEASE_NOTE_THIS_WILL_BE_WRAPPED_IN_AN_ARRAY_IF_YOU_REQUEST_BY_SYMBOL_USING_THE_V2_ENDPOINT_CATEGORY_VALUES
    ):
        return cast(
            CryptocurrenciesInfoCryptocurrencyObjectPleaseNoteThisWillBeWrappedInAnArrayIfYouRequestBySymbolUsingTheV2EndpointCategory,
            value,
        )
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CRYPTOCURRENCIES_INFO_CRYPTOCURRENCY_OBJECT_PLEASE_NOTE_THIS_WILL_BE_WRAPPED_IN_AN_ARRAY_IF_YOU_REQUEST_BY_SYMBOL_USING_THE_V2_ENDPOINT_CATEGORY_VALUES!r}"
    )
