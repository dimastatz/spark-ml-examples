import cruncher
import tests.utils.test_data_generator as test_data_generator

from models.lead import SfdcLead
from tests.utils.common import spark
from models.lead_lean import LeadLean
from tests.utils.tenant_fixture import *


def test_crunch(tenant):
    test_data_generator.generate_sfdc_lead()
    assert SfdcLead.count() == 1 
    assert LeadLean.is_empty() 
    
    #test_data_generator.generate_lead_sf_fields()
    #assert SfdcLead.count() == 1
    
    cruncher.crunch(spark=spark)
    #assert LeadLean.count() == 1
    assert tenant == 1