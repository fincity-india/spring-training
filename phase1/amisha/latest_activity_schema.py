
from sqlalchemy import TEXT, Column, DateTime, Integer, String


def latest_activity_schema(sample_chunk):
    columns = [
        Column('id', Integer),
        Column('opportunity_id', String(255)),
        Column('is_verified', Integer),
        Column('activity_id', String(255)),
        Column('activity_date', DateTime),
        Column('status', String(255)),
        Column('status_date', DateTime),
        Column('sub_status', String(255)),
        Column('sub_status_date', DateTime),
        Column('first_activity', String(255)),
        Column('first_activity_date', DateTime),
        Column('follow_up', String(255)),
        Column('follow_up_date', DateTime),
        Column('next_follow_up', String(255)),
        Column('next_follow_up_date', DateTime),
        Column('visit_proposed', String(255)),
        Column('visit_proposed_date', DateTime),
        Column('visit_confirmed', String(255)),
        Column('visit_confirmed_date', DateTime),
        Column('visit_done', String(255)),
        Column('visit_done_date', DateTime),
        Column('meeting_proposed', String(255)),
        Column('meeting_proposed_date', DateTime),
        Column('meeting_done', String(255)),
        Column('meeting_done_date', DateTime),
        Column('booking_done', String(255)),
        Column('booking_done_date', DateTime),
        Column('reassigned', String(255)),
        Column('reassigned_date', DateTime),
        Column('latest_comment', TEXT),
        Column('lost', String(255)),
        Column('opportunity_lost_reason', String(255)),
        Column('non_contactable', String(255)),
        Column('opportunity_non_contactable_reason', String(255)),
        Column('customer_called_count', Integer),
        Column('called_customer_count', Integer),
        Column('created_at', DateTime),
        Column('updated_at', DateTime),
        Column('is_active', Integer),
    ]
    return columns