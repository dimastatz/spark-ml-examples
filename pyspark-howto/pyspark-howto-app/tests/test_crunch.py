import cruncher
from tests.common import spark
from models.lead import SfdcLead
from models.lead_lean import LeadLean
from tests.utils.tenant_fixture import *
import tests.utils.test_data_generator as test_data_generator


def test_crunch(tenant):
    test_data_generator.generate_sfdc_lead()
    test_data_generator.generate_lead_sf_fields()
    assert SfdcLead.count() == 1
    assert LeadLean.is_empty()
    cruncher.crunch(spark=spark)
    assert LeadLean.count() == 1

    assert tenant == 1