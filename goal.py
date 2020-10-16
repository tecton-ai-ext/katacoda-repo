# from tecton import PushFeatureTable
# from tecton.types import Schema, Integer, Timestamp
# import entities

# input_schema = Schema(
#     ("ad_id", Integer),
#     ("ad_interesting_score", Integer),
#     ("timestamp", Timestamp)
# )

# ad_copy_feature = PushFeatureTable(
#     name="ad_interesting_score",
#     description="A feature representing how interesting an ad is (as rated by a human.)",
#     entities=[entities.ad_entity],
#     input_schema=input_schema
# )