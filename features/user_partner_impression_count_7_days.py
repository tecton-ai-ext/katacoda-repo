from tecton import pyspark_transformation, TemporalFeaturePackage, DataSourceConfig, MaterializationConfig
import entities, data_sources
from datetime import datetime


@pyspark_transformation(inputs=data_sources.ad_impressions_batch, has_context=True)
def user_partner_impression_count_7_days_transformer(context, input_df):
    import pyspark.sql.functions as F

    user_website_views = input_df.groupBy("user_uuid", "partner_id").agg(F.count(F.col("*")).alias("user_partner_impressions_7_days"))
    user_website_views = user_website_views.withColumn("timestamp", F.to_timestamp(F.lit(context.feature_data_end_time)))
    return user_website_views

user_partner_impression_count_7_days = TemporalFeaturePackage(
    name="user_partner_impression_count_7_days",
    description="[Pyspark Feature] The number of ads a user has been shown on a given partner site over the past 7 days",
    transformation=user_partner_impression_count_7_days_transformer,
    entities=[entities.user_entity, entities.partner_entity],
    materialization=MaterializationConfig(
        offline_enabled=True,
        online_enabled=True,
        feature_start_time=datetime(year=2020, month=6, day=20),
        serving_ttl="1d",
        schedule_interval="1d",
        data_lookback_period="7d"
    ),
    family='ad_serving',
    tags={'release': 'production'}
)