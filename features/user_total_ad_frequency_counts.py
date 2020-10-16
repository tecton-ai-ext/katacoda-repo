from datetime import datetime
from tecton import TemporalAggregateFeaturePackage, FeatureAggregation, DataSourceConfig, sql_transformation, MaterializationConfig
import entities, data_sources

@sql_transformation(inputs=data_sources.ad_impressions_stream)
def user_total_ad_frequency_counts_transformer(input_df):
    return f"""
        select
            user_uuid,
            1 as impression,
            timestamp
        from
            {input_df}
        """


user_total_ad_frequency_counts = TemporalAggregateFeaturePackage(
    name="user_total_ad_frequency_counts",
    description="[Stream Feature] The totals ads a user has been shown across all websites",
    entities=[entities.user_entity],
    transformation=user_total_ad_frequency_counts_transformer,
    aggregation_slide_period="1h",
    aggregations=[FeatureAggregation(column="impression", function="count", time_windows=["1h", "12h", "24h","72h","168h"])],
    materialization=MaterializationConfig(
        online_enabled=True,
        offline_enabled=True,
        feature_start_time=datetime(2020, 6, 1),
    ),
    family='ad_serving',
    tags={'release': 'production'}
)
