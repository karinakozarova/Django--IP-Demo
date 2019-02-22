from django.db import models
from django.utils.translation import ugettext as _


class Score(models.Model):
    """
    Description: Model Description
    """

    left_player_score = models.PositiveIntegerField(
        default=0
    )

    right_player_score = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _("Score")
        verbose_name_plural = _("Scores")
        ordering = ['created_at']

    def __str__(self):
        return str(self.left_player_score) + "-" + str(self.right_player_score)
