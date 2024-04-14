from django.db import models
from users.models import CustomUser
from event_topics.models import EventTopic, EventSubTopic


class EventType(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.CharField(max_length=200, null=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.name}"


class Group(models.Model):
    name = models.CharField(max_length=200, null=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(null=True)
    modified_at = models.DateTimeField(null=True)
    social_links = models.JSONField(null=True)
    about = models.TextField(null=True)
    banner_url = models.CharField(max_length=200, null=True)
    logo_url = models.CharField(max_length=200, null=True)
    deleted_at = models.DateTimeField(null=True)
    follower_count = models.IntegerField(default=0)
    thumbnail_image_url = models.URLField(null=True, blank=True)
    is_promoted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class DiscountCode(models.Model):
    code = models.TextField(max_length=200, null=True)
    value = models.FloatField(null=True)
    type = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(null=True)
    tickets_number = models.IntegerField(null=True)
    min_quantity = models.IntegerField(null=True)
    max_quantity = models.IntegerField(null=True)
    valid_from = models.DateTimeField(null=True)
    valid_till = models.DateTimeField(null=True)
    event_id = models.ForeignKey("Event", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(null=True)
    marketer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    used_for = models.CharField(max_length=200, null=True)
    discount_url = models.CharField(max_length=200, null=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.code}"

class Event(models.Model):
    identifier = models.CharField(max_length=8)
    name = models.CharField(max_length=255, null=False)
    external_event_url = models.URLField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)
    starts_at = models.DateTimeField(null=False)
    ends_at = models.DateTimeField(null=False)
    timezone = models.CharField(max_length=50, null=False, default="UTC")
    online = models.BooleanField(default=False)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    location_name = models.CharField(max_length=255, blank=True, null=True)
    searchable_location_name = models.CharField(max_length=255, blank=True, null=True)
    public_stream_link = models.CharField(max_length=255, blank=True, null=True)
    stream_loop = models.BooleanField(default=False)
    stream_autoplay = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_promoted = models.BooleanField(default=False)
    is_demoted = models.BooleanField(default=False)
    is_chat_enabled = models.BooleanField(default=False)
    is_videoroom_enabled = models.BooleanField(default=False)
    is_document_enabled = models.BooleanField(default=False)
    document_links = models.JSONField(blank=True, null=True)
    chat_room_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    after_order_message = models.TextField(blank=True, null=True)
    original_image_url = models.URLField(blank=True, null=True)
    thumbnail_image_url = models.URLField(blank=True, null=True)
    large_image_url = models.URLField(blank=True, null=True)
    show_remaining_tickets = models.BooleanField(default=False)
    icon_image_url = models.URLField(blank=True, null=True)
    owner_name = models.CharField(max_length=255, blank=True, null=True)
    is_map_shown = models.BooleanField(default=False)
    is_oneclick_signup_enabled = models.BooleanField(default=False)
    has_owner_info = models.BooleanField(default=False)
    owner_description = models.CharField(max_length=255, blank=True, null=True)
    is_sessions_speakers_enabled = models.BooleanField(default=False)
    is_cfs_enabled = models.BooleanField(default=False)
    privacy = models.CharField(max_length=10, default="public")
    state = models.CharField(max_length=10, default="draft")
    is_announced = models.BooleanField(default=False)
    ticket_url = models.CharField(max_length=255, blank=True, null=True)
    code_of_conduct = models.CharField(max_length=255, blank=True, null=True)
    schedule_published_on = models.DateTimeField(blank=True, null=True)
    is_ticketing_enabled = models.BooleanField(default=False)
    is_donation_enabled = models.BooleanField(default=False)
    is_ticket_form_enabled = models.BooleanField(default=True)
    is_badges_enabled = models.BooleanField(default=False)
    payment_country = models.CharField(max_length=100, blank=True, null=True)
    payment_currency = models.CharField(max_length=100, blank=True, null=True)
    paypal_email = models.CharField(max_length=255, blank=True, null=True)
    is_tax_enabled = models.BooleanField(default=False)
    is_billing_info_mandatory = models.BooleanField(default=False)
    can_pay_by_paypal = models.BooleanField(default=False)
    can_pay_by_stripe = models.BooleanField(default=False)
    can_pay_by_cheque = models.BooleanField(default=False)
    can_pay_by_bank = models.BooleanField(default=False)
    can_pay_by_invoice = models.BooleanField(default=False)
    can_pay_by_onsite = models.BooleanField(default=False)
    can_pay_by_omise = models.BooleanField(default=False)
    can_pay_by_alipay = models.BooleanField(default=False)
    can_pay_by_paytm = models.BooleanField(default=False)
    cheque_details = models.CharField(max_length=255, blank=True, null=True)
    bank_details = models.CharField(max_length=255, blank=True, null=True)
    onsite_details = models.CharField(max_length=255, blank=True, null=True)
    invoice_details = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(null=True)
    pentabarf_url = models.CharField(max_length=255, blank=True, null=True)
    ical_url = models.CharField(max_length=255, blank=True, null=True)
    xcal_url = models.CharField(max_length=255, blank=True, null=True)
    is_sponsors_enabled = models.BooleanField(default=False)
    refund_policy = models.CharField(max_length=255, blank=True, null=True)
    is_stripe_linked = models.BooleanField(default=False)
    completed_order_sales = models.IntegerField(default=0)
    placed_order_sales = models.IntegerField(default=0)
    pending_order_sales = models.IntegerField(default=0)
    completed_order_tickets = models.IntegerField(default=0)
    placed_order_tickets = models.IntegerField(default=0)
    pending_order_tickets = models.IntegerField(default=0)
    discount_code_id = models.ForeignKey(DiscountCode, on_delete=models.CASCADE, null=True, blank=True)
    event_type_id = models.ForeignKey(EventType, on_delete=models.CASCADE, null=True, blank=True)
    event_topic_id = models.ForeignKey(EventTopic, on_delete=models.CASCADE, null=True, blank=True)
    event_sub_topic_id = models.ForeignKey(EventSubTopic, on_delete=models.CASCADE, null=True, blank=True)
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Exhibitors(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    position = models.IntegerField(default=0)
    logo_url = models.CharField(max_length=200, blank=True, null=True)
    banner_url = models.CharField(max_length=200, blank=True, null=True)
    video_url = models.CharField(max_length=200, blank=True, null=True)
    slides_url = models.URLField(null=True, blank=True)
    social_links = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=2147483647, null=True, blank=True, default="pending")
    contact_email = models.EmailField(null=True, blank=True)
    contact_link = models.URLField(null=True, blank=True)
    enable_video_room = models.BooleanField(default=False)
    thumbnail_image_url = models.URLField(null=True, blank=True)
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name}"