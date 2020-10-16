from datetime import datetime
from tecton import TemporalAggregateFeaturePackage, FeatureAggregation, DataSourceConfig, sql_transformation, MaterializationConfig
import entities, data_sources

@sql_transformation(inputs=data_sources.ad_impressions_batch)
def ad_group_ctr_performance_transformer(input_df):
    return f"""
        select
            ad_group_id,
            clicked,
            1 as impression,
            timestamp
        from
            {input_df}
        """


ad_group_ctr_performance = TemporalAggregateFeaturePackage(
    name="ad_group_ctr_performance:v1",
    description="[Batch Feature] The aggregate CTR of an ad_group across all impressions (clicks / total impressions)",
    entities=[entities.ad_group_entity.with_join_keys('ad_group_id')],
    transformation=ad_group_ctr_performance_transformer,
    aggregation_slide_period="1h",
    aggregations=[
        FeatureAggregation(column="impression", function="count", time_windows=["1h", "12h", "24h","72h","168h"]),
        FeatureAggregation(column="clicked", function="sum", time_windows=["1h", "12h", "24h","72h","168h"])
        ],
    materialization=MaterializationConfig(
        online_enabled=True,
        offline_enabled=True,
        feature_start_time=datetime(2020, 6, 1),
    ),
    family='ad_serving',
    tags={'release': 'development'}
)


ad_group_ctr_performance_2 = TemporalAggregateFeaturePackage(
    name="ad_group_ctr_performance:experimental",
    description="[Batch Feature] The aggregate CTR of an ad_group across all impressions (clicks / total impressions)",
    entities=[entities.ad_group_entity.with_join_keys('ad_group_id')],
    transformation=ad_group_ctr_performance_transformer,
    aggregation_slide_period="1h",
    aggregations=[
        FeatureAggregation(column="impression", function="count", time_windows=["1h", "12h", "24h","72h","7000h"]),
        FeatureAggregation(column="clicked", function="sum", time_windows=["1h", "12h", "24h","72h","168h"])
        ],
    materialization=MaterializationConfig(
        online_enabled=True,
        offline_enabled=True,
        feature_start_time=datetime(2020, 6, 1),
    ),
    family='ad_serving',
    tags={'release': 'development'}
)
