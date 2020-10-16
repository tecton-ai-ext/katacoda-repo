from datetime import datetime
from tecton import TemporalAggregateFeaturePackage, FeatureAggregation, DataSourceConfig, sql_transformation, MaterializationConfig
import entities, data_sources

@sql_transformation(inputs=data_sources.ad_impressions_stream)
def content_keyword_ctr_performance_transformer(input_df):
    return f"""
        select
            content_keyword,
            clicked,
            1 as impression,
            timestamp
        from
            {input_df}
        """


content_keyword_ctr_performance = TemporalAggregateFeaturePackage(
    name="content_keyword_ctr_performance",
    description="[Stream Feature] The aggregate CTR of a content_keyword across all impressions (clicks / total impressions)",
    entities=[entities.content_keyword_entity],
    transformation=content_keyword_ctr_performance_transformer,
    aggregation_slide_period="1h",
    aggregations=[
        FeatureAggregation(column="impression", function="count", time_windows=["1h", "12h", "24h","72h","168h"]),
        FeatureAggregation(column="clicked", function="sum", time_windows=["12h", "24h","72h","168h"])
        ],
    materialization=MaterializationConfig(
        online_enabled=True,
        offline_enabled=True,
        feature_start_time=datetime(2020, 6, 1),
    ),
    family='ad_serving',
    tags={'release': 'development'}
)
