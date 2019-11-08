# pylint: disable=invalid-name
from builtins import object
from enum import Enum

import related

from models.python.dashboard.schema_20190524.visualization_settings import (
    VisualizationSettings,
    VisualizationType,
)

DEFAULT_COLUMN_COUNT = 6


class DateRangeType(Enum):
    '''
    An enumeration for defining different types of date ranges
    '''

    CUSTOM = 'CUSTOM'
    FORECAST = 'FORECAST'
    CURRENT_CALENDAR_MONTH = 'CURRENT_CALENDAR_MONTH'
    CURRENT_QUARTER = 'CURRENT_QUARTER'
    PREVIOUS_CALENDAR_DAY = 'PREVIOUS_CALENDAR_DAY'
    PREVIOUS_CALENDAR_WEEK = 'PREVIOUS_CALENDAR_WEEK'
    PREVIOUS_CALENDAR_MONTH = 'PREVIOUS_CALENDAR_MONTH'
    PREVIOUS_QUARTER = 'PREVIOUS_QUARTER'
    PREVIOUS_CALENDAR_YEAR = 'PREVIOUS_CALENDAR_YEAR'
    LAST_365_DAYS = 'LAST_365_DAYS'
    ALL_TIME = 'ALL_TIME'
    ET_CHOOSE_MONTHS = 'ET_CHOOSE_MONTHS'


@related.mutable(strict=True)
class DashboardOptions(object):
    title = related.StringField('New Dashboard')
    column_count = related.IntegerField(DEFAULT_COLUMN_COUNT, key='columnCount')
    show_filter_button = related.BooleanField(False, key='showDashboardFilterButton')


@related.mutable(strict=True)
class LayoutSize(object):
    id = related.StringField()
    rows = related.IntegerField()
    columns = related.IntegerField()


# TODO(stephen, anyone): Replace the sequence fields in the AQT query definition
# with references to their true models. Cannot reference the inidividual models
# directly, though, since they get serialized in their `flask_potion` style and
# not in their backend style.
@related.mutable(strict=True)
class AdvancedFieldDefinition(object):
    id = related.StringField()
    calculation = related.ChildField(dict)
    canonical_name = related.StringField(key='canonicalName')
    category = related.ChildField(dict)
    customizable_filter_items = related.SequenceField(
        dict, key='customizableFilterItems'
    )
    description = related.StringField()
    label = related.StringField()
    short_name = related.StringField(key='shortName')
    source = related.ChildField(dict)


@related.mutable(strict=True)
class QueryDefinition(object):
    id = related.StringField()
    advanced_fields = related.SequenceField(
        AdvancedFieldDefinition, [], key='advancedFields'
    )
    advanced_filters = related.SequenceField(dict, [], key='advancedFilters')
    advanced_groups = related.SequenceField(dict, [], key='advancedGroups')
    name = related.StringField(required=False)
    magic_filter_ids = related.SequenceField(str, [], key='magicFilters')
    date_range_id = related.StringField('', key='dateRangeId')
    group_by = related.StringField('', key='groupBy')


@related.mutable(strict=True)
class FilterDefinition(object):
    id = related.StringField()
    filter_on = related.StringField(key='filterOn')
    filter_values = related.SequenceField(str, [], key='filterValues')
    name = related.StringField(required=False)


@related.mutable(strict=True)
class DateRangeSpecification(object):
    id = related.StringField()
    date_type = related.ChildField(DateRangeType, key='dateType')
    end_date = related.DateTimeField(key='endDate')
    start_date = related.DateTimeField(key='startDate')


@related.mutable(strict=True)
class CustomField(object):
    id = related.StringField()
    field_ids = related.SequenceField(str, key='fieldIds')
    formula = related.StringField()
    name = related.StringField(required=False)


@related.mutable(strict=True)
class LayoutItem(object):
    id = related.StringField()
    query_id = related.StringField(key='queryId')
    item_type = related.ChildField(VisualizationType, key='type')
    upper_x = related.IntegerField(key='upperX')
    upper_y = related.IntegerField(key='upperY')
    size_id = related.StringField(key='sizeId')
    custom_fields = related.SequenceField(CustomField, [], key='customFields')

    # TODO(stephen, anyone): Add full model for filter modal selections and
    # frontend selections filter.
    filter_modal_selections = related.ChildField(dict, {}, key='filterModalSelections')
    front_end_selections_filter = related.ChildField(
        dict, {}, key='frontendSelectionsFilter'
    )
    name = related.StringField(required=False)
    is_advanced_query_item = related.BooleanField(False, key='isAdvancedQueryItem')
    is_locked = related.BooleanField(False, key='isLocked')
    setting_id = related.StringField(required=False, key='settingId')


@related.mutable(strict=True)
class DashboardSpecification(object):
    version = related.StringField()
    date_ranges = related.MappingField(
        DateRangeSpecification, 'id', {}, key='dateRanges'
    )
    filters = related.MappingField(FilterDefinition, 'id', {})
    items = related.MappingField(LayoutItem, 'id', {})
    queries = related.MappingField(QueryDefinition, 'id', {})
    settings = related.MappingField(VisualizationSettings, 'id', {})
    sizes = related.MappingField(LayoutSize, 'id', {})
    options = related.ChildField(DashboardOptions, DashboardOptions())