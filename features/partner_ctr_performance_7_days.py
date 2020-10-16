from tecton import sql_transformation, TemporalFeaturePackage, DataSourceConfig, MaterializationConfig
import entities as e, data_sources
from datetime import datetime


@sql_transformation(inputs=data_sources.ad_impressions_batch, has_context=True)
def partner_ctr_performance_7_days_transformer(context, ad_impressions_batch):
    return f"""
    SELECT
        partner_id,
        sum(clicked) / count(*) as partner_total_ctr,
        to_timestamp('{context.feature_data_end_time}') as timestamp
    FROM
        {ad_impressions_batch}
    GROUP BY
        partner_id
    """

partner_ctr_performance_7_days = TemporalFeaturePackage(
    name="partner_ctr_performance_7_days",
    description="[SQL Feature] The aggregate CTR of a partner website (clicks / total impressions) over the past 7 days",
    transformation=partner_ctr_performance_7_days_transformer,
    entities=[e.partner_entity],
    materialization=MaterializationConfig(
        offline_enabled=True,
        online_enabled=False,
        feature_start_time=datetime(year=2020, month=6, day=20),
        serving_ttl="1d",
        schedule_interval="1d",
        data_lookback_period="7d"
    ),
    family='ad_serving',
    tags={'release': 'development'}
)
