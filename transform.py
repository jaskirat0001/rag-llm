# import pathway as pw

# def concat_with_titles(**kwargs) -> str:
#     combined = [f"{title}: {value}" for title, value in kwargs.items()]
#     return ', '.join(combined)

# def transform(flight_data):
#     return flight_data.select(
#         details=pw.apply(concat_with_titles, **flight_data),
#     )
import pathway as pw

def concat_flight_details(**kwargs) -> str:
    combined = [f"{title}: {value}" for title, value in kwargs.items()]
    return ', '.join(combined)

def transform_flight_details(flight_data):
    return flight_data.select(
        details=pw.apply(concat_flight_details, **flight_data),
    )
