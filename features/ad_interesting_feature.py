from tecton import PushFeaturePackage, MaterializationConfig
from pyspark.sql.types import StructType, StructField, IntegerType, TimestampType
import entities

input_schema = StructType([
    StructField("ad_id", IntegerType()),
    StructField("ad_interesting_score", IntegerType()),
    StructField("timestamp", TimestampType())
])

ad_copy_feature = PushFeaturePackage(
      name="ad_interesting_score",
      description="A feature representing how interesting an ad is (as rated by a human.)",
      entities=[entities.ad_entity],
      materialization=MaterializationConfig(
          serving_ttl='7days',
          online_enabled=True,
          offline_enabled=True
    ),
    input_schema=input_schema,
    timestamp_key='timestamp'
)