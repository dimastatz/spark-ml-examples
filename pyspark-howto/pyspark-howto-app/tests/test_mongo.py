import mongomock
from models.lead import *
from mongoengine import *
from tests.utils.tenant_fixture import *
from tests.utils.test_data_generator import *


def test_leads(spark_session):
    connect('mongoenginetest', 
            host='mongodb://localhost',
            mongo_client_class=mongomock.MongoClient, 
            uuidRepresentation='standard')
    
    lead = SfdcLead()
    lead.FirstName = 'Lead'
    lead.LastName = 'Leader'
    lead.save()

    first = SfdcLead.objects().first()
    assert first.FirstName == lead.FirstName

    first_dic = cast_mongo_id(dict(first.to_mongo()))

    df = spark_session.createDataFrame([first_dic])
    assert df.count() == 1

    leads = SfdcLead.objects().as_pymongo()
    assert len(leads) == 1 and type(leads[0]) is dict

    df.show(truncate=False)
    disconnect()


def test_write(mongo_client):
    lead_in = { 'name': 'lead 1', 'company': 'lead 1 company' }
    lead_id = write(mongo_client, 'leads_db', 'leads', lead=lead_in)
    #print('lead_in', lead_id)
    lead_out = read(mongo_client, 'leads_db', 'leads', company='lead 1 company')
    #print('lead_out', lead_out[0], type(lead_out[0]))
    assert lead_in['name'] == lead_out[0]['name']
    assert lead_id == lead_out[0]['_id']


def test_mongo_to_df(mongo_client, spark_session):
    # populate DB
    for i in range(1, 4):
        lead_in = { 'name': f'lead {i}', 'company': f'lead {i} company' }
        write(mongo_client, 'leads_db', 'leads', lead_in)
    
    # fetch DB content
    leads = read(mongo_client, 'leads_db', 'leads', company='lead *')
    assert len(leads) == 4

    leads = [cast_mongo_id(l) for l in leads]
    df = spark_session.createDataFrame(leads)
    df.show(truncate=False)

    assert df.count() == 4


def test_compare_df(mongo_client, spark_session):
    def are_dfs_equal(df1, df2, col): 
        return (df1.schema == df2.schema) and \
        (df1.sort(col).collect() == df2.sort(col).collect())
    

    leads = read(mongo_client, 'leads_db', 'leads', company='lead *')
    leads = [cast_mongo_id(l) for l in leads]
    
    df1 = spark_session.createDataFrame(leads)
    df1.show()

    leads2 = leads[::-1]
    df2 = spark_session.createDataFrame(leads2)
    df2.show()

    assert are_dfs_equal(df1, df2, '_id')



    

    
