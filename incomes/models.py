"""Menus model."""

import uuid

# Django
from django.db import models
from django.utils import timezone


class Income(models.Model):
    """Incomes model."""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField(max_length=50, blank=False)
    amount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now, editable=False, null=False, blank=False)

    class Meta:
        """Meta option."""
        get_latest_by = 'created_at'
        ordering = ['-created_at']

    def __str__(self):
        """Return menu_id."""
        return '{}: ${}'.format(self.description, self.amount)
