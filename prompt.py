# import pathway as pw #it is a high level interface for defining data transformations,aggregations and other data streams
# from datetime import datetime
# from common.openaiapi_helper import openai_chat_completion #used for completing the chats and the searched texts


# def prompt(index, embedded_query, user_query):

#     @pw.udf
#     def build_prompt(local_indexed_data, query):
#         docs_str = "\n".join(local_indexed_data)
#         prompt = f"Given the following data: \n {docs_str} \nanswer this query: {query}, Assume that current date is: {datetime.now()}. and clean the output"
#         return prompt

#     query_context = embedded_query + index.get_nearest_items(
#         embedded_query.vector, k=3, collapse_rows=True
#     ).select(local_indexed_data_list=pw.this.doc).promise_universe_is_equal_to(embedded_query)

#     prompt = query_context.select(
#         prompt=build_prompt(pw.this.local_indexed_data_list, user_query)
#     )

#     return prompt.select(
#         query_id=pw.this.id,
#         result=openai_chat_completion(pw.this.prompt),
#     )
import pathway as pw
from datetime import datetime
from common.openaiapi_helper import openai_chat_completion

def flight_query(index, embedded_query, flight_data):

    @pw.udf
    def build_flight_prompt(local_indexed_data, data):
        flight_details_str = "\n".join(local_indexed_data)
        prompt = f"Given the following flight data: \n {flight_details_str} \nanswer this query: {data['source']} to {data['destination']} on {data['date']}, Assume that current date is: {datetime.now()}. and clean the output"
        return prompt

    query_context = embedded_query + index.get_nearest_items(
        embedded_query.vector, k=3, collapse_rows=True
    ).select(local_indexed_data_list=pw.this.doc).promise_universe_is_equal_to(embedded_query)

    prompt = query_context.select(
        prompt=build_flight_prompt(pw.this.local_indexed_data_list, flight_data)
    )

    return prompt.select(
        query_id=pw.this.id,
        result=openai_chat_completion(pw.this.prompt),
    )
