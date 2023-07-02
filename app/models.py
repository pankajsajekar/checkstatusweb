from django.db import models
import uuid
from django.utils.translation import gettext as _

# Create your models here.
class CertificateModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serialno = models.CharField(_('Serial No'), max_length=250, blank=True, null=True)
    issuingdate = models.DateField(_('Issue Date'), blank=True, null=True)
    validtill = models.DateField(_('Valid Till'), blank=True, null=True)
    createddate = models.DateField(auto_now_add=True, auto_now=False, blank=True, null=True)

    class Meta:
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")

    def __str__(self):
        return self.namserialnoe

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})