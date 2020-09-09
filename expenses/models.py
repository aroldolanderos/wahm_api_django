"""Expenses model."""

import uuid

# Django
from django.db import models
from django.utils import timezone

class Expense(models.Model):
    """Expenses model."""

    CATEGORIES = (
        ('P', 'Poduct'),
        ('S', 'Service'),
    )

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    amount = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=1, choices=CATEGORIES)
    description = models.TextField(max_length=256)
    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
        null=False,
        blank=False
    )

    class Meta:
        """Meta option."""
        get_latest_by = 'created_at'
        ordering = ['-created_at']

    def __str__(self):
        """Return menu_id."""
        return '{}: ${}'.format(self.description, self.amount)
